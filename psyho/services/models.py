from django.core.validators import MaxValueValidator
from django.db import models

from clients.models import Client


class Service(models.Model):
    name = models.CharField(max_length=50)
    full_price = models.PositiveIntegerField()  # Целое число

    def __str__(self):
        return f"Service: {self.name}, Price: {self.full_price}"


class Plan(models.Model):
    PLAN_TYPES = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('discount', 'Discount')
    )

    plan_type = models.CharField(choices=PLAN_TYPES, max_length=10)
    discount_percent = models.PositiveIntegerField(default=0,
                                                   validators=[
                                                       MaxValueValidator(100)
                                                   ])

    def __str__(self):
        return f"Discount_plan: {self.pk} {self.plan_type} = {self.discount_percent}%"


class Subscription(models.Model):
    client = models.ForeignKey(Client, related_name='subscriptions',
                               on_delete=models.PROTECT)  # client.subscriptions.all()
    service = models.ForeignKey(Service, related_name='subscriptions',
                                on_delete=models.PROTECT)  # service.subscriptions.all()
    plan = models.ForeignKey(Plan, related_name='subscriptions',
                             on_delete=models.PROTECT)  # service.subscriptions.all()

    def __str__(self):
        return f"Subscription for: {self.client}, {self.service}, {self.plan}"

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

import random
import string


def random_alphanumeric_string():
    return ''.join(
        random.choices(
            # string.ascii_letters + string.digits,
            string.digits,
            k=12
        )
    )

class Package(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    # receive_date = models.DateField(null=True)
    short_description = models.TextField(null=True, blank=True)
    track_id = models.CharField(default=random_alphanumeric_string(),max_length=500, unique=True, null=False, blank=False)
    receiver = models.CharField(max_length=500, null=True, blank=True)
    sender = models.CharField(max_length=500, null=True, blank=True)
    phone_number = PhoneNumberField(blank=True)
    destination_address = models.CharField(
        max_length=500, null=True, blank=True)
    destination_country = models.CharField(
        max_length=500, null=True, blank=True)
    arrival_date = models.DateTimeField(max_length=500, null=True, blank=True)
    current_location = models.CharField(max_length=500, null=True, blank=True)

    SALE_STATUS = (
        ('Still at station', 'Still at Station'),
        ('On transit', 'On Transit'),
        ('On hold', 'On Hold'),
        ('Arrived in destination', 'Arrived in Destination'),
        ('Delivered', 'Delivered')
    )
    delivery_status = models.CharField(choices=SALE_STATUS,
                                       default='Still at station', max_length=50, null=True)

    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

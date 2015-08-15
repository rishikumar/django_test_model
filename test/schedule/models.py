from django.db import models

from test.account.models import Account


class Schedule(models.Model):
    class Meta:
        db_table = 'test_schedule'

    account = models.ForeignKey(Account)
from django.db import models


class Account(models.Model):
    class Meta:
        db_table = 'test_account'

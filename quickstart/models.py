from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Participation(models.Model):
    username = models.CharField(null=False, max_length=60)
    class_id = models.CharField(null=False, max_length=60)

    class Meta:
        db_table = "participation_file"


class Stt(models.Model):
    class_id = models.CharField(null=False, max_length=60)
    stt_file = models.CharField(max_length=100000000)

    class Meta:
        db_table = "stt_file"


class Summary(models.Model):
    class_id = models.CharField(null=False, max_length=60)
    summary_file = models.CharField(max_length=100000000)

    class Meta:
        db_table = "summary_file"

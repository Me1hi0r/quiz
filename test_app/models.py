from django.db import models
from django.contrib.auth.forms import User


class MyUser(User):
    select_test = models.IntegerField(default=0)
    select_quest = models.IntegerField(default=0)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    used_1 = models.BooleanField(default=False, blank=False, verbose_name="Use?")
    ans_1 = models.CharField(max_length=80, blank=True, verbose_name="Answer text:")
    right_1 = models.BooleanField(default=False, blank=True, verbose_name="Right?")
    points_1 = models.SmallIntegerField(default=0, blank=True)
    used_2 = models.BooleanField(default=False, blank=False, verbose_name="Use?")
    ans_2 = models.CharField(max_length=80, blank=True, verbose_name="Answer text:")
    right_2 = models.BooleanField(default=False, blank=True, verbose_name="Right?")
    points_2 = models.SmallIntegerField(default=0, blank=True)
    used_3 = models.BooleanField(default=False, blank=False, verbose_name="Use?")
    ans_3 = models.CharField(max_length=80, blank=True, verbose_name="Answer text:")
    right_3 = models.BooleanField(default=False, blank=True, verbose_name="Right?")
    points_3 = models.SmallIntegerField(default=0, blank=True)
    used_4 = models.BooleanField(default=False, blank=False, verbose_name="Use?")
    ans_4 = models.CharField(max_length=80, blank=True, verbose_name="Answer text:")
    right_4 = models.BooleanField(default=False, blank=True, verbose_name="Right?")
    points_4 = models.SmallIntegerField(default=0, blank=True)
    used_5 = models.BooleanField(default=False, blank=False, verbose_name="Use?")
    ans_5 = models.CharField(max_length=80, blank=True, verbose_name="Answer text:")
    right_5 = models.BooleanField(default=False, blank=True, verbose_name="Right?")
    points_5 = models.SmallIntegerField(default=0, blank=True)

    def __str__(self):
        return self.question_text


class Test(models.Model):
    test_name = models.CharField(max_length=200)
    question = models.ManyToManyField(Question, help_text="Select a question for this test")
    pass_point = models.IntegerField(default=0)
    max_attepts = models.IntegerField(default=1)
    def __str__(self):
        return self.test_name

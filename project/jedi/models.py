from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=100)


class Jedi(models.Model):
    name = models.CharField(max_length=100)
    planet = models.ForeignKey(Planet)


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    planet = models.ForeignKey(Planet)
    age = models.IntegerField()
    email = models.EmailField()
    jedi = models.ForeignKey(Jedi, null=True)


class Question(models.Model):
    text = models.TextField()
    right_answer = models.BooleanField()


class Answer(models.Model):
    candidate = models.ForeignKey(Candidate)
    question = models.ForeignKey(Question)
    answer = models.BooleanField()


class Challenge(models.Model):
    # решил, что на каждой планете по одному ордену, дабы не вводить еще одну сущность
    order = models.ForeignKey(Planet)
    question = models.ManyToManyField(Question)

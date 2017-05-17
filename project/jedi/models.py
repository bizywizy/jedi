from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Jedi(models.Model):
    name = models.CharField(max_length=100)
    planet = models.ForeignKey(Planet)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    planet = models.ForeignKey(Planet)
    age = models.IntegerField()
    email = models.EmailField()
    jedi = models.ForeignKey(Jedi, null=True)

    def __str__(self):
        return "{} from {}".format(self.name, self.planet)


class Question(models.Model):
    text = models.TextField()
    right_answer = models.BooleanField()

    def __str__(self):
        return self.text[:20] + "..."


class Answer(models.Model):
    candidate = models.ForeignKey(Candidate)
    question = models.ForeignKey(Question)
    answer = models.BooleanField()


class Challenge(models.Model):
    # решил, что на каждой планете по одному ордену, дабы не вводить еще одну сущность
    order = models.ForeignKey(Planet)
    question = models.ManyToManyField(Question)

    def __str__(self):
        return "{} order challenge".format(self.order)

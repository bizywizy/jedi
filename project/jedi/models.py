from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# кастомный менеджер для модели Jedi
class JediManager(models.Manager):
    # добавляет поле количество падаванов к джедаю
    def get_queryset(self):
        return super(JediManager, self).get_queryset().annotate(padawans_cnt=models.Count('candidate'))

    # возвращает джедаев, у которых меньше трех падаванов
    def can_teach(self):
        return self.get_queryset().filter(padawans_cnt__lte=3)

    # возвращает джедаев, у которых больше одного падавана
    def more_than_one(self):
        return self.get_queryset().filter(padawans_cnt__gt=1)


class Jedi(models.Model):
    name = models.CharField(max_length=100)
    planet = models.ForeignKey(Planet)
    objects = models.Manager()  # для удобства оставим дефолтный менеджер
    with_padawans = JediManager()

    def __str__(self):
        return self.name


# кастомный менеджер для модели Candidate,
# нужен для того, чтобы отделять кандидатов, которые еще не стали джедаями
class CandidateManager(models.Manager):
    def get_queryset(self):
        return super(CandidateManager, self).get_queryset().filter(jedi=None)


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    planet = models.ForeignKey(Planet)
    age = models.IntegerField()
    email = models.EmailField()
    jedi = models.ForeignKey(Jedi, null=True)
    objects = CandidateManager()  # переопределяем дефолтный менеджер

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

    class Meta:
        unique_together = (('candidate', 'question'),)


class Challenge(models.Model):
    # решил, что на каждой планете по одному ордену, дабы не вводить еще одну сущность
    order = models.OneToOneField(Planet)
    question = models.ManyToManyField(Question)

    def __str__(self):
        return "{} order challenge".format(self.order)

from django.db import models


# Create your models here.
class onlineuser(models.Model):
    name = models.CharField(max_length=100);
    email = models.CharField(max_length=100);
    pwd = models.CharField(max_length=100);
    gender = models.CharField(max_length=100);
    phone = models.CharField(max_length=100);



class performance(models.Model):
    alg_name = models.CharField(max_length=100)
    sc1 = models.FloatField()
    sc2 = models.FloatField()
    sc3 = models.FloatField()
    sc4 = models.FloatField()

class chat(models.Model):
    name=models.CharField(max_length=100);
    email=models.CharField(max_length=100);
    message=models.TextField();



class Questions(models.Model):
    qid = models.IntegerField()
    Question = models.TextField()
 
class Answers(models.Model):
    qid = models.IntegerField()
    Answer = models.TextField()
 
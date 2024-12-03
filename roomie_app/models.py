from django.db import models
from pytils.translit import slugify
from datetime import datetime
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField("",max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)



class Ad(models.Model):
    foto=models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField("Название квартиры", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    prace = models.CharField("Цена", max_length=50)
    location = models.CharField("Локация", max_length= 100)
    description = models.TextField("Описание квартиры", default="Не указано")
    parking = models.CharField("Парковка", max_length= 150, default="Не указано")
    time = models.DateTimeField("Дата публикации", default=datetime.now)
    contact = models.CharField("Контакты", max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default= 1)

    class Meta:
        verbose_name = "Аренда"
        verbose_name_plural = "Аренды"

    def __str__(self):
        return self.title

    

#объявления
#1-фото квартиры
#2-название
#3-цена
#4-локация
#5-описание
#6-парковка
#7-дата публикации
#8-контакты




class Roommates(models.Model):
    imo = models.ImageField(upload_to='images/', null=True, blank=True)
    name= models.CharField("Имя", max_length=50)
    age = models.CharField("Возраст", max_length=100)
    gender = models.CharField("Пол", max_length=30)
    city = models.CharField("Город", max_length=50)
    email = models.CharField("E-mail", max_length=150)
    hobby = models.TextField("Хобби, кого ищете")
    phone = models.CharField("Телефон", max_length=50)

    class Meta:
       verbose_name = "Сожитель"
       verbose_name_plural = "Сожители"

    def __str__(self):
        return self.name


#Сожители
#фото
#1-имя
#2-возраст
#3-пол
#город
#емайл
#4-увлечени/график/кого ищет\
#хобби
#5-лимит аренды/ сколько готов платить
#6-избранное
#7-номер(?)



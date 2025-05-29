from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from django.utils import timezone



class Status(models.Model):
    """
    Модель статусов денежных средств
    """
    name = models.CharField(max_length=255, verbose_name="Название статуса")
    
    class Meta:
        """
        Название модели в админ-панели
        """    
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
    
    
    def __str__(self):
        """
        Возвращение заголовка статуса
        """
        return self.name


class TypePayOut(models.Model):
    """
    Модель типа платежа (пополнение-вывод)
    """
    name = models.CharField(max_length=255, verbose_name="Тип платежа")

    class Meta:
        """
        Название модели в админ-панели
        """    
        verbose_name = 'Платёж'
        verbose_name_plural = 'Тип платежей'
    
    
    def __str__(self):
        """
        Возвращение заголовка типа
        """
        return self.name


class Category(MPTTModel):
    """
    Модель категорий с вложенностью
    """
    title = models.CharField(max_length=255, verbose_name="Название категории")
    slug = models.SlugField(max_length=255, verbose_name="URL категории", blank=True)
    description = models.TextField(verbose_name="Описание категории")
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="children", 
                            verbose_name="Родительская категория")
    type = models.ForeignKey(TypePayOut, on_delete=models.CASCADE, verbose_name="Тип платежа", related_name="categories")

    class MPTTMeta:
        """
        Сортировка по вложенности
        """
        order_insertion_by = ('title',)
        
    
    class Meta:
        """
        Название модели в админ-панели
        """    
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    
    def __str__(self):
        """
        Возвращение заголовка категории
        """
        return self.title
    

class RecordCash(models.Model):
    """
    Модель записи движения денежных средств
    """
    create = models.DateTimeField(verbose_name="Время добавления", editable=True, blank=True)
    amount = models.IntegerField(verbose_name="Сумма")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", related_name="records")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="Статус", related_name="status")
    
    class Meta:
        """
        Название модели в админ-панели
        """
        verbose_name = 'Запись ДДС'
        verbose_name_plural = 'Записи ДДС'
        
    
    def __str__(self):
        return f"{self.amount} ({self.category})"
    
    def save(self, *args, **kwargs):
        if not self.create:
            self.create = timezone.now()
        super().save(*args, **kwargs)
    

class Comment(MPTTModel):
    """
    Модель древовидных комментариев
    """
    record = models.ForeignKey(RecordCash, on_delete=models.CASCADE, verbose_name="Запись", related_name="comments")
    author = models.ForeignKey(User, verbose_name="Автор комментария", on_delete=models.CASCADE, related_name="comments_author")
    content = models.TextField(verbose_name="Текст комментария", max_length=1000)
    time_create = models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновления', auto_now=True)
    parent = TreeForeignKey('self', verbose_name="Родительский комментарий", null=True, blank=True, related_name="children", 
                            on_delete=models.CASCADE)
    
    class MPTTMeta:
        """
        Сортировка по вложенности
        """
        order_insertion_by = ('-time_create')
        
    
    class Meta:
        """
        Сортировка, название модели в админ-панели, таблица с данными
        """
        ordering = ['-time_create']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        
    def __str__(self):
        return f"{self.author}: {self.content}"
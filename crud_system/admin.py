from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin


from .models import Category, Comment, RecordCash, Status, TypePayOut


@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    """
    Админ-панель модели категорий
    """
    prepopulated_fields = {'slug': ('title',)}
    

@admin.register(Comment)
class CommentAdmin(DjangoMpttAdmin):
    """
    Админ-панель модели комментариев
    """
    pass
    
    

@admin.register(RecordCash)
class RecordCashAdmin(admin.ModelAdmin):
    """
    Админ-панель записей ДДС
    """
    list_display = ('amount', 'category', 'status', 'create',)
    list_filter = ('amount', 'category', 'status', 'create',)
    fields = ('amount', 'category', 'status', 'create',)
    search_fields = ('amount', 'category', 'status', 'create',) 


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    """
    Админ-панель статусов записей ДДС
    """
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(TypePayOut)
class TypePayOutAdmin(admin.ModelAdmin):
    """
    Админ-панель типов платежа
    """
    search_fields = ('name',)
    list_filter = ('name',)
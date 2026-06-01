from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Group, Post, Comm, Emoji, Post_Emoji

class CustomUserAdmin(UserAdmin):
    # Какие поля показывать в списке пользователей
    list_display = ('email', 'username', 'name', 'surname', 'group_owner', 'admin', 'is_staff')
    ordering = ('email',)

    # Поля при редактировании пользователя
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Персональные данные', {'fields': ('username', 'name', 'surname')}),
        ('Права и Роли', {'fields': ('group_owner', 'admin', 'is_active', 'is_staff', 'is_superuser')}),
    )

    # Поля при создании нового пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'name', 'surname', 'password'),
        }),
    )

# Регистрируем кастомную модель User со специальными настройками админки
admin.site.register(User, CustomUserAdmin)

# Регистрируем остальные таблицы твоей лабораторной
admin.site.register(Group)
admin.site.register(Post)
admin.site.register(Comm)
admin.site.register(Emoji)
admin.site.register(Post_Emoji)
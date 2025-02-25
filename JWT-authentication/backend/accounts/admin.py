from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreateForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreateForm
    form = CustomUserChangeForm

    models = CustomUser

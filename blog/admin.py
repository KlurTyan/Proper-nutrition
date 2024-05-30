from django.contrib import admin
from .models import Profile, Card, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email"]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "date_of_birth", "photo"]
    raw_id_fields = ["user"]


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ["title"]

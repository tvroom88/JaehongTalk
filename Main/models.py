#-*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin

# Create your models here.
class Member(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)


class MemberAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

admin.site.register(Member, MemberAdmin)
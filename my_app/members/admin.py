from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'phone', 'email', 'gender', 'joined_date')
    list_filter = ('gender', 'joined_date')
    search_fields = ('firstname', 'lastname', 'email')
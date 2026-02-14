from django.contrib import admin

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'email', 'phonenumber', 'enrollment_date')
    search_fields = ('first_name', 'last_name', 'email')

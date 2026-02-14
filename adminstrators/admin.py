from django.contrib import admin

# Register your models here.
class AdministratorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'email', 'phonenumber', 'employee_id')
    search_fields = ('first_name', 'last_name', 'email', 'employee_id')

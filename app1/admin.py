from django.contrib import admin

from app1.models import employee_model
class employee_admin(admin.ModelAdmin):
    list_display=['emp_name','emp_id','emp_mobile','emp_salary']
admin.site.register(employee_model,employee_admin)

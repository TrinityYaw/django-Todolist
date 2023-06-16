from django.contrib import admin
from .models import Task

# Register your models here.



@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    
    fields = ['title',('description','complete','user')]


    @admin.display(description="title [lower case]")
    def lower_case_user_title(self,obj):
        return obj.title.capitalize()
    
    @admin.display(description="description [lower case]")
    def lower_case_user_description(self,obj):
        return obj.description.capitalize()
    
    list_display = ['lower_case_user_title','lower_case_user_description','complete','user']




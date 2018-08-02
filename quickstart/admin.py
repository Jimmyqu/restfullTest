from django.contrib import admin
from .models import Artical,NewsCategory,Users,Vote
# Register your models here.


class ArticalAdmin(admin.ModelAdmin): #admin站显示
    list_display = ('id','category','title','profile','created_time',)

admin.site.register(Artical,ArticalAdmin)
admin.site.register(NewsCategory)
admin.site.register(Users)
admin.site.register(Vote)
# admin.site.register(Comment)


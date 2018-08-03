from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.

class NewsCategory(models.Model):
    category_text = models.CharField(max_length=20,default='国内新闻')
    def __str__(self):
        return self.category_text
    class Meta:
        #站點顯示名稱
        verbose_name_plural='分類'

class Users(models.Model):
    name=models.CharField(null=False,max_length=20,blank=False)
    password = models.CharField(null=False,max_length=50,blank=False)
    mobile = models.CharField(null=False,max_length=20,blank=False)
    #money = models.FloatField(null=False,default=0)

    class Meta:
        verbose_name_plural='用戶'
    def __str__(self):
        return self.name


class Artical(models.Model):
    title=models.CharField(max_length=50,verbose_name='標題')
    created_time= models.DateTimeField(auto_now_add=True,verbose_name='創建時間')
    content = UEditorField(width=800, height=500, toolbars="full", imagePath="../static/course/ueditor/", filePath="../static/course/ueditor/", upload_settings={"imageMaxSize":1204000},default='',verbose_name='內容')
    img = models.ImageField(upload_to='../static/uploadImg', null=True, blank=True)
    category = models.ForeignKey(NewsCategory,on_delete=models.SET_DEFAULT,default=1,verbose_name='新聞分類')


    def __str__(self):
        return self.title

    def profile(self):
        #控制content 显示字段
        if len(str(self.content))>65:
            return '{}...'.format(str(self.content)[:65])
        else:
            return  str(self.content)
    profile.allow_tags = True

    class Meta:
        verbose_name_plural='文章'


class Vote(models.Model):
    user_id= models.ForeignKey(Users,on_delete=models.DO_NOTHING,blank=True,null=True)
    status = models.BooleanField(default=False)
    comment = models.TextField(null=False,max_length=500,blank=True)
    category = models.ForeignKey(Artical, related_name="comments",on_delete=models.DO_NOTHING,blank=True,null=True)
    def __str__(self):
        return str(self.category)
    class Meta:
        verbose_name_plural='點贊'


# class Comment(models.Model):
#     user_id= models.ForeignKey(Users,on_delete=models.DO_NOTHING)
#     bbs_id = models.ForeignKey(Artical,on_delete=models.DO_NOTHING)
#     comment = models.TextField(null=False,max_length=500)
#     def __str__(self):
#         return self.bbs_id
#     class Meta:
#         verbose_name_plural='評論'
#




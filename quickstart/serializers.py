from rest_framework import serializers
from .models import Artical,Users,NewsCategory,Vote

# class UsersSerializer(serializers.Serializer):
#     #可以指明字段 POST時檢查字段 存儲
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(required=True,max_length=20)
#     password = serializers.CharField(required=True,max_length=20)
#     mobile = serializers.CharField(required=True,max_length=20)
#
#     def create(self, validated_data):
#         """
#         根据提供的验证过的数据创建并返回一个新的`Users`实例。
#         """
#         return Users.objects.create(**validated_data)


class UsersSerializer(serializers.ModelSerializer):
    # ModelSerializer 幫我們完成上步的功能
    class Meta:
        model = Users
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = '__all__'
        #fields = ('id','category_text')

class VoteSerializer(serializers.ModelSerializer):
    # 需要外键的对应属性 = rializers.CharField(source='本字段外键名.属性')
    user_name = serializers.CharField(source='user_id.name')
    class Meta:
        model = Vote
        fields = ('id','comment','user_name','status')

class ArticalSerializer(serializers.ModelSerializer):
    # 可將外鍵做ModelSerializer 然後外鍵實例化後  ModelSerializer字段將返回外鍵所有信息
    category=CategorySerializer()
    comments = VoteSerializer(many=True,read_only=True)
    class Meta:
        model = Artical
        # fields = '__all__'
        fields = ('id','title','created_time','content','img','category','comments')




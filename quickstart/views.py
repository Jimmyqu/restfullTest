from django.shortcuts import render
from django.http import HttpResponse
from .models import Artical,Users
from rest_framework.views import APIView #restful對django View的包裝
from rest_framework import generics  #更進一步封裝VIEW
from rest_framework import mixins

from rest_framework.response import Response #對django response的包裝
from .serializers import ArticalSerializer,UsersSerializer # 引入寫好的包裝
from rest_framework import status
from rest_framework import viewsets

# ALLLIST start
# 1 普通 APIView
# class AllList(APIView):
#     def get(self,request,format = None):
#         lists = Artical.objects.all()
#         lists_serializer = ArticalSerializer(lists,many=True)
#         return Response(lists_serializer.data)



# 2 ListAPIView
#class AllList(generics.ListAPIView):
    # def get(self,request,*args,**kwargs):
    #     return self.list(request,*args,**kwargs) #ListAPIView 封裝了Response

    #ListAPIView 幫助返回def get（）數據 並且分頁可用
    # queryset = Artical.objects.all()
    # serializer_class = ArticalSerializer

# 3 viewsets配合restful router使用
# mixins.xxModelMixin 获取数据的各种方式
#  viewsets有很多ViewSet 對應不同請求獲取的數據
class AllList(mixins.RetrieveModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Artical.objects.all()
    serializer_class = ArticalSerializer


# ALLLIST end


# UsersApi start
# class UsersApi(APIView):
#     def get(self,request,format = None):
#         lists = Users.objects.all()
#         lists_serializer = UsersSerializer(lists,many=True)
#         return Response(lists_serializer.data)
#
#     def post(self,request):
#         data = UsersSerializer( data= request.data)  # 序列化post數據
#         if data.is_valid():
#             data.save()
#             return Response(data.data,status=status.HTTP_201_CREATED)
#         return Response(data.errors,status=status.HTTP_400_BAD_REQUEST)

#ListAPIView only get()
#ListCreateAPIView can post()
class UsersApi(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

# UsersApi end
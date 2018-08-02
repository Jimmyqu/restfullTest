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
# class AllList(APIView):
#     def get(self,request,format = None):
#         lists = Artical.objects.all()
#         lists_serializer = ArticalSerializer(lists,many=True)
#         return Response(lists_serializer.data)


class AllList(generics.ListAPIView):
    #ListAPIView 幫助返回def get（）數據 並且分頁可用
    queryset = Artical.objects.all()
    serializer_class = ArticalSerializer

    # def get(self,request,*args,**kwargs):
    #     return self.list(request,*args,**kwargs) #ListAPIView 封裝了Response
#ALLLIST end


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

class UsersApi(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

# UsersApi end
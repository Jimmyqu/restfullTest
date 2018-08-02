#測試普通json

from django.views.generic.base import  View
from .models import Artical
from django.http import  HttpResponse
from django.http import  JsonResponse #提供的快捷放回JSOn
import json
from django.forms.models import  model_to_dict
from django.core import serializers

class ArcticleList(View):
    def get(self,request):
        lists = Artical.objects.all()[:3]
        json_list=[]
        # for item in lists:
        #     json_res = {}
        #     json_res['title']=item.title
        #     json_res['content']=item.content
        #     json_res['created_time']=str(item.created_time)
        #     json_list.append(json_res)

        res= serializers.serialize('json',lists)  # django提供的快速序列化到JSON

        #return HttpResponse(res,content_type='application/json')
        return JsonResponse(json.loads(res),safe=False)


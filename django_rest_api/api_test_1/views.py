from .models import Student
from .serializers import StudentSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.views import View
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

import io


@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        _id = python_data.get('id', None)

        if _id is not None:
            stu = Student.objects.get(id=id)
            serialize = StudentSerializer(stu)
            to_json = JSONRenderer().render(serialize.data)
            return HttpResponse(to_json, content_type="application/json")

        # if the id is None
        stu = Student.objects.all()
        serialize = StudentSerializer(stu, many=True)  # for more than one row or entry
        to_json = JSONRenderer().render(serialize.data)
        return HttpResponse(to_json, content_type="application/json")

    def post(self, request, *args, **kwargs):
        json_data = request.body
        # converts into bytes
        stream = io.BytesIO(json_data)
        # conversion from bytes to json
        python_data = JSONParser().parse(stream)
        # conversion from json to complex objects.(deserialize)
        serialize = StudentSerializer(data=python_data)
        # if everything is valid , then save it
        if serialize.is_valid():
            serialize.save()
            res = {"msg": "Data Created."}
            json_response = JSONRenderer().render(res)
            return HttpResponse(json_response, content_type="application/json")

        # if the data is not valid
        to_json = JSONRenderer().render(serialize.errors)
        return HttpResponse(to_json, content_type="application/json")

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        _id = python_data.get("id")
        stu = Student.objects.get(id=_id)
        serialize = StudentSerializer(stu, data=python_data, partial=True)
        # partial is set to True when we are updating only partial data

        if serialize.is_valid():
            serialize.save()
            res = {"status": "Data updated !"}
            return JsonResponse(res, safe=False)

        json_response = JSONRenderer.render(serialize.errors)
        return HttpResponse(json_response, content_type="application/json")

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        _id = python_data.get("id")
        stu = Student.objects.get(id=_id)
        stu.delete()
        res = {"status": "Data deleted !"}
        return JsonResponse(res, safe=False)

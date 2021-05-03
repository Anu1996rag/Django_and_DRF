from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import StudentSerializer
from .models import Student

# Create your views here.
class StudentAPI(ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serialize = StudentSerializer(stu,many=True)
        return Response(serialize.data)

    def retrieve(self, request, pk=None):
        _id = pk
        if _id is not None:
            stu = Student.objects.get(id=_id)
            serialize = StudentSerializer(stu)
            return Response(serialize.data)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Created.."},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        _id = pk
        if _id is not None:
            stu = Student.objects.get(id=_id)
            serializer = StudentSerializer(stu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"Data updated.."}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        _id = pk
        if _id is not None:
            stu = Student.objects.get(id=_id)
            serializer = StudentSerializer(stu, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Data partially updated.."}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        _id = pk
        if _id is not None:
            stu = Student.objects.get(id=_id)
            stu.delete()
            return Response({"msg": "Data deleted.."}, status=status.HTTP_200_OK)
        return Response({"msg": "Id not found"}, status=status.HTTP_400_BAD_REQUEST)

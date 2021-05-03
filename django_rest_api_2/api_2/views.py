from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer


class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            stu = Student.objects.get(id=pk)  # query set
            serializer = StudentSerializer(stu)  # serialization
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, pk=None, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data created."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        stu = Student.objects.get(pk=pk)
        serialize = StudentSerializer(stu, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({"msg": "Data completely updated."}, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, format=None):
        _id = pk
        stu = Student.objects.get(pk=_id)
        serialize = StudentSerializer(stu, data=request.data, partial=True)
        if serialize.is_valid():
            serialize.save()
            return Response({"msg": "Data partially updated."}, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        _id = pk
        stu = Student.objects.get(pk=_id)  # this points to the record in the table
        stu.delete()
        return Response({"msg": "Data deleted."}, status=status.HTTP_200_OK)

from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import viewsets

from .models import Todo
from .serializers import *

# 전체 조회
class TodosAPIView(APIView):
    # 조회
    def get(self, request):
        todos = Todo.objects.filter(complete=False)
        serializer = TodoSimpleSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Todo 생성 함수 - POST 방식
    def post(self, request):
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# 상세 조회
class TodoAPIView(APIView):
    # 조회
    def get(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Todo 수정
    def put(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoCreateSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# 완료된 Todo 전체조회
class DoneTodosAPIView(APIView):
    def get(self, request):
        dones = Todo.objects.filter(complete=True)                  # complete가 true인 것만 필터링
        serializer = TodoSimpleSerializer(dones, many=True)         # 완료된 Todo(dones)를 TodosimpleSerializer에 전달
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# Todo 완료시키기
class DoneTodoAPIView(APIView):
    def get(self, request, pk):
        done = get_object_or_404(Todo, id=pk)
        done.complete = True                    # Todo 완료시키기(complete = True)
        done.save()                             # 저장!
        serializer = TodoDetailSerializer(done)
        return Response(status=status.HTTP_200_OK)
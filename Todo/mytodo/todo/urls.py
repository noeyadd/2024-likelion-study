from django.urls import path

from .views import *

urlpatterns = [
    path('todo/', TodosAPIView.as_view()),              # Todo 전체조회 & 생성
    path('todo/<int:pk>/', TodoAPIView.as_view()),      # Todo 상세조회 & 수정
    path('done/', DoneTodosAPIView.as_view()),          # 완료된 Todo 전체조회
    path('done/<int:pk>/', DoneTodoAPIView.as_view()),  # Todo 완료시키기
]

from django.urls import path, include
from .views import *

urlpatterns = [
    path("hello/", HelloAPI),
    path("fbv/books/", booksAPI),
    path("fbv/book/<int:bid>", bookAPI),
]
# CRUD에 관련된 모든 정보가 들어있음 - 손쉽게 사용 가능
from rest_framework.viewsets import ModelViewSet
from .serializer import ProductSerializer
from .models import Product

class ProductViewSet(ModelViewSet) :
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
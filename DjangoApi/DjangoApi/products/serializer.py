from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Product
        # migrations에 있는 initial을 참고해서 field를 채우면 된다
        fields = (
            'id',
            'product_name',
            'price'
        )
from django.contrib.auth.models import User                             # User 모델
from django.contrib.auth.password_validation import validate_password   # Django의 기본 패스워드 검증도구
from django.contrib.auth import authenticate                            # 유저를 인증해주는 함수

from rest_framework import serializers
from rest_framework.authtoken.models import Token       # Token 모델
from rest_framework.validators import UniqueValidator   # 이메일 중복 방지를 위한 검증 도구

from .models import *


# 회원가입 시리얼라이저
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],  # 이메일에 대한 중복 검증
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],     # 비밀번호에 대한 검증
    )
    password2 = serializers.CharField(
        write_only=True, 
        required=True       # 비밀번호 확인을 위한 필드
    )       

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    def validate(self, data):   # 비밀번호 일치 여부 확인
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password" : "password fields didn't match."}
            )
        
        return data
    
    def create(self, validated_data):
        # create 요청에 대해 create 메소드를 오버라이딩, 유저를 생성하고 토큰을 생성하게 함
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user
    

# 로그인 시리얼라이저
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError(
            {"error": "Unable to log in with provided credentials."}
        )
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("nickname", "position", "subjects", "image")
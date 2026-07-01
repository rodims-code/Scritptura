from rest_framework import serializers
from .models import User, Cursus, Livret, Lecon, Question, ProgressionLecon, UserAnswer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'student_code', 'username', 'email', 'first_name', 'last_name', 'role', 'phone', 'city', 'country', 'password']
        extra_kwargs = {"password": {"write_only": True}}
    def create(self, validated_data): 
        user = User.objects.create_user(**validated_data)
        return user

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class LeconSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Lecon
        fields = ['id', 'number', 'title', 'questions']

class LivretSerializer(serializers.ModelSerializer):
    lecons = LeconSerializer(many=True, read_only=True)
    class Meta:
        model = Livret
        fields = ['id', 'code', 'title', 'order', 'lecons']

class CursusSerializer(serializers.ModelSerializer):
    livrets = LivretSerializer(many=True, read_only=True)
    class Meta:
        model = Cursus
        fields = ['id', 'title', 'description', 'livrets']

class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}

class ProgressionLeconSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressionLecon
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}
from rest_framework import viewsets, status, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User, Cursus, Livret, Lecon, Question, ProgressionLecon, UserAnswer
from .serializers import (
    UserSerializer, CursusSerializer, 
    LivretSerializer, LeconSerializer, QuestionSerializer, 
    ProgressionLeconSerializer, UserAnswerSerializer
)

# --- CONFIGURATION LOGIQUE D'AUTH ---
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

# --- ACTIONS RECURREMTES (CRUD) ---
class CursusViewSet(viewsets.ModelViewSet):
    queryset = Cursus.objects.all()
    serializer_class = CursusSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LivretViewSet(viewsets.ModelViewSet):
    queryset = Livret.objects.all()
    serializer_class = LivretSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LeconViewSet(viewsets.ModelViewSet):
    queryset = Lecon.objects.all()
    serializer_class = LeconSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = UserAnswerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Un étudiant ne voit que ses réponses, un prof voit tout
        if self.request.user.role in ['TEACHER', 'ADMIN']:
            return UserAnswer.objects.all()
        return UserAnswer.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProgressionLeconViewSet(viewsets.ModelViewSet):
    serializer_class = ProgressionLeconSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role in ['TEACHER', 'ADMIN']:
            return ProgressionLecon.objects.all()
        return ProgressionLecon.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
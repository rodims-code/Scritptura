from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.text import slugify
from uuid import uuid1

# --- UTILISATEUR CUSTOM ---
class User(AbstractUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('STUDENT', 'Étudiant'),
        ('TEACHER', 'Correcteur / Enseignant'),
        ('ADMIN', 'Administrateur'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid1, editable=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    email = models.EmailField(unique=True)
    student_code = models.CharField(max_length=50, unique=True, null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='STUDENT')
    
    # Formulaire de la couverture papier
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def save(self, *args, **kwargs):
        # Génération automatique et sécurisée du username en arrière-plan
        if not self.username and self.first_name and self.last_name:
            base_username = slugify(f"{self.first_name}-{self.last_name}")
            username = base_username
            counter = 1
            while User.objects.filter(username=username).exists():
                username = f"{base_username}{counter}"
                counter += 1
            self.username = username
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student_code or 'Pas de code'} - {self.get_full_name()}"


# --- STRUCTURE DES COURS ---
class Cursus(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Cursus"

    def __str__(self):
        return self.title


class Livret(models.Model):
    cursus = models.ForeignKey(Cursus, on_delete=models.CASCADE, related_name='livrets')
    code = models.CharField(max_length=50, unique=True) # Ex: C2
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.code} - {self.title}"


class Lecon(models.Model):
    livret = models.ForeignKey(Livret, on_delete=models.CASCADE, related_name='lecons')
    number = models.PositiveIntegerField() # De 1 à 10
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Leçon"
        ordering = ['number']

    def __str__(self):
        return f"Leçon {self.number} : {self.title} ({self.livret.code})"


class Question(models.Model):
    TYPE_CHOICES = [
        ('QCM', 'Choix multiples'),
        ('HOLES', 'Texte à trous'),
        ('OPEN', 'Question ouverte'),
        ('LINK', 'Éléments à relier'),
        ('CROSSWORD', 'Verset caché / Grille'),
    ]
    lecon = models.ForeignKey(Lecon, on_delete=models.CASCADE, related_name='questions')
    type = models.CharField(max_length=15, choices=TYPE_CHOICES)
    statement = models.TextField()
    configuration = models.JSONField(help_text="Stocke les options de QCM, les grilles de lettres ou les solutions.")
    points = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"[{self.type}] {self.statement[:30]}... ({self.lecon})"


# --- SUIVI & RÉPONSES ---
class ProgressionLecon(models.Model):
    STATUS_CHOICES = [
        ('LOCKED', 'Verrouillé'),
        ('IN_PROGRESS', 'En cours'),
        ('SUBMITTED', 'Soumis pour correction'),
        ('GRADED', 'Corrigé'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progressions')
    lecon = models.ForeignKey(Lecon, on_delete=models.CASCADE, related_name='progressions')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='LOCKED')
    score = models.PositiveIntegerField(default=0)
    date_submitted = models.DateTimeField(null=True, blank=True)
    date_graded = models.DateTimeField(null=True, blank=True)
    teacher_feedback = models.TextField(blank=True)
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='corrections')

    class Meta:
        verbose_name = "Progression Leçon"
        unique_together = ('user', 'lecon')


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='user_answers')
    response_data = models.JSONField(help_text="Stocke la réponse saisie par l'étudiant.")
    is_correct = models.BooleanField(default=False)
    score_assigned = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Réponse Étudiant"
        unique_together = ('user', 'question')
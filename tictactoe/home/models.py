from django.db import models

class Game(models.Model):
    id = models.BigAutoField(primary_key=True)
    player1 = models.CharField(max_length=20)
    player2 = models.CharField(max_length=20)
    winner = models.CharField(max_length=20, blank=True, null=True)
    draw = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

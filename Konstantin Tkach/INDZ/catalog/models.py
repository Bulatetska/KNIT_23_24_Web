from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=200)       # Назва гри
    description = models.TextField()                 # Опис
    category = models.CharField(max_length=100)      # Категорія (напр. Стратегія)
    author_name = models.CharField(max_length=100)   # Автор гри (за вимогою ТЗ)
    created_at = models.DateTimeField(auto_now_add=True) # Дата додавання
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Ціна")

    def __str__(self):
        return self.title

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    author_name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
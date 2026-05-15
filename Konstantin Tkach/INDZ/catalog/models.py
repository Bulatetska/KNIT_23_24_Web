from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва гри")
    description = models.TextField(verbose_name="Опис")
    category = models.CharField(max_length=100, verbose_name="Жанр")
    author_name = models.CharField(max_length=100, verbose_name="Видавець")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Ціна")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата додавання")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Гра"
        verbose_name_plural = "Ігри"


class Review(models.Model):
    # Зв'язок з грою: при видаленні гри видаляються і її відгуки
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews', verbose_name="Гра")
    author_name = models.CharField(max_length=100, verbose_name="Ім'я автора")
    # ОСЬ ЦЕ ПОЛЕ МИ ВИКОРИСТОВУЄМО В HTML ЯК {{ review.text }}
    text = models.TextField(verbose_name="Текст відгуку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    def __str__(self):
        return f"Відгук від {self.author_name} на {self.game.title}"

    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"
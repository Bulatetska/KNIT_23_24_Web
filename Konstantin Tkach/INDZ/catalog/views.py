from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Game, Review


# Функція для головної сторінки з пошуком
def game_list(request):
    query = request.GET.get('q')
    if query:
        # Шукаємо збіги в назві АБО в категорії
        games = Game.objects.filter(
            Q(title__icontains=query) | Q(category__icontains=query)
        )
    else:
        games = Game.objects.all().order_by('-created_at')

    return render(request, 'catalog/index.html', {'games': games, 'query': query})


# ТІЄЇ ФУНКЦІЇ, ЯКОЇ НЕ ВИСТАЧАЄ:
def game_detail(request, id):
    game = get_object_or_404(Game, id=id)
    reviews = game.reviews.all().order_by('-created_at')

    if request.method == 'POST':
        author = request.POST.get('author_name')
        text = request.POST.get('text')
        if author and text:
            Review.objects.create(game=game, author_name=author, text=text)

    return render(request, 'catalog/game_detail.html', {
        'game': game,
        'reviews': reviews
    })
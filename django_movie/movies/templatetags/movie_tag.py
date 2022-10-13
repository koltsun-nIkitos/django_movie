from django import template
from movies.models import Category, Movie

register = template.Library()

@register.simple_tag()
def get_categories():
    """Вывод всех категорий"""
    return Category.objects.all()

@register.inclusion_tag('movies/tags/last_movie.html')
def get_last_movies(count=5):
    movies = Movie.objects.order_by("id")[:count]
    return {"last_movies" : movies}

@register.simple_tag()
def get_money_str(money):
    """Преобразование денег в отформатированный вид"""
    money_str = str(money)
    invers_money_str = ''
    position = 0
    for char in range(len(money_str)-1, -1, -1):
        if position == 3:
            invers_money_str += ' '
            position = 0
        invers_money_str += money_str[char]
        position += 1
    money_str = '$'    
    for char in range(len(invers_money_str)-1, -1, -1):
        money_str += invers_money_str[char]
    return money_str
    

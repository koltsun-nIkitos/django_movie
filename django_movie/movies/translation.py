from modeltranslation.translator import register, TranslationOptions
from .models import Category, Actor, Movie, Genre, MovieShorts


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Actor)
class ActorTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('title', 'tagline', 'description', 'country')


@register(MovieShorts)
class MovieShotsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
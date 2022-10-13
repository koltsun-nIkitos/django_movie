from django import template
import datetime

register = template.Library()

@register.simple_tag()
def get_age(date_of_birth):
    """Вывод возраста актера"""
    date_now = datetime.date.today()
    age = (date_now - date_of_birth) // 365
    age = str(age)
    age = age[:3]

    return f"{age} лет"
from django.db import models

class Contact(models.Model):
    """Подписка по email"""
    email = models.EmailField("e-mail")
    date = models.DateTimeField("Дата", auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
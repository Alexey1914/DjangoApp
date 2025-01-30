from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    description = models.TextField(null = True, blank = True)
    price = models.FloatField(null = True, blank = True)
    published = models.DateField(auto_now_add = True, db_index = True)

    def __str__(self):
        return self.title + " | " + self.author

    class Meta:
        verbose_name_plural = 'Книги'
        verbose_name = 'Книга'
        ordering = [ 'id' ]
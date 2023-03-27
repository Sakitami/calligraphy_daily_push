from django.db import models


# Create your models here.


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    image_url = models.URLField(max_length=200, blank=True)
    classification = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateField(help_text='文章日期，格式为YYYY-MM-DD')
    view = models.PositiveIntegerField(default=0)
    author = models.CharField(max_length=45, default='李白')
    title = models.CharField(max_length=255, default='test')

    def __str__(self):
        return self.title + ' - ' + str(self.date)

from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(default='')
    year = models.PositiveIntegerField(default=2024)
    imgThumbnail = models.ImageField(upload_to="images", null=True, blank=True)

    def __str__(self):
        return self.title_with_year()

    def title_with_year(self):
        return "{}({})".format(self.title, self.year)

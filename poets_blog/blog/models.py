from django.db import models


# Create your models here.
class Post(models.Model):

    """Docstring for Post. Creating created_at, title, content
       which wi will display in are blog."""
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    tag = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    views = models.IntegerField(default=0)

    def __unicode__(self):
        """TODO: Docstring for __unicode.
        :returns: TODO

        """
        return self.title + "/" + self.content

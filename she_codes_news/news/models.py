# from cProfile import label
# from email.mime import image
# from telnetlib import STATUS
# from turtle import update
from django.contrib.auth import get_user_model
from django.db import models


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    pub_date = models.DateTimeField(verbose_name="Date")
    content = models.TextField()
    image_url = models.URLField(null=True, blank=True, verbose_name= "Image URL", max_length=200)



    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

    # def cache(self):
    #     result = urllib.request.urlretrieve(self.url)
    #     self.photo.save(
    #             os.path.basename(self.url),
    #             File(open(result[0]))
    #             )
    #     self.save()

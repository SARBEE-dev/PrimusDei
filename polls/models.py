from django.db import models
from PIL import Image
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    picture = models.ImageField(default='default.jpg',upload_to='profile_Pics')

    def save(self, *args, **kwargs):
        # change profile image size
        super(Choice, self).save(*args, **kwargs)
        img = Image.open(self.picture.path)
        if img.width > 300 or img.height > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.picture.path)


    def __str__(self):
        return self.choice_text
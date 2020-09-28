import datetime
from django.utils import timezone
from django.db import models


class Question(models.Model):
    """
    Moedel representing a question.
    """
    # we set 'verbose_name' for showing Human_readable texts!
    text = models.CharField(max_length=300, verbose_name='question')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """
        String for representring the Model object.
        """
        return self.text

    def was_published_recently(self):
        """
        Return true if pub_date is in last 24 hours.
        """
        now = timezone.now()
        return (now - datetime.timedelta(days=1)) <= self.pub_date <= now


class Choice(models.Model):
    """
    Model representing a choice.
    """
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    text = models.CharField(max_length=200, verbose_name='choice')
    vote = models.IntegerField(default=0)

    def __str__(self):
        """
        String for representring the Model object.
        """
        return self.text

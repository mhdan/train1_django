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

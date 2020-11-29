from django.db import models

class Journal(models.Model):
    upsetting_event = models.CharField(max_length=200)
    create_date = models.DateTimeField('date created')

class Emotion(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    SAD = "sad"
    ANXIOUS = "anxious"
    GUILTY = "guilty"
    INFERIOR = "inferior"
    LONELY = "lonely"
    EMBARRASSED = "embarrassed"
    HOPELESS = "hopeless"
    FRUSTRATED = "frustrated"
    ANGRY = "angry"
    OTHER = "other"
    emotion_choices = [
        (SAD,"Sad, blue, depressed, down, unhappy"),
        (ANXIOUS,"Anxious, worried, panicky, nervous, frightened"),
        (GUILTY,"Guilty, remorseful, bad, ashamed"),
        (INFERIOR,"Inferior, worthless, inadequate, defective, incompetent"),
        (LONELY,"Lonely, unloved, unwanted, rejected, alone, abandoned"),
        (EMBARRASSED,"Embarrassed, foolish, humiliated, self-conscious"),
        (HOPELESS,"Hopeless, discouraged, pessimistic, despairing"),
        (FRUSTRATED,"Frustrated, stuck, thwarted, defeated"),
        (ANGRY,"Angry, mad, resentful, annoyed, irritated, upset, furious"),
        (OTHER,"Other, specify an unlisted emotion")
    ]
    emotion = models.CharField(
        max_length=20,
        choices=emotion_choices,
        default=SAD
    )
    other_text = models.CharField(max_length=100,blank=True)
    now_percent = models.DecimalField(default=0.00,max_digits=5,decimal_places=2)
    goal_percent = models.DecimalField(default=0.00,max_digits=5,decimal_places=2)
    after_percent = models.DecimalField(default=0.00,max_digits=5,decimal_places=2)

class Distortion(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Thought(models.Model):        
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    negative_thoughts = models.CharField(max_length=200)
    positive_thoughts = models.CharField(max_length=200)
    distortions = models.ManyToManyField(Distortion)
    now_percent = models.DecimalField(default=0.00,max_digits=5,decimal_places=2)
    after_percent = models.DecimalField(default=0.00,max_digits=5,decimal_places=2)
    belief_percent = models.DecimalField(default=0.00,max_digits=5,decimal_places=2)

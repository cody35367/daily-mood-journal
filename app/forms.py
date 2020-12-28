from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.forms import CheckboxSelectMultiple,Textarea

from .models import Journal,Emotion,Thought,Distortion

class JournalForm(ModelForm):
    class Meta:
        model = Journal
        fields = ['upsetting_event']

def getEmotionFormSet(extras):
    return inlineformset_factory(
                    Journal,
                    Emotion,
                    extra=extras,
                    fields=[
                        'emotion',
                        'other_text',
                        'now_percent',
                        'goal_percent',
                        'after_percent'
                    ])

def getThoughtFormSet(extras):
    return inlineformset_factory(
                    Journal,
                    Thought,
                    extra=extras,
                    widgets={
                        'distortions' : CheckboxSelectMultiple(),
                        'negative_thoughts' : Textarea(),
                        'positive_thoughts': Textarea()
                    },
                    fields=[
                        'negative_thoughts',
                        'now_percent',
                        'after_percent',
                        'distortions',
                        'positive_thoughts',
                        'belief_percent'
                    ])

from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.forms import CheckboxSelectMultiple,Textarea

from .models import Journal,Emotion,Thought,Distortion

class JournalForm(ModelForm):
    class Meta:
        model = Journal
        fields = ['upsetting_event']

EmotionFormSet = inlineformset_factory(
                    Journal,
                    Emotion,
                    extra=0,
                    fields=[
                        'emotion',
                        'other_text',
                        'now_percent',
                        'goal_percent',
                        'after_percent'
                    ])
ThoughtFormSet = inlineformset_factory(
                    Journal,
                    Thought,
                    extra=0,
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

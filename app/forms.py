from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import Journal,Emotion,Thought,Distortion

class JournalForm(ModelForm):
    class Meta:
        model = Journal
        fields = ['upsetting_event','create_date']

EmotionFormSet = inlineformset_factory(
                    Journal,
                    Emotion,
                    extra=1,
                    fields=['emotion',
                            'other_text',
                            'now_percent',
                            'goal_percent',
                            'after_percent'
                    ])
ThoughtFormSet = inlineformset_factory(
                    Journal,
                    Thought,
                    extra=1,
                    fields=['negative_thoughts',
                            'now_percent',
                            'after_percent',
                            'distortions',
                            'positive_thoughts',
                            'belief_percent'
                    ])

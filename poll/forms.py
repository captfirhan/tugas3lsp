from django import forms
from .models import PollModel

class PollForm(forms.ModelForm):
	class Meta:
		model=PollModel
		fields=['question','option1','option2','option3']

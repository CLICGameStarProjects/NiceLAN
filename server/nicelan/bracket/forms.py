from django.forms import ModelForm, widgets


from .models import Bracket, FFABracket


class BracketForm(ModelForm):
    class Meta:
        model = Bracket
        exclude = []
        fields = [
            "name",
            "category",
            "start_date",
            "start_time",
            "end_date",
            "end_time",
            "description",
        ]
        widgets = {
            "start_date": widgets.DateInput(attrs={"type": "date"}),
            "start_time": widgets.TimeInput(attrs={"type": "time"}),
            "end_date": widgets.DateInput(attrs={"type": "date"}),
            "end_time": widgets.TimeInput(attrs={"type": "time"}),
        }


class FFABracket(BracketForm):
    class Meta(BracketForm.Meta):
        model = FFABracket
        exclude = BracketForm.Meta.exclude + []
        fields = BracketForm.Meta.fields + ["points_min"]
        widgets = BracketForm.Meta.widgets

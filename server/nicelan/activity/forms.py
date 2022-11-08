from django.forms import ModelForm, widgets


from .models import Activity, Animation, Other, Tournament


class ActivityForm(ModelForm):
    class Meta:
        model = Activity
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


class TournamentForm(ActivityForm):
    class Meta(ActivityForm.Meta):
        model = Tournament
        exclude = ActivityForm.Meta.exclude + []
        fields = ActivityForm.Meta.fields + ["points_min"]
        widgets = ActivityForm.Meta.widgets


class AnimationForm(ActivityForm):
    class Meta(ActivityForm.Meta):
        model = Animation
        exclude = ActivityForm.Meta.exclude + []
        fields = ActivityForm.Meta.fields + ["possible_points"]
        widgets = ActivityForm.Meta.widgets


class OtherForm(ActivityForm):
    class Meta(ActivityForm.Meta):
        model = Other
        exclude = ActivityForm.Meta.exclude + []
        fields = ActivityForm.Meta.fields + []
        widgets = ActivityForm.Meta.widgets

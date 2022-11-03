from django.forms import ModelForm, widgets


from .models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ["name", "start_date", "start_time", "end_date", "end_time", "description"]
        widgets = {
            "start_date": widgets.DateInput(attrs={"type": "date"}),
            "start_time": widgets.TimeInput(attrs={"type": "time"}),
            "end_date": widgets.DateInput(attrs={"type": "date"}),
            "end_time": widgets.TimeInput(attrs={"type": "time"}),
        }

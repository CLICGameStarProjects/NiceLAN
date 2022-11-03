# Generated by Django 4.1.2 on 2022-11-02 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("event", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Activity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                (
                    "category",
                    models.CharField(choices=[("OTHER", "Other")], default="OTHER", max_length=8),
                ),
                ("start", models.DateTimeField()),
                ("end", models.DateTimeField()),
                ("place", models.CharField(max_length=64)),
                ("team", models.BooleanField(default=False)),
                ("description", models.CharField(max_length=1024)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="event.event"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Animation",
            fields=[
                (
                    "activity_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="activity.activity",
                    ),
                ),
                ("possible_points", models.IntegerField(default=0)),
            ],
            bases=("activity.activity",),
        ),
        migrations.CreateModel(
            name="Other",
            fields=[
                (
                    "activity_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="activity.activity",
                    ),
                ),
            ],
            bases=("activity.activity",),
        ),
        migrations.CreateModel(
            name="Tournament",
            fields=[
                (
                    "activity_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="activity.activity",
                    ),
                ),
                ("points_min", models.IntegerField(default=0)),
            ],
            bases=("activity.activity",),
        ),
    ]

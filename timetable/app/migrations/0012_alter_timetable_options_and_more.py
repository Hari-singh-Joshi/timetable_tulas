# Generated by Django 5.1.2 on 2024-11-08 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0011_alter_timetable_sessiontype"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="timetable",
            options={"ordering": ["Day", "Timestart"]},
        ),
        migrations.AddConstraint(
            model_name="timetable",
            constraint=models.UniqueConstraint(
                fields=("Teacher", "Venue", "Timestart", "Day", "Section"),
                name="unique_teacher_venue_timestart_day_section",
            ),
        ),
        migrations.AddConstraint(
            model_name="timetable",
            constraint=models.UniqueConstraint(
                fields=("Teacher", "Timestart", "Day"),
                name="unique_teacher_timestart_day",
            ),
        ),
        migrations.AddConstraint(
            model_name="timetable",
            constraint=models.UniqueConstraint(
                fields=("Venue", "Timestart", "Day"), name="unique_venue_timestart_day"
            ),
        ),
        migrations.AddConstraint(
            model_name="timetable",
            constraint=models.UniqueConstraint(
                fields=("Section", "Timestart", "Day"),
                name="unique_section_timestart_day",
            ),
        ),
    ]

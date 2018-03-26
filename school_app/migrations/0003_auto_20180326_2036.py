# Generated by Django 2.0.3 on 2018-03-26 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0002_auto_20180326_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='student_reference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school_app.Student', unique=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='subject_reference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school_app.Subject', unique=True),
        ),
    ]
# Generated by Django 3.0.14 on 2022-02-12 21:19

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('home', '0009_auto_20220212_2043'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Documents',
        ),
        migrations.RenameField(
            model_name='collaboration',
            old_name='link',
            new_name='image_link',
        ),
        migrations.RenameField(
            model_name='startup_initiative',
            old_name='link',
            new_name='document_link',
        ),
        migrations.RemoveField(
            model_name='collaboration',
            name='image',
        ),
        migrations.RemoveField(
            model_name='internships',
            name='image',
        ),
        migrations.RemoveField(
            model_name='people',
            name='image',
        ),
        migrations.RemoveField(
            model_name='startup_initiative',
            name='image',
        ),
        migrations.AddField(
            model_name='collaboration',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='internships',
            name='image_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='people',
            name='image_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='startup_initiative',
            name='image_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='startup_initiative',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]

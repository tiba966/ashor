# Generated by Django 4.0.4 on 2023-06-17 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_about_remove_goals_goal_num_ar_alter_goals_goal_desc_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goals',
            name='image_banner_goals',
        ),
    ]

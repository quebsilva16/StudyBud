# Generated by Django 4.0.3 on 2022-03-08 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='descripcion',
            new_name='description',
        ),
    ]

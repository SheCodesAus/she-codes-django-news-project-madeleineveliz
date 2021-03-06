# Generated by Django 4.0.1 on 2022-02-20 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_newsstory_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsstory',
            options={'ordering': ['-pub_date']},
        ),
        migrations.AddField(
            model_name='newsstory',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
        migrations.AddField(
            model_name='newsstory',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

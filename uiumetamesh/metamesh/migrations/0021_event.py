# Generated by Django 4.2.1 on 2023-08-11 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metamesh', '0020_clubpost_cimage_clubs_imagee_posts_pictures_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(null=True, upload_to='banner')),
                ('name', models.CharField(max_length=100)),
                ('cat', models.CharField(max_length=100)),
                ('stime', models.CharField(max_length=20)),
                ('etime', models.CharField(max_length=30)),
                ('details', models.CharField(max_length=400)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metamesh.students')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metamesh.clubs')),
            ],
            options={
                'db_table': 'event',
            },
        ),
    ]
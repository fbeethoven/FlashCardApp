# Generated by Django 3.2.4 on 2021-06-25 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='deck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deck', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='flashCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('question', models.CharField(max_length=200)),
                ('answer', models.TextField()),
                ('deck', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flashCard', to='main.deck')),
            ],
        ),
    ]

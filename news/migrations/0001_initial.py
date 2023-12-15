# Generated by Django 4.1.6 on 2023-08-27 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='Default author', max_length=255, verbose_name='author')),
                ('post_type', models.CharField(choices=[('NE', 'Новость'), ('AR', 'Статья')], default='AR', max_length=2, verbose_name='Вид поста')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='дата и время изменения')),
                ('title', models.CharField(default='Default title', max_length=255, verbose_name='заголовок')),
                ('content', models.TextField(default='Default content', verbose_name='текст')),
            ],
        ),
    ]
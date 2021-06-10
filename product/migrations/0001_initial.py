# Generated by Django 3.1.7 on 2021-05-23 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, null=True)),
                ('price', models.FloatField()),
                ('special_note', models.CharField(blank=True, max_length=256, null=True)),
                ('specifications', models.CharField(max_length=512, null=True)),
                ('description', models.CharField(max_length=512, null=True)),
                ('in_stock', models.BooleanField(default=True, null=True)),
            ],
        ),
    ]
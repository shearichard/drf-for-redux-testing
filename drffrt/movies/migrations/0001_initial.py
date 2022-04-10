# Generated by Django 4.0.3 on 2022-04-10 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.CharField(max_length=100)),
                ('year', models.SmallIntegerField()),
                ('audience_score_percent', models.DecimalField(blank=True, decimal_places=2, max_digits=4)),
                ('genre', models.CharField(blank=True, max_length=100)),
                ('lead_studio', models.CharField(blank=True, max_length=100)),
                ('profitability', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('rotten_tomatoes_percent', models.DecimalField(blank=True, decimal_places=2, max_digits=4)),
                ('worldwide_gross_usd', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
            ],
            options={
                'ordering': ['film', 'year'],
            },
        ),
    ]

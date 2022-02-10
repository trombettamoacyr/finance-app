# Generated by Django 4.0.2 on 2022-02-10 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=200)),
                ('value', models.DecimalField(decimal_places=2, max_digits=7)),
                ('notes', models.TextField(blank=True, max_length=500)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.category')),
            ],
        ),
    ]
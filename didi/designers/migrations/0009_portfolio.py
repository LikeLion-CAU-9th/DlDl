# Generated by Django 3.2.4 on 2021-06-30 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('designers', '0008_delete_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('representation', models.CharField(choices=[('0', 'μλΈ'), ('1', 'λν')], max_length=1)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('comment', models.TextField()),
                ('designer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='portfolio', to='designers.designer_info')),
            ],
        ),
    ]

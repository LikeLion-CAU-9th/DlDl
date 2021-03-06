# Generated by Django 3.2.4 on 2021-06-28 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Designer_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_image', models.ImageField(upload_to='uploads/')),
                ('personerity_pick_1', models.CharField(choices=[('1', '시간 엄수'), ('2', '소통'), ('3', '친화력'), ('4', '협업'), ('5', '아이디어'), ('6', '기획'), ('7', '노력'), ('8', '인내'), ('9', '열정')], max_length=1)),
                ('personerity_pick_2', models.CharField(choices=[('1', '시간 엄수'), ('2', '소통'), ('3', '친화력'), ('4', '협업'), ('5', '아이디어'), ('6', '기획'), ('7', '노력'), ('8', '인내'), ('9', '열정')], max_length=1)),
                ('personerity_pick_3', models.CharField(choices=[('1', '시간 엄수'), ('2', '소통'), ('3', '친화력'), ('4', '협업'), ('5', '아이디어'), ('6', '기획'), ('7', '노력'), ('8', '인내'), ('9', '열정')], max_length=1)),
                ('intruduce', models.TextField()),
            ],
        ),
    ]

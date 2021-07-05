# Generated by Django 3.2.4 on 2021-07-05 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fcuser', '0005_fcuser_useremail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='제목')),
                ('contents', models.TextField(verbose_name='내용')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('wirter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fcuser.fcuser', verbose_name='작성자')),
            ],
            options={
                'verbose_name_plural': '게시글',
                'db_table': 'fastcampus_board',
            },
        ),
    ]

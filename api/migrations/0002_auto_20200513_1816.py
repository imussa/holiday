# Generated by Django 3.0.6 on 2020-05-13 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_type',
            field=models.IntegerField(choices=[(1, '普通用户'), (2, '管理员')], default=1),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='usertoken',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='token', to='api.UserInfo'),
        ),
        migrations.CreateModel(
            name='Translates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translate', models.CharField(max_length=128)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translates', to='api.Words')),
            ],
        ),
    ]

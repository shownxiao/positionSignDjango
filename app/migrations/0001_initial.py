# Generated by Django 2.1.5 on 2019-09-09 20:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='参加时间')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255, verbose_name='留言内容')),
                ('time', models.DateTimeField(verbose_name='留言时间')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='地点名')),
                ('longitude', models.FloatField(verbose_name='经度')),
                ('latitude', models.FloatField(verbose_name='纬度')),
                ('score', models.IntegerField(verbose_name='初始分值')),
                ('radius', models.IntegerField(verbose_name='打卡半径')),
                ('introduction', models.CharField(max_length=500, verbose_name='介绍文案')),
                ('image', models.CharField(max_length=100, verbose_name='图片')),
                ('is_used', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_signed', models.BooleanField(verbose_name='是否签到成功')),
                ('score', models.FloatField(verbose_name='分值')),
                ('time', models.DateTimeField(verbose_name='签到时间')),
                ('created_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='record', to='app.Position', verbose_name='签到地点')),
            ],
        ),
        migrations.CreateModel(
            name='Transcript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='副本名')),
                ('introduction', models.CharField(max_length=200, verbose_name='副本介绍')),
                ('start_time', models.DateTimeField(verbose_name='副本开始时间')),
                ('end_time', models.DateTimeField(verbose_name='副本结束时间')),
                ('number', models.IntegerField(default=0, verbose_name='参与人数')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=50, verbose_name='openid')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('std_id', models.CharField(max_length=20, verbose_name='学号')),
                ('sex', models.CharField(max_length=4, verbose_name='性别')),
                ('wx_nickname', models.CharField(max_length=20, verbose_name='微信昵称')),
                ('wx_avatar', models.CharField(max_length=100, verbose_name='头像链接')),
                ('phone', models.CharField(max_length=20, verbose_name='电话')),
                ('academy', models.CharField(max_length=10, verbose_name='学院')),
                ('major', models.CharField(max_length=10, verbose_name='专业')),
                ('class_s', models.CharField(max_length=10, verbose_name='班级')),
                ('last_login', models.DateField(default=datetime.datetime(2019, 9, 9, 20, 15, 42, 232546), null=True)),
                ('createTime', models.DateField(null=True)),
                ('is_bind', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='record',
            name='transcript',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='record', to='app.Transcript', verbose_name='所属副本'),
        ),
        migrations.AddField(
            model_name='record',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='record', to='app.User', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='position',
            name='transcript',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='position', to='app.Transcript', verbose_name='所属副本'),
        ),
        migrations.AddField(
            model_name='message',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='message', to='app.Position', verbose_name='地点'),
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to='app.User', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='join',
            name='transcript',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='join', to='app.Transcript', verbose_name='活动'),
        ),
        migrations.AddField(
            model_name='join',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='join', to='app.User', verbose_name='用户'),
        ),
    ]

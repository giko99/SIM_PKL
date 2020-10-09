# Generated by Django 2.2 on 2020-10-09 03:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mitra', '0002_auto_20200924_0259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waktu', models.DateTimeField(default=datetime.datetime.now)),
                ('desc', models.TextField()),
                ('mahasiswa', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mahasiswas', to=settings.AUTH_USER_MODEL)),
                ('nama_mitra', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mitra.Mitra')),
            ],
        ),
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waktu', models.DateTimeField(default=datetime.datetime.now)),
                ('desc', models.TextField()),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='posting', to='forum.Forum')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Komen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waktu', models.DateTimeField(default=datetime.datetime.now)),
                ('desc', models.TextField()),
                ('pengguna', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='pengguna', to=settings.AUTH_USER_MODEL)),
                ('posting', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='komentar', to='forum.Posting')),
            ],
        ),
        migrations.CreateModel(
            name='Balas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waktu', models.DateTimeField(default=datetime.datetime.now)),
                ('desc', models.TextField()),
                ('komen', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='balasan', to='forum.Komen')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

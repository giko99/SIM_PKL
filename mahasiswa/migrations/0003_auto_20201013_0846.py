# Generated by Django 2.2 on 2020-10-13 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mahasiswa', '0002_auto_20201001_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pkl',
            name='nama_mitra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='forum.Forum'),
        ),
    ]

# Generated by Django 3.2.13 on 2022-05-04 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehiclechecklist',
            old_name='truck',
            new_name='vehicle',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('DR', 'Driver'), ('SP', 'Supervisor')], default='DR', max_length=2),
        ),
        migrations.AddField(
            model_name='user',
            name='vehicle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.vehicle'),
        ),
    ]

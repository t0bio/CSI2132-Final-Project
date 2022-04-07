# Generated by Django 4.0.3 on 2022-04-06 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='employee_id',
            new_name='employee',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='patient_id',
            new_name='patient',
        ),
        migrations.RenameField(
            model_name='appointment_procedure',
            old_name='appointment_id',
            new_name='appointment',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
# Generated by Django 4.0 on 2021-12-23 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0007_alter_salary_conveyance_allowance_alter_salary_hra_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary',
            name='conveyance_allowance',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='salary',
            name='hra',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='salary',
            name='medical_allowance',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='salary',
            name='others',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='salary',
            name='performance_bonus',
            field=models.FloatField(blank=True, default=0),
        ),
    ]

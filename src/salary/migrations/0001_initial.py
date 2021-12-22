# Generated by Django 4.0 on 2021-12-22 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dno', models.IntegerField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=20)),
                ('dept_date', models.DateField()),
                ('mgrid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('slipno', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('basic_salary', models.FloatField()),
                ('hra', models.FloatField()),
                ('conveyance_allowance', models.FloatField()),
                ('medical_allowance', models.FloatField()),
                ('performance_bonus', models.FloatField()),
                ('others', models.FloatField()),
                ('sdate', models.DateField()),
                ('dno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salary.department')),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Deduction',
            fields=[
                ('dedid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('ded_date', models.DateField()),
                ('dcategory', models.CharField(choices=[('P', 'Pension'), ('L', 'Loans')], max_length=1)),
                ('damt', models.FloatField()),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]

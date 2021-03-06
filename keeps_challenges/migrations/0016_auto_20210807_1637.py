# Generated by Django 3.2.6 on 2021-08-07 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('keeps_challenges', '0015_auto_20210807_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='keeps_challenges.course'),
            preserve_default=False,
        ),
    ]

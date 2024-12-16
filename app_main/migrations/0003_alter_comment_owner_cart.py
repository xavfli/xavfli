# Generated by Django 5.1.1 on 2024-10-04 15:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0002_initial'),
        ('app_users', '0002_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_users.customer'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_main.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_users.customer')),
            ],
            options={
                'unique_together': {('product_id', 'user_id')},
            },
        ),
    ]

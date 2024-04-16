# Generated by Django 5.0.1 on 2024-04-16 12:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_post_is_available_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('is_paid', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PostThatBuy', to='account.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserThatBuy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

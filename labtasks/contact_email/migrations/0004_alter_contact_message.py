# Generated by Django 4.1.7 on 2023-03-17 19:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contact_email", "0003_alter_contact_message"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="message",
            field=models.CharField(max_length=2000),
        ),
    ]
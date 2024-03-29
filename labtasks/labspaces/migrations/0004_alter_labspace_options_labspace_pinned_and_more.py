# Generated by Django 4.1.7 on 2023-04-18 18:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("labspaces", "0003_labspace_host_message"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="labspace",
            options={"ordering": ["updated", "created"]},
        ),
        migrations.AddField(
            model_name="labspace",
            name="pinned",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="labspace",
            name="description",
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="labspace",
            name="name",
            field=models.CharField(max_length=50),
        ),
    ]

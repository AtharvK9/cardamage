# Generated by Django 4.2.10 on 2024-03-02 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PicUpload",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("imagefile", models.ImageField(blank=True, upload_to="pic_upload")),
            ],
        ),
    ]
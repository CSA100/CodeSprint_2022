# Generated by Django 4.1.1 on 2022-10-02 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Homepage", "0003_verifiedjoblisting_hash"),
    ]

    operations = [
        migrations.CreateModel(
            name="CoLoadingListing",
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
                ("Date", models.DateField()),
                ("Time", models.TimeField()),
                ("Destination", models.CharField(max_length=200)),
                ("AvailableVolume", models.IntegerField()),
                ("AvailableWeight", models.IntegerField()),
                ("RequiredVolume", models.IntegerField()),
                ("RequiredWeight", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="VerifiedCoLoadingListing",
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
                ("Date", models.DateField()),
                ("Time", models.TimeField()),
                ("Destination", models.CharField(max_length=200)),
                ("AvailableVolume", models.IntegerField()),
                ("AvailableWeight", models.IntegerField()),
                ("RequiredVolume", models.IntegerField()),
                ("RequiredWeight", models.IntegerField()),
            ],
        ),
    ]

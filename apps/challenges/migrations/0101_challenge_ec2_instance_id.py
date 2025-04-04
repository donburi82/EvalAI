# Generated by Django 2.2.20 on 2023-08-10 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("challenges", "0100_challenge_uses_ec2_worker"),
    ]

    operations = [
        migrations.AddField(
            model_name="challenge",
            name="ec2_instance_id",
            field=models.CharField(
                blank=True, default="", max_length=200, null=True
            ),
        ),
        migrations.AlterField(
            model_name="challenge",
            name="uses_ec2_worker",
            field=models.BooleanField(
                db_index=True,
                default=False,
                verbose_name="Uses EC2 worker instance",
            ),
        ),
    ]

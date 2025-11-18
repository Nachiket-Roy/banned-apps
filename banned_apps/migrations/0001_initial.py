import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BannedApp",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("country_name", models.CharField(max_length=100)),
                ("country_code", models.CharField(max_length=2)),
                ("app_name", models.CharField(max_length=100)),
                (
                    "app_type",
                    models.CharField(
                        choices=[
                            ("social", "Social Media"),
                            ("messaging", "Messaging"),
                            ("gaming", "Gaming"),
                            ("streaming", "Streaming"),
                            ("other", "Other"),
                        ],
                        max_length=20,
                    ),
                ),
                ("ban_reason", models.TextField()),
                ("ban_date", models.DateField(default=django.utils.timezone.now)),
                ("source_url", models.URLField(blank=True)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Banned App",
                "verbose_name_plural": "Banned Apps",
                "ordering": ["country_name", "app_name"],
            },
        ),
        migrations.AddIndex(
            model_name="bannedapp",
            index=models.Index(fields=["country_name"], name="bannedapp_country_name_idx"),
        ),
        migrations.AddIndex(
            model_name="bannedapp",
            index=models.Index(fields=["country_code"], name="bannedapp_country_code_idx"),
        ),
    ]

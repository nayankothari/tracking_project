# Generated by Django 4.1.3 on 2022-11-06 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "__first__"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UploadDrs",
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
                ("drs_no", models.BigIntegerField()),
                ("image", models.ImageField(upload_to="")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RouteMaster",
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
                ("area_name", models.CharField(max_length=250)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "pincode",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.pincode",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"verbose_name_plural": "Route Master",},
        ),
        migrations.CreateModel(
            name="PaymentMaster",
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
                ("payment_type", models.CharField(max_length=250)),
                ("opening_balance", models.FloatField()),
                ("status", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"verbose_name_plural": "Payment Master",},
        ),
        migrations.CreateModel(
            name="PartyMaster",
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
                ("party_name", models.CharField(max_length=256)),
                ("in_person_name", models.CharField(max_length=256)),
                ("mobile_number", models.BigIntegerField()),
                ("alternate_numnber", models.BigIntegerField(blank=True)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("username", models.CharField(max_length=16, unique=True)),
                ("password", models.CharField(max_length=30)),
                ("party_address", models.TextField(blank=True)),
                ("is_gst_enabled_party", models.BooleanField(default=False)),
                ("gst_number", models.CharField(blank=True, max_length=15)),
                ("remarks", models.TextField(blank=True)),
                ("opening_balance", models.FloatField()),
                ("status", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"verbose_name_plural": "Party Master",},
        ),
        migrations.CreateModel(
            name="LoadOutWard",
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
                ("lot_no", models.BigIntegerField()),
                ("from_destination", models.CharField(max_length=256)),
                ("to_destination", models.CharField(max_length=256)),
                ("additional_mainifest_no", models.CharField(max_length=30)),
                ("c_note_number", models.BigIntegerField()),
                ("document_destination", models.CharField(max_length=30)),
                ("consignee_name", models.CharField(max_length=256)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "from_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"verbose_name_plural": "Load Outward",},
        ),
        migrations.CreateModel(
            name="LoadInWard",
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
                ("c_note_number", models.BigIntegerField()),
                ("consignee_name", models.CharField(max_length=256)),
                ("document_destination", models.CharField(max_length=30)),
                ("additional_mainifest_no", models.CharField(max_length=30)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "from_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "received_by_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_by_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"verbose_name_plural": "Load Inward",},
        ),
        migrations.CreateModel(
            name="DeliveryBoy",
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
                ("delivery_boy_name", models.CharField(max_length=120)),
                ("mobile_number", models.BigIntegerField()),
                ("alternate_number", models.CharField(blank=True, max_length=15)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("address", models.TextField()),
                ("status", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "area_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="operations.routemaster",
                    ),
                ),
                (
                    "pincode",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.pincode",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"verbose_name_plural": "Delivery Boy Master",},
        ),
        migrations.CreateModel(
            name="Booking",
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
                ("reference_courier_number", models.CharField(max_length=25)),
                ("payment_mode", models.CharField(max_length=30)),
                ("booking_datetime", models.DateTimeField()),
                ("consignor_mobile_number", models.BigIntegerField()),
                ("consignor_address", models.TextField()),
                ("consignor_gst_number", models.CharField(max_length=16)),
                ("consignee_name", models.CharField(max_length=250)),
                ("consignee_mobile_number", models.BigIntegerField()),
                ("consignee_address", models.TextField()),
                ("consignee_gst_number", models.CharField(max_length=16)),
                ("area_name", models.CharField(max_length=256)),
                ("weight_in_gms", models.FloatField()),
                ("charge_weight", models.FloatField()),
                ("declare_value", models.FloatField()),
                ("risk_coverage_charges", models.FloatField()),
                ("apply_gst", models.BooleanField(default=False)),
                ("tax_percentage", models.FloatField()),
                ("tax_amount", models.FloatField()),
                ("hsn_number", models.CharField(max_length=15)),
                ("courier_charges", models.FloatField()),
                ("fuel_charges", models.FloatField()),
                ("insurance_charges", models.FloatField()),
                ("other_charges", models.FloatField()),
                ("to_pay", models.BooleanField(default=False)),
                ("to_pay_amount", models.FloatField()),
                ("booking_last_status", models.CharField(max_length=256)),
                ("remarks", models.TextField()),
                ("status", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "booking_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.bookingtype",
                    ),
                ),
                (
                    "c_note_number",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.cnotehistory",
                    ),
                ),
                (
                    "consignor_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="operations.partymaster",
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.country",
                    ),
                ),
                (
                    "pincode",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.pincode",
                    ),
                ),
                (
                    "refernce_courier_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.refrencecourier",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"verbose_name_plural": "Booking Master",},
        ),
    ]

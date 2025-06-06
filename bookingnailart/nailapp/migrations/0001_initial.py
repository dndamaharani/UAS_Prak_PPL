# Generated by Django 5.2 on 2025-05-30 06:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Layanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('harga', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deskripsi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pelanggan', models.CharField(max_length=100)),
                ('tanggal', models.DateField()),
                ('catatan', models.TextField(blank=True)),
                ('layanan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nailapp.layanan')),
            ],
        ),
    ]

from django.contrib import admin
from .models import Layanan, Booking

admin.site.register(Layanan)
admin.site.register(Booking)
admin.site.site_header = "💅 Nail Art Admin"
admin.site.site_title = "Booking Nail Art Admin"
admin.site.index_title = "Selamat Datang di Dashboard Admin 💖"
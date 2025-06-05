from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['nama_pelanggan', 'tanggal', 'layanan', 'catatan']

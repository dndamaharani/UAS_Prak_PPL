from django.shortcuts import render
from .forms import BookingForm
from .models import Layanan

def index(request):
    """
    View utama yang menampilkan form booking dan daftar layanan.
    """
    success = False
    error = False  # tambahkan flag untuk error

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = BookingForm()  # reset form setelah submit sukses
        else:
            error = True  # form tidak valid
    else:
        form = BookingForm()

    layanan_list = Layanan.objects.all()

    return render(request, 'index.html', {
        'form': form,
        'success': success,
        'error': error,
        'layanan_list': layanan_list
    })

def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'booking_form.html', {'form': BookingForm(), 'success': True, 'layanan_list': Layanan.objects.all()})
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form, 'layanan_list': Layanan.objects.all()})

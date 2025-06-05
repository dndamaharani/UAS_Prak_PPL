from django.db import models

class Layanan(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name = "Layanan"
        verbose_name_plural = "Layanan"

class Booking(models.Model):
    nama_pelanggan = models.CharField(max_length=100)
    tanggal = models.DateField()
    layanan = models.ForeignKey(Layanan, on_delete=models.CASCADE)
    catatan = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nama_pelanggan} - {self.tanggal}"

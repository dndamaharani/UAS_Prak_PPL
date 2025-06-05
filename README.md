
# 💅 Aplikasi Web Booking Nail Art

Aplikasi web untuk sistem pemesanan layanan **nail art**, dikembangkan menggunakan **Django**. Aplikasi ini memudahkan pelanggan dalam melakukan booking secara online dan membantu penyedia layanan dalam mengelola jadwal serta data pelanggan dengan lebih efisien.

---

## 📌 Fitur Utama

- Formulir pemesanan layanan nail art secara online
- Dashboard admin untuk mengelola booking dan layanan
- Antarmuka pengguna berbasis template Django
- Penyimpanan data menggunakan database SQLite
- Sistem autentikasi pengguna dan admin
- Halaman konfirmasi booking
- Dukungan tampilan responsif (dasar)

---

## 🗂️ Struktur Folder

```
bookingnailart/
├── bookingnailart/        # Konfigurasi utama proyek Django
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── nailapp/               # Aplikasi inti
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│   ├── migrations/
├── static/                # File statis (CSS, JS, gambar)
├── db.sqlite3             # Database SQLite
├── manage.py              # Skrip manajemen Django
```

---

## ⚙️ Cara Menjalankan Proyek

1. **Clone repository (jika sudah berada dalam repositori):**

   ```bash
   git clone <url-repository>
   cd bookingnailart
   ```

2. **Aktifkan virtual environment (opsional):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Di Windows: venv\Scripts\activate
   ```

3. **Install dependensi yang dibutuhkan:**

   ```bash
   pip install django
   ```

4. **Jalankan migrasi database:**

   ```bash
   python manage.py migrate
   ```

5. **Jalankan server lokal:**

   ```bash
   python manage.py runserver
   ```

6. **Buka aplikasi di browser:**  
   `http://127.0.0.1:8000/`

---

## 🔐 Akses Admin

Untuk membuat superuser/admin:

```bash
python manage.py createsuperuser
```

Login admin dapat diakses di:  
`http://127.0.0.1:8000/admin/`

---

## 📃 Lisensi

Proyek ini dikembangkan untuk keperluan pembelajaran dan tugas akademik. Hak cipta dimiliki oleh pengembang terkait.

---

## ✍️ Pengembang

- Proyek Akhir – Praktikum PPL
- Dikembangkan oleh: **[Nama Anda / Tim Anda]**

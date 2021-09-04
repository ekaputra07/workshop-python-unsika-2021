# Workshop Python UNSIKA 2021

![cover](https://github.com/ekaputra07/workshop-python-unsika-2021/raw/main/screenshots/cover.png)

Materi workshop "Light up your Python!" **Himpunan Mahasiswa Sistem Informasi Fakultas Ilmu Komputer Universitas Singaperbangsa Karawang**, 4 September 2021 (Online via Zoom).

- [>> Video Workshop](https://youtu.be/MlSfwmCn49k)
- [>> Slides presentasi](https://docs.google.com/presentation/d/1kxU1M94zCGCGWMokkWkykZ7vQW9wFQkiMLliikV2ftM/edit?usp=sharing)

## Pendahuluan

<details>
  <summary><b>1. Tentang Eka Putra</b></summary>
  
  ![Eka Putra](https://github.com/ekaputra07/workshop-python-unsika-2021/raw/main/screenshots/ekaputra.png)
  
  [Eka Putra](https://github.com/ekaputra07) sudah berkecimpung di dunia pengembangan website sejak 2009, meskipun beberapa tahun sebelum itu dia sudah mempelajari programming walaupun sebatas hobi menggunakan bahasa pemrograman Pascal (Delphi).
  
  Pada awalnya dia mulai menjajakan jasa pembuatan website melalui website sederhana buatannya sendiri yang dibuat menggunakan WordPress, saat itu masih bekerja di sebuah perusahaan aksesoris sebagai desainer grafis. Klien pun mulai dia dapatkan sampai akhirnya dia memutuskan untuk terjun full-time menjadi freelance web developer.
  
  Pada tahun 2015 dia mendapatkan tawaran untuk bekerja di sebuah perusahaan berbasis di Australia, karena kebetulan sang pemilik juga tinggal di Bali. Dari tahun 2015 itu sampai 2018 (3 tahun) dia bekerja secara remote, dan pada akhir 2018 dia bisa berangkat ke Australia dengan sponsor perusahaan untuk bekerja di kantornya di Sydney. Saat inipun (September 2021) dia masih bekerja di perusahaan yang sama sebagai Senior Software Engineer (Data).
</details>

<details>
  <summary><b>2. Mengenal Python</b></summary>
  
  ![Tentang Python](https://github.com/ekaputra07/workshop-python-unsika-2021/raw/main/screenshots/tentang-python-1.png)
  
  [Python](https://www.python.org/) adalah sebuah bahasa pemrograman tingkat tinggi (high-level) dan multi guna. Tingkat tinggi yang dimaksud adalah dari cara kita berinteraksi dengan komputer menggunakan bahasa yang hampir mirip dengan bahasa manusia tanpa perlu mengerti dan memahami detail dari sistem operasi atau komputer itu sendiri. Berbeda dengan bahasa pemrograman tingkat rendah seperti Assembly atau C yang mana kita perlu memahami cara memanage memory dan sebagainya.
  
  Python diciptakan pada akhir tahun 1980-an oleh [Guido Van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum) seorang programmer dari Belanda. Python dirilis pertama kali pada tahun 1991, Python 2.0 dirilis pada tahun 2000 dan Python 3.0 dirilis pada tahun 2008. Saat ini buat teman-teman yang ingin belajar Python, saya sarankan langsung mulai dengan Python versi 3+.
  
  Karena populernya bahasa ini dan bisa digunakan untuk berbagai macam keperluan, kita akan sering melihat Python digunakan dalam web development, pembuatan API, program berbasis CLI, embedded system, scripting engine untuk game dan lain sebagainya.
  
  ![Survey Python](https://github.com/ekaputra07/workshop-python-unsika-2021/raw/main/screenshots/tentang-python-2.png)
  
  Berdasarkan survey yang dilakukkan oleh [Stack Overflow](https://insights.stackoverflow.com/survey/2021), Python berada di urutan nomer 3 dari teknologi atau bahasa pemrograman terpopuler di dunia dibawah Javascript dan HTML/CSS, dan merupakan bahasa pemrograman nomer 1 yang paling ingin dipelajari oleh orang yang belum pernah menggunakannya.
  
  ![Siapa memakai Python?](https://github.com/ekaputra07/workshop-python-unsika-2021/raw/main/screenshots/tentang-python-3.png)
  
  Karena bisa dibilang mudah dipelajari dan multiguna maka tidak hayal bahwa banyak perusahaan besar di dunia menggunakan Python di tech-stack mereka. Dan saya yakin begitu juga dengan perusahaan-perusahaan dan startup di Indonesia. Perusahaan-perusahan seperti Google, Instagram, Dropbox, Facebook dll. bisa dipastikan menggunakan Python di system mereka meskipun bukan cuma satu-satunya bahasa yang mereka gunakan.
  
</details>

<details>
  <summary><b>3. Instalasi Python</b></summary>
  
  > **Instalasi Python tidak diperagakan di workshop ini**, saya berasumsi bahwa peserta workshop sudah memiliki Python terinstall di komputer masing-masing dan siap digunakan.
  
  Untuk instalasi bisa mengikuti panduan dari website ini untuk Windows, Linux dan MacOS: https://realpython.com/installing-python/
  
</details>

<details>
  <summary><b>4. Menjalankan kode Python secara online</b></summary>
  
  Buat yang tidak memiliki Python di komputernya, peserta workshop juga bisa mengikuti program ini dengan menggunakan layanan online berikut ini:
  
  - [www.programiz.com](https://www.programiz.com/python-programming/online-compiler/)
  - [www.onlinegdb.com](https://www.onlinegdb.com/online_python_interpreter)
  - [www.online-python.com](https://www.online-python.com/)
  
</details>


## Python Dasar

<details>
  <summary><b>Contoh kode Python</b></summary>
  
  ![Contoh Kode Python](https://github.com/ekaputra07/workshop-python-unsika-2021/raw/main/screenshots/python-code.png)
  
  Kode diatas merupakan contoh sederhana kode Python, meskipun kode Python yang paling sederhana sebenarnya adalah `print('Hello World')` tetapi kode yang berguna tidak cukup hanya dengan satu perintah `print` saja.
  
  Pada screenshot diatas menunjukkan bagian-bagian dari kode Python yang lebih lengkap dengan rincian sebagai berikut:
  
  - `import` digunakan untuk meng-import modul, fungsi atau class dari sebuah package.
  - `def` digunakan untuk mendefinisikan sebuah fungsi.
  - `#` digunakan untuk memulai sebuah komentar pada kode
  - `"""` digunakan untuk memulai sebuah komentar yang memungkinan kita menulis komentar dengan baris lebih dari satu, sedangkan `#` untuk komentar satu baris.
  - Penamaan variable biasanya menggunkan hurup kecil dan menggunakan underscore sebagai pemisah kata satu dengan yang lainnya.
  
</details>

1. [Hello World](https://github.com/ekaputra07/workshop-python-unsika-2021/blob/main/1-python-dasar/1_hello_world.py)
1. [Variable dan Tipe Data](https://github.com/ekaputra07/workshop-python-unsika-2021/blob/main/1-python-dasar/2_variable_tipe_data.py)
1. [Percabangan](https://github.com/ekaputra07/workshop-python-unsika-2021/blob/main/1-python-dasar/3_percabangan.py)
1. [Perulangan](https://github.com/ekaputra07/workshop-python-unsika-2021/blob/main/1-python-dasar/4_perulangan.py)
1. [Fungsi](https://github.com/ekaputra07/workshop-python-unsika-2021/blob/main/1-python-dasar/5_fungsi.py)
1. [Pengenalan class](https://github.com/ekaputra07/workshop-python-unsika-2021/blob/main/1-python-dasar/6_class.py)
1. [Module di Python](https://github.com/ekaputra07/workshop-python-unsika-2021/blob/main/1-python-dasar/7_module.py)
1. [Penggunaan Library atau Package](https://github.com/ekaputra07/workshop-python-unsika-2021/blob/main/1-python-dasar/8_package.py)

## Website dan Flask

<details>
  <summary><b>1. Bagaimana Website Bekerja?</b></summary>
  
  ![Bagaimana Website Bekerja?](https://github.com/ekaputra07/workshop-python-unsika-2021/raw/main/screenshots/how-website-works.png)
  
  Kita bisa mengakses sebuah halaman di website karena ada beberapa elemen yang bekerja secara bersama-sama:
  
  - **Komputer yang terkoneksi ke internet** dan terdapat **aplikasi web browser** di dalamnya seperti Google Chrome atau Firefox.
  - **Jaringan internet** yang memungkinkan kita mengakses server yang ada di belahan dunia manapun.
  - **Webserver** yang merupakan server yang khusus untuk menerima request dari komputer kita dan mengembalikan dokumen (berupa halaman web) yang ingin kita akses.
  
  Ketiga elemen tersebut saling bekerja sama dan memiliki peran masing-masing mengantarkan data dari komputer kita ke web server dan sebaliknya juga dari web server ke komputer kita.
  
  Komputer kita dan web server berkomunikasi dengan sebuah protokol bernama HTTP (Hyper Text Transfer Protocol), dimana web browser membuat request dan web server akan memberikan respone.
  
  Web developer dipastikan akan bertemu dan bekerja dengan request dan response ini dalam karirnya, oleh karena itu memahami bagaimana memproses request dan memberikan response adalah skill dasar yang harus dimiliki oleh pengembang website terutama website yang sifatnya dinamis.
  
</details>

<details>
  <summary><b>2. Jenis dan Cara Membuat Website?</b></summary>
  
  ![Bagaimana Membuat Website?](https://github.com/ekaputra07/workshop-python-unsika-2021/raw/main/screenshots/membuat-website.png)
  
  Berdasarkan sifatnya, website bisa dikategorikan menjadi dua jenis:
  
  1. **Website Statis**, website jenis ini biasanya dibuat hanya dengan HTML/CSS dan Javascript (optional). Website statis biasanya memiliki halaman yang sudah jadi sebelum di-serve oleh web server. Untuk mengganti isi website maka harus dilakukkan perubahan secara manual dan kembali menguploadnya ke server. Website jenis ini cocok untuk website yang tidak akan terlalu banyak mengalamai perubahan, cocok untuk halaman dokumentasi, personal blog sederhana, ataupun company profile sederhana.
  2. **Website Dinamis**, ini mungkin jenis website yang paling sering kita temui saat ini, ciri-ciri website ini biasanya kaya akan fitur yang interaktif. Kita bisa berinteraksi dengan website, kita bisa meminta website untuk melakukkan sesuatu misalnya mengirim email, update status, upload file dan yang lainnya. Website ini meng-generate halaman ketika kita mengaksesnya dan sesuai dengan URL yang kita buka, itulah kenapa disebut website dinamis. Bisa dipastikan website-website ini menggunakan semacam database untuk menyimpan data dan menggunakan bahasa pemrograman tertentu untuk mengambil dan menampilkan datanya.
  
  Jadi berdasarkan jenis-jenis website tersebut, cara membuatnya pun bermacam-macam karena memang bisa dibuat dengan teknologi yang berbeda-beda misalnya yang paling umum adalah dengan bahasa PHP dipadukan dengan HTML/CSS/Javascript maka kita bisa membuat website yang menarik dan interaktif.
  
  Secara umum, website atau aplikasi berbasis website pasti akan memerlukan perpaduan antara HTML (struktur website), CSS (style/tampilan website), Javascript (interaksi dinamis), bahasa scripting atau pemrograman seperti PHP, Python, NodeJS dan banyak lagi yang bertugas memproses request, membaca database, merender template dan mengembalikan hasilnya berupa HTTP response ke browser.
  
  Dan beberapa tahun belakangan ini, semakin banyak framework pembuatan website bermunculan dari berbagai macam bahasa pemrograman seperti PHP dan Python, dan kali ini karena kita sedang membahas Python maka kita akan mencoba membuat sebuah aplikasi berbasis web sederhana menggunakan framework [Flask](https://flask.palletsprojects.com/en/2.0.x/) dimana kita akan coding menggunakan bahasa Python.
  
  > Untuk pembuatan aplikasi berbasis web saya sarankan menggunakan framework karena selain mempercepat proses pembuatan, maka hal yang paling penting yaitu faktor keamanan. Keamanan website merupakan urusan yang susah-susah gampang, pengembang framework biasanya sudah memperhatikan aspek keamanannya sebelum dipakai khalayak umum meskipun sebagai pengguna framework kita tetap harus berhati-hati dan selalu mengikuti tata cara yang baik pengembangan website untuk menjamin keamanannya.
  
</details>

<details>
  <summary><b>3. Flask Web Framework</b></summary>
  
  ![Flask Web Framework](https://github.com/ekaputra07/workshop-python-unsika-2021/raw/main/screenshots/flask.png)
  
  [Flask Web Framework](https://flask.palletsprojects.com/en/2.0.x/)
  
</details>

<details>
  <summary><b>4. Hello Flask</b></summary>
  
  ![Hello Flask](https://github.com/ekaputra07/workshop-python-unsika-2021/raw/main/screenshots/hello-flask.png)
  
  Kode diatas adalah sebuah aplikasi web sederhana menggunakan Flask, seperti terlihat bahwa aplikasi tersebut hanya memiliki dua buah URL yang bisa diakses yaitu `/` (menampilkan tulisan `Hello World`) dan `/unsika` (menampilkan tulisan `Terima kasih UNSIKA!`).
  
  Cara kerjanya pun disini sesuai dengan konsep Request dan Response, kita memberikan request ke URL `/` maka Flask merespon dengan tulisan `Hello World`, begitu juga ketika kita request URL `/unsika` maka Flask akan merespon dengan tulisan `Terima kasih UNSIKA!`.
  
</details>


## Membuat aplikasi todo list dengan Flask


![Apa yang akan kita pelajari](https://github.com/ekaputra07/workshop-python-unsika-2021/raw/main/screenshots/what-we-learn.png)

Seperti tujuan dari workshop kali ini yaitu untuk mengajak teman-teman developer yang belum pernah memakai Python untuk mencoba Python dan juga memperkenalkan bagaimana pembuatan aplikasi berbasis web bisa dilakukkan dengan Flask (salah satu web framework berbasis Python).

Saya tahu pasti bahwa buat teman-teman yang sama sekali belum pernah memakai Python dan langsung membuat aplikasi web sederhana pastinya tidak mudah, untuk itu saya merancang workshop ini dengan mempertimbangkan pengalaman peserta dimana buat yang belum pernah mencoba Python bisa mencobanya, dan buat yang sudah mengetahui dasarnya bisa mencoba Flask.

Aplikasi inipun saya rancang supaya kita bisa mempraktekkan ilmu-ilmu yang kita pelajari pada saat pengenalan Python dasar.

<details>
  <summary><b>1. Tampilan Aplikasi</b></summary>
  
  ![Tampilan Aplikasi Todolist dengan Flask](https://github.com/ekaputra07/workshop-python-unsika-2021/raw/main/screenshots/flask-todolist-design.png)
  
  Tampilan aplikasi kita sangat sederhana namun tetap fungsional dan harus berfungsi sesuai dengan yang kita inginkan.
  
  User Interface (UI) dari aplikasi ini dibuat dengan menggunakan [UI framework Bootstrap](https://getbootstrap.com/) karena relatif mudah dipakai. Saya sudah menyediakan template yang akan kita gunakan untuk membuat Todo list ini, bisa diunduh [disini](https://github.com/ekaputra07/workshop-python-unsika-2021/blob/main/4-flask-todolist-livecoding/index.html).
  
</details>

<details>
  <summary><b>2. Requirements Aplikasi</b></summary>
  
  ![Requirements Aplikasi Todolist dengan Flask](https://github.com/ekaputra07/workshop-python-unsika-2021/raw/main/screenshots/flask-todolist-requirements.png)
  
  Sebelum kita memulai sebuah proyek software, ada baiknya kita sudah memiliki banyangan apa tujuan akhir dari proyek yang akan kita buat. Apa fitur-fitur yang diperlukan dan bagaimana mereka akan bekerja. Ini penting karena perencanaan yang matang akan membuat proses pembuatan proyek berjalan lebih mulus meskipun tantangan-tantangan tidak terduga bisa saja muncul dalam prosesnya. Tapi itulah tugas seorang programmer, solving problem dengan teknologi.
  
  Pada gambar gambar diatas saya sudah menyiapkan beberapa requirements untuk proyek Todo kita kali ini, apabila semua requirements itu berhasil kita kerjakan maka proyek bisa dibilang sukses.
  
</details>

<details>
  <summary><b>3. Rancangan URL Aplikasi</b></summary>
  
  ![Rancangan URL Aplikasi Todolist dengan Flask](https://github.com/ekaputra07/workshop-python-unsika-2021/raw/main/screenshots/flask-todolist-urls.png)
  
  Sebelum kita mulai coding aplikasi berbasis web, kita juga perlu memiliki bayangan halaman-halaman apa yang kita perlukan dan URL-URL apa saja yang kita perlukan untuk mendukung aplikasi yang akan kita buat.
  
  Seperti terlihat diatas bahwa kita akan membuat 4 buah endpoint yang masing-masing memiliki satu tugas khusus. Kenapa kita perlu 4 endpoint? kenapa tidak satu saja? Karena lebih mudah membuat endpoint yang bertujuan untuk melakukkan satu tugas spesifik daripada membuat satu endpoint yang harus melakukkan banyak hal.
  
  Sekali lagi, tujuan kita adalah membuat aplikasi yang tidak cuma berjalan baik tetapi juga mudah untuk di maintain.
</details>

<details>
  <summary><b>4. Demo Aplikasi</b></summary>
  
  ![Menjalankan Aplikasi](https://github.com/ekaputra07/workshop-python-unsika-2021/raw/main/screenshots/hello-flask-run.png)
  
  Buat yang ingin mencoba aplikasi yang sudah jadi, silahkan arahkan terminalnya ke direktori `3-flask-todolist/`.
  
  Pertama kita install dulu library yang kita perlukan untuk proyek ini, karena ini adalah proyek sederhana maka kita hanya perlu Flask, itu terlihat dari isi file `requirements.txt` yang merupakan cara kita mendaftarkan dependencies yang diperlukan sebuah proyek Python.
  
  Kita install semua library yang diperlukan dengan menjalankan perintah:

  ```
  pip install -r requirements.txt
  ```

  Apabila Flask sudah terinstall maka aplikasi tinggal dijalankan dengan perintah:
  
  ```
  flask run
  ```
  
  Setelah aplikasi berjalan maka tinggal buka web browser dan buka alamat: `localhost:5000`, localhost adalah alamat tempat server Flask berjalan dan 5000 adalah port aplikasi todo kita berjalan.
</details>

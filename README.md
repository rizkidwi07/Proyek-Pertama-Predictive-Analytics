# Laporan Proyek Machine Learning - Rizki Dwi Sya'bana Nugraha
## Domain Proyek

Domain yang dipilih untuk proyek _machine learning_ ini adalah **Ekonomi dan Bisnis**, dengan judul **Predictive Analytics : Prediksi Harga Properti Rumah di Kota Bandung**

### Latar Belakang

![Prediksi Harga Properti](https://pict.sindonews.net/dyn/850/pena/news/2024/05/08/34/1373379/harga-rumah-di-ri-jauh-lebih-murah-ketimbang-negara-lain-tapi-tingkat-kepemilikan-rendah-nsw.jpg)
  
Pasar properti di Indonesia, khususnya di kota Bandung, mengalami perkembangan yang pesat dalam beberapa tahun terakhir. Dengan meningkatnya urbanisasi dan permintaan perumahan, pemahaman yang lebih baik tentang faktor-faktor yang mempengaruhi harga properti menjadi semakin penting. Namun, informasi harga seringkali sulit diakses dan tidak transparan bagi calon pembeli atau investor.

Bandung Housing Price Dataset yang dikumpulkan melalui web scraping dari situs [Jual Beli Properti Rumah Apartemen | Rumah123](https://www.rumah123.com/) pada Maret 2024, memberikan peluang untuk menganalisis dan memprediksi harga properti dengan lebih akurat. Dengan menggunakan metode _machine learning_, kita dapat memanfaatkan data historis untuk mengembangkan model prediktif yang dapat membantu dalam pengambilan keputusan.

### Mengapa dan Bagaimana Masalah Ini Harus Diselesaikan?

- Banyak pembeli atau penjual properti tidak memiliki informasi yang cukup mengenai harga pasar. Model prediksi harga dapat membantu mengurangi kesenjangan ini dengan memberikan estimasi yang akurat berdasarkan data objektif.
  
- Agen properti, pengembang, dan pembeli dapat menggunakan prediksi harga untuk mengevaluasi apakah harga yang ditawarkan sesuai dengan kondisi pasar.
  
- Dengan prediksi harga yang akurat, pasar properti menjadi lebih efisien karena harga yang ditawarkan mendekati nilai wajar, sehingga mengurangi kemungkinan spekulasi yang tidak sehat.
  
- Meningkatkan aksesibilitas bagi masyarakat dalam memperoleh hunian yang sesuai dengan anggaran mereka.
  
- Membantu pemerintah dalam membuat kebijakan terkait properti dan perumahan.


## Business Understanding

### Problem Statements

Berdasarkan latar belakang di atas, berikut ini merupakan rincian masalah yang dapat diselesaikan pada proyek ini:
- Dari serangkaian fitur yang ada, fitur apa yang paling berpengaruh terhadap harga prediksi properti rumah di Bandung?
- Berapa harga pasar properti rumah di Bandung dengan karakteristik atau fitur tertentu?  

### Goals

Tujuan dari proyek ini adalah:
- Mengetahui fitur yang paling berkorelasi dengan harga properti rumah di Bandung.
- Membuat model _machine learning_ yang dapat memprediksi harga properti rumah di Bandung seakurat mungkin berdasarkan fitur-fitur yang ada.

### Solution statements
- Metodologi pada proyek ini adalah: Membangun model regresi dengan harga properti rumah sebagai target
- Menggunakan algoritma seperti: K-Nearest Neighbor (KNN), Random Forest, dan Boosting Algorithm
- Untuk mengukur performa model, digunakan metrik berikut: Mean Squared Error (MSE) atau Root Mean Square Error (RMSE)

## Data Understanding
Dataset yang digunakan dalam proyek ini adalah data yang berfokus pada properti perumahan di Bandung, Jawa Barat, Indonesia. Data ini dapat diunduh melalui Kaggle. 

Informasi Dataset:

Jenis | Keterangan
--- | ---
Title | Daftar Harga Rumah di Kota Bandung
Source | [Kaggle](https://www.kaggle.com/datasets/khaleeel347/harga-rumah-seluruh-kecamatan-di-kota-bandung)
Maintainer | [Khalilullah Al Faath](https://www.kaggle.com/khaleeel347)
License | Data files © Original Authors
Visibility | Public
Tags | Beginner, Data Visualization, Exploratory Data Analysis, Regression, Asia
Usability | 8.82

### Variabel-variabel pada Dataset Daftar Harga Rumah di Kota Bandung adalah sebagai berikut:
- `type`: Jenis atau kategori properti.
- `status`: Status properti (misalnya, tersedia, terjual).
- `price`: Harga properti dalam Rupiah (IDR).
- `installment`: Rincian rencana cicilan yang terkait dengan properti.
- `house_name`: Nama atau judul properti residensial.
- `location`: Lokasi atau area di Bandung di mana properti tersebut berada.
- `bedroom_count`: Jumlah kamar tidur di properti.
- `bathroom_count`: Jumlah kamar mandi di properti.
- `carport_count`: Jumlah carport atau tempat parkir yang tersedia di properti.
- `land_area`: Total luas tanah properti dalam meter persegi.
- `building_area`: Total luas bangunan properti dalam meter persegi.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data atau exploratory data analysis.

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Anda perlu menjelaskan tahapan dan parameter yang digunakan pada proses pemodelan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan kelebihan dan kekurangan dari setiap algoritma yang digunakan.
- Jika menggunakan satu algoritma pada solution statement, lakukan proses improvement terhadap model dengan hyperparameter tuning. **Jelaskan proses improvement yang dilakukan**.
- Jika menggunakan dua atau lebih algoritma pada solution statement, maka pilih model terbaik sebagai solusi. **Jelaskan mengapa memilih model tersebut sebagai model terbaik**.

## Evaluation
Pada bagian ini anda perlu menyebutkan metrik evaluasi yang digunakan. Lalu anda perlu menjelaskan hasil proyek berdasarkan metrik evaluasi yang digunakan.

Sebagai contoh, Anda memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:
- Penjelasan mengenai metrik yang digunakan
- Menjelaskan hasil proyek berdasarkan metrik evaluasi

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.

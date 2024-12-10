# Laporan Proyek Machine Learning - Rizki Dwi Sya'bana Nugraha
## Domain Proyek

Domain yang dipilih untuk proyek _machine learning_ ini adalah **Ekonomi dan Bisnis**, dengan judul **Predictive Analytics: Prediksi Harga Properti Rumah di Kota Bandung**

### Latar Belakang

<div><img src="https://github.com/rizkidwi07/Source/raw/main/harga-rumah-di-ri-jauh-lebih-murah-ketimbang-negara-lain-tapi-tingkat-kepemilikan-rendah-nsw.jpg") width="1000"/></div><br />
  
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
- Bagaimana memprediksi harga rumah dengan fitur tertentu?  

### Goals

Tujuan dari proyek ini adalah:
- Mengetahui fitur yang paling berkorelasi dengan harga properti rumah di Bandung.
- Membuat model _machine learning_ yang dapat memprediksi harga properti rumah di Bandung seakurat mungkin berdasarkan fitur-fitur yang ada.

### Solution statements
- Metodologi pada proyek ini adalah: Membangun model regresi dengan harga properti rumah sebagai target
- Menggunakan algoritma seperti: K-Nearest Neighbor (KNN), Random Forest, dan Boosting Algorithm
- Untuk mengukur performa model, digunakan metrik berikut: Mean Squared Error (MSE)
  
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

### Exploratory Data Analysis
<div><img src="https://github.com/rizkidwi07/Source/raw/main/Screenshot%202024-12-06%20003443.png") width="450"/></div><br />
Dari output terlihat bahwa:

- Jumlah data terdiri dari 7.611 baris dan 11 kolom.
- Terdapat missing value di beberapa kolom, diantaranya pada `status`, `land_area`, dan `building_area`.
- Kolom `price`, `installment`, `land_area`, dan `building_area` bertipe objek, padahal kita akan memprediksi harga yang merupakan kategori numerik. Hal ini harus diubah menjadi numerik dengan tipe data int64.

<div><img src="https://github.com/rizkidwi07/Source/raw/main/Screenshot%202024-12-06%20004100.png") width="450"/></div><br />

Dari hasil fungsi describe(), nilai minimum untuk kolom `bedroom_count`, `bathroom_count`, dan `carport_count` adalah 0. `bedroom_count`, `bathroom_count`, dan `carport_count` adalah jumlah dari kamar tidur, kamar mandi, dan tempat parkir di suatu properti, sehingga tidak mungkin ada properti dengan jumlah kamar tidur, kamar mandi, dan tempat parkir bernilai 0. Cek ada berapa missing value pada ketiga kolom tersebut.

<div><img src="https://github.com/rizkidwi07/Source/raw/main/Screenshot%202024-12-08%20000559.png") width="450"/></div><br />

- Menangani Missing Value

  <div><img src="https://github.com/rizkidwi07/Source/blob/main/Screenshot%202024-12-06%20004131.png") width="225"/></div><br />

  Berdasarkan hasil di atas, dapat diketahui bahwa nilai yang paling dominan dalam kolom `status` ialah "Featured". Nilai inilah yang selanjutnya akan digunakan sebagai pengganti missing value.

  <div><img src="https://github.com/rizkidwi07/Source/blob/main/Screenshot%202024-12-06%20004145.png") width="1000"/></div><br />

  Dua sampel missing value pada kolom `land_area` merupakan jumlah yang kecil jika dibandingkan dengan jumlah total sampel yaitu 7.611. Jika 2 sampel ini dihapus, tidak jadi masalah sebab kita masih memiliki 7.611 sampel lainnya. Oleh karena itu, bisa dihapus saja missing value ini.

  <div><img src="https://github.com/rizkidwi07/Source/blob/main/Screenshot%202024-12-06%20004151.png") width="1000"/></div><br />

  Satu sampel missing value merupakan pada kolom `building_area` merupakan jumlah yang kecil jika dibandingkan dengan jumlah total sampel yaitu 7.611. Jika 1 sampel ini dihapus, tidak jadi masalah sebab kita masih memiliki 7.611 sampel lainnya. Oleh karena itu, bisa dihapus saja missing value ini.

  Drop baris yang terdapat nilai 0.

  <div><img src="https://github.com/rizkidwi07/Source/blob/main/Screenshot%202024-12-06%20004214.png") width="225"/></div><br />

  Missing value sudah diatasi. Jumlah sampel sekarang ada sebanyak 5.233

- Menangani Masalah Tipe Data

  Konversi kolom `price`, `installment`, `land_area`, dan `building_area` ke dalam tipe data int64

  <div><img src="https://github.com/rizkidwi07/Source/blob/main/Screenshot%202024-12-06%20004236.png") width="225"/></div><br />

  Masalah tipe data sudah teratasi. Kolom `price`, `installment`, `land_area`, dan `building_area` sudah dalam tipe data int64

- Menangani Duplikasi Data

  <div><img src="https://github.com/rizkidwi07/Source/raw/main/Screenshot%202024-12-06%20004053.png") width="250"/></div>

  Hapus data pada baris yang memiliki duplikasi data dengan fungsi drop.

  <div><img src="https://github.com/rizkidwi07/Source/blob/main/Screenshot%202024-12-06%20004225.png") width="225"/></div><br />

  Duplikasi data sudah teratasi. Jumlah sampel sekarang ada sebanyak 4.867

- Menangani Masalah Outliers

  <div><img src="https://github.com/rizkidwi07/Source/blob/main/Screenshot%202024-12-06%20011243.png") width="450"/></div><br />
  <div><img src="https://github.com/rizkidwi07/Source/blob/main/Screenshot%202024-12-06%20011255.png") width="450"/></div><br />
  <div><img src="https://github.com/rizkidwi07/Source/blob/main/Screenshot%202024-12-06%20011303.png") width="450"/></div><br />
  <div><img src="https://github.com/rizkidwi07/Source/blob/main/Screenshot%202024-12-06%20011309.png") width="450"/></div><br />
  <div><img src="https://github.com/rizkidwi07/Source/blob/main/Screenshot%202024-12-06%20011315.png") width="450"/></div><br />
  <div><img src="https://github.com/rizkidwi07/Source/blob/main/Screenshot%202024-12-06%20011320.png") width="450"/></div><br />
  <div><img src="https://github.com/rizkidwi07/Source/blob/main/Screenshot%202024-12-06%20011325.png") width="450"/></div><br />
  
  Hasil bloxpot dari kolom numerik `price`, `installment`, `bedroom_count`, `bathroom_count`, `carport_count`, `land_area`, `building_area` terdapat beberapa outliers.

  Hapus data pada baris yang memiliki outliers dengan teknik IQR.

  <div><img src="https://github.com/rizkidwi07/Source/blob/main/Screenshot%202024-12-06%20004259.png") width="225"/></div><br />

  Dataset sekarang telah bersih dan memiliki 3.751 sampel.

- Univariate Analysis

  Univariate Analysis adalah menganalisis setiap fitur secara terpisah.

  **Analisis jumlah nilai unique pada setiap fitur kategorik**
  
  <div><img src="https://github.com/rizkidwi07/Source/raw/main/Screenshot%202024-12-06%20012217.png") width="450"/></div><br />
  
  Terdapat 1 kategori pada fitur `type`, yaitu Rumah. Dari data persentase dapat disimpulkan bahwa 100% merupakan tipe Rumah.
  
  <div><img src="https://github.com/rizkidwi07/Source/raw/main/Screenshot%202024-12-06%20012223.png") width="450"/></div><br />
  
  Terdapat 2 kategori pada fitur `status`, yaitu Featured dan Premiere. Dari data persentase dapat disimpulkan bahwa 98.9% merupakan tipe Featured dan 1.1% merupakan tipe Premiere.
  
  <div><img src="https://github.com/rizkidwi07/Source/raw/main/Screenshot%202024-12-06%20012232.png") width="450"/></div><br />
  
  Terdapat 3.701 kategori pada fitur `house_name`. Ini berarti terdapat 3.701 macam nama rumah yang ada.
  
  <div><img src="https://github.com/rizkidwi07/Source/raw/main/Screenshot%202024-12-06%20012240.png") width="450"/></div><br />
  
  Terdapat 27 kategori pada fitur `location`. Ini berarti terdapat rumah di 27 lokasi berbeda.
  
  **Analisis jumlah nilai unique pada setiap fitur numerik**
  
  <div><img src="https://github.com/rizkidwi07/Source/raw/main/Screenshot%202024-12-06%20012320.png") width="450"/></div><br />
  <div><img src="https://github.com/rizkidwi07/Source/raw/main/Screenshot%202024-12-06%20012334.png") width="450"/></div><br />
  
  Dari histogram `price`, kita bisa memperoleh beberapa informasi, antara lain:
  
  - Distribusi harga miring ke kanan (right-skewed). Hal ini akan berimplikasi pada model.
  - Semakin tinggi harga rumah, semakin sedikit jumlah sampel yang tersedia. Tren ini menunjukkan bahwa rumah dengan harga terjangkau lebih umum dibandingkan rumah mewah.
  - Rentang harga rumah cukup lebar, mencakup properti dari beberapa ratus juta hingga sekitar Rp 10 miliar.
  - Berdasarkan konsentrasi sampel, dapat disimpulkan bahwa rumah dengan harga di bawah Rp 2 miliar mendominasi pasar.
  
  
- Multivariate Analysis
  
  Multivariate Analysis adalah menganalisis hubungan antara dua atau lebih variabel pada data.
  
  **Analisis rata-rata harga terhadap masing-masing fitur untuk mengetahui pengaruh fitur kategori terhadap harga** 
  
  <div><img src="https://github.com/rizkidwi07/Source/raw/main/Screenshot%202024-12-06%20012413.png") width="450"/></div><br />
  <div><img src="https://github.com/rizkidwi07/Source/raw/main/Screenshot%202024-12-06%20012419.png") width="450"/></div><br />
  
  Dengan mengamati rata-rata harga relatif terhadap fitur kategori di atas, dapat diperoleh insight sebagai berikut:
  
  -  Karena fitur `type` hanya berisi satu nilai (Rumah), fitur ini tidak memiliki pengaruh signifikan terhadap variasi `price`. Dengan kata lain, tidak ada perbedaan rata-rata harga yang bisa dianalisis berdasarkan tipe properti. Sehingga, fitur tersebut dapat di-drop.
  - Properti dengan `status` Premier memiliki rata-rata harga lebih tinggi dibandingkan dengan properti ber`status` Featured. `status` properti tampaknya memiliki dampak signifikan pada rata-rata `price`.
  - Terdapat lebih dari 3.000 nama rumah yang unik. `house_name` tidak terlalu membantu untuk analisis agregat karena distribusinya sangat tersebar. Sehingga, fitur tersebut dapat di-drop.
  - Distribusi antara kecamatan cukup merata. `location` merupakan fitur penting yang dapat mempengaruhi harga rumah. Properti di lokasi populer seperti kemungkinan memiliki harga lebih tinggi dibandingkan dengan lokasi yang kurang terwakili.
  
  - **Analisis hubungan antar fitur numerik**
  
  <div><img src="https://github.com/rizkidwi07/Source/raw/main/Screenshot%202024-12-06%20012503.png") width="450"/></div><br />
  
  Pada pola sebaran data grafik pairplot, terlihat `installment`, `land_area`, dan `building_area` memiliki korelasi yang tinggi dengan fitur `price`. Sedangkan ketiga fitur lainnya yaitu `bedroom_count`, `bathroom_count`, dan `carport_count` terlihat memiliki korelasi yang lemah karena sebarannya tidak membentuk pola. Untuk mengevaluasi skor korelasinya, gunakan correlation matrix.
  
  <div><img src="https://github.com/rizkidwi07/Source/raw/main/Screenshot%202024-12-06%20012531.png") width="450"/></div><br />
  
  Fitur `installment` memiliki skor korelasi yang sangat tinggi (1), `land_area`, dan `building_area` memiliki skor korelasi yang besar (di atas 0.75) dengan fitur target `price`. Artinya, fitur `price`       berkorelasi tinggi dengan ketiga fitur tersebut. Sementara itu, fitur `bedroom_count`, `bathroom_count` memiliki korelasi normal (0.5). Fitur `carport_count` (0.42) bisa didrop karena kurang berkolerasi.
  
  <div><img src="https://github.com/rizkidwi07/Source/raw/main/Screenshot%202024-12-06%20014153.png") width="500"/></div><br />
  
  Inilah data yang akan digunakan. Terdapat 3.751 sampel dari 8 kategori (fitur).

## Data Preparation

Teknik yang digunakan dalam penyiapan data (Data Preparation) yaitu:

- One-Hot Encoding
  
  One hot encoding adalah teknik mengubah data kategorik menjadi data numerik dimana setiap kategori menjadi kolom baru ke dalam vektor biner (nilai 0 atau 1). Fitur yang akan diubah menjadi numerik pada proyek ini adalah kolom `status` dan `location`.
- Train Test Split Data
  
  Train test split atau proses membagi data menjadi data latih dan data uji. Data latih akan digunakan untuk membangun model, sedangkan data uji akan digunakan untuk menguji performa model. Pada proyek ini, 90% dataset digunakan untuk melatih model, dan 10% sisanya digunakan untuk mengevaluasi model.
- Normalisasi
  
  Algoritma machine learning akan memiliki performa lebih baik dan bekerja lebih cepat jika dimodelkan dengan data seragam yang memiliki skala relatif sama. Pada proyek ini proses Standarisasi akan menggunakan StandardScaler.

## Modeling
  Pada tahap modeling ini dibuat beberapa model dengan algoritma yang berbeda-beda. Pada proyek ini akan dibuat 3 model, diantaranya yaitu menggunakan KNN, Random Forest, dan AdaBoost. 
  - K-Nearest Neighbour

    K-Nearest Neighbour bekerja dengan membandingkan jarak satu sampel ke sampel pelatihan lain dengan memilih sejumlah k tetangga terdekat. Proyek ini menggunakan [sklearn.neighbors.KNeighborsRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html) dengan memasukkan X_train dan y_train dalam membangun model. Parameter yang digunakan pada proyek ini adalah :
    + `n_neighbors` = 10 (Jumlah tetangga terdekat yang digunakan dalam prediksi).

  - Random Forest

    Algoritma random forest adalah teknik dalam machine learning dengan metode ensemble. Teknik ini beroperasi dengan membangun banyak decision tree pada waktu pelatihan. Proyek ini menggunakan [sklearn.ensemble.RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html) dengan memasukkan X_train dan y_train dalam membangun model. Parameter yang digunakan pada proyek ini adalah :
    + `n_estimators` = 50 (Jumlah maksimum estimator di mana boosting dihentikan).
    + `max_depth` = 16 (Kedalaman maksimum setiap tree).
    + `random_state` = 55 (Mengontrol seed acak yang diberikan pada setiap base_estimator pada setiap iterasi boosting).
    + `n_jobs` = -1 (Jumlah job (pekerjaan) yang digunakan secara paralel untuk mengontrol thread atau proses yang berjalan).

  - Adaboost

    AdaBoost juga disebut Adaptive Boosting adalah teknik dalam machine learning dengan metode ensemble.  Algoritma yang paling umum digunakan dengan AdaBoost adalah pohon keputusan (decision trees) satu tingkat yang berarti memiliki pohon Keputusan dengan hanya 1 split. Pohon-pohon ini juga disebut Decision Stumps. Algoritma ini bertujuan untuk meningkatkan performa atau akurasi prediksi dengan cara menggabungkan beberapa model sederhana dan dianggap lemah (weak learners) secara berurutan sehingga membentuk suatu model yang kuat (strong ensemble learner). Proyek ini menggunakan [sklearn.ensemble.AdaBoostRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html) dengan memasukkan X_train dan y_train dalam membangun model. Parameter yang digunakan pada proyek ini adalah :
    + `n_estimators` = default (Jumlah maksimum estimator di mana boosting dihentikan).
    + `learning_rate` = 0.05 (Learning rate memperkuat kontribusi setiap regressor).
    + `random_state` = 55 (Mengontrol seed acak yang diberikan pada setiap base_estimator pada setiap iterasi boosting).

## Evaluation
Pada proyek ini, model yang dibuat merupakan kasus prediksi harga dan menggunakan metriks akurasi. Metrik evaluasi yang digunakan pada proyek ini adalah akurasi dan mean squared error (MSE). Akurasi menentukan tingkat kemiripan antara hasil prediksi dengan nilai yang sebenarnya (y_test). Mean squared error (MSE) mengukur error dalam model statistik dengan cara menghitung rata-rata error dari kuadrat hasil aktual dikurang hasil prediksi. Berikut rumus dari MSE:

<div><img src="https://github.com/rizkidwi07/Source/raw/main/Screenshot%202024-12-06%20020439.png") width="450"/></div><br />

Berikut adalah nilai Mean Squared Error (MSE) untuk masing-masing model yang telah dibuat:

<div><img src="https://github.com/rizkidwi07/Source/raw/main/Screenshot%202024-12-10%20223813.png") width="450"/></div><br />

Berikut hasil evaluasi pada proyek ini:
<div><img src="https://github.com/rizkidwi07/Source/raw/main/Screenshot%202024-12-07%20000115.png") width="450"/></div><br />

Model Random Forest (RF) memiliki performa terbaik karena menghasilkan MSE (nilai eror) terendah baik pada data train maupun test. Sedangkan model dengan algoritma KNN memiliki eror yang paling besar. Sehingga model Random Forest (RF) yang akan kita pilih sebagai model terbaik untuk melakukan prediksi harga rumah di Bandung.

**Evaluasi Dampak Model Terhadap Business Understanding**

1. Apakah model menjawab problem statement?
   
  - Problem Statement 1: "Dari serangkaian fitur yang ada, fitur apa yang paling berpengaruh terhadap harga prediksi properti rumah di Bandung?"
  
    Dampak: Model Random Forest (RF), yang memiliki performa terbaik berdasarkan MSE, secara inheren menyediakan informasi mengenai pentingnya fitur melalui atribut feature importance. Hasil ini membantu menjawab fitur mana yang paling berpengaruh terhadap harga properti. Misalnya, fitur seperti lokasi, luas tanah, dan kondisi properti dapat diidentifikasi sebagai faktor dominan. Dengan ini, analisis dapat digunakan untuk pengambilan keputusan bisnis, seperti penentuan harga atau prioritas pemasaran.

  - Problem Statement 2: "Bagaimana memprediksi harga rumah dengan fitur tertentu?"
  
    Dampak: Model RF menghasilkan prediksi yang cukup akurat berdasarkan dataset dan fitur yang disediakan. Dengan menggunakan model ini, pelaku bisnis atau pengguna dapat memperkirakan harga rumah di Bandung berdasarkan parameter seperti status, cicilan, lokasi, jumlah kamar tidur, jumlah kamar mandi, luas tanah, dan luas bangunan.

2. Apakah model berhasil mencapai goals yang diharapkan?

  - Goal 1: "Mengetahui fitur yang paling berkorelasi dengan harga properti rumah di Bandung."
  
    Capaian: Random Forest tidak hanya memberikan akurasi tinggi dalam prediksi, tetapi juga menyediakan analisis fitur yang menunjukkan keterkaitan antara atribut (misalnya, lokasi, luas tanah) dan harga properti. Hal ini menjawab tujuan pertama dengan memberikan wawasan yang dapat ditindaklanjuti.

  - Goal 2: "Membuat model machine learning yang dapat memprediksi harga properti rumah di Bandung seakurat mungkin berdasarkan fitur-fitur yang ada."
  
    Capaian: Dengan menggunakan evaluasi berbasis MSE, model Random Forest memberikan error terendah dibandingkan algoritma lain (KNN dan Boosting). Hal ini menunjukkan bahwa tujuan kedua telah tercapai karena model mampu memprediksi harga rumah dengan akurasi tinggi.

3. Apakah solusi statement yang direncanakan berdampak?

    Iya berdampak. Metodologi yang direncanakan—menggunakan algoritma seperti KNN, Random Forest, dan Boosting Algorithm dengan MSE sebagai metrik utama—terbukti efektif. Pilihan Random Forest sebagai model akhir memberikan keseimbangan antara interpretabilitas dan akurasi. Dalam konteks bisnis, ini berarti solusi tidak hanya menjawab pertanyaan analitis tetapi juga mendukung keputusan operasional, seperti penentuan harga pasar atau strategi penjualan.

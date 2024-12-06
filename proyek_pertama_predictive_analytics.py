# -*- coding: utf-8 -*-
"""Proyek Pertama: Predictive Analytics.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OKRQUfkSrOyAl6y2xPHaN0psvjQ1wEfM

## Predictive Analytics : Prediksi Harga Properti Rumah di Kota Bandung

## Data Loading

### Import Library
"""

# Commented out IPython magic to ensure Python compatibility.
import zipfile
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib inline
import seaborn as sns

"""### Mengunduh Dataset"""

# Download dataset
!kaggle datasets download -d khaleeel347/harga-rumah-seluruh-kecamatan-di-kota-bandung

# Melakukan ekstraksi pada file zip
local_zip = 'harga-rumah-seluruh-kecamatan-di-kota-bandung.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/content/harga-rumah-seluruh-kecamatan-di-kota-bandung/')
zip_ref.close()

# Cek isi direktori dataset
os.listdir('/content/harga-rumah-seluruh-kecamatan-di-kota-bandung/')

"""Dari keluaran di atas, dapat diketahui bahwa ada dua berkas data, diantaranya adalah dataset utama (raw) dan berkas lainnya adalah merupakan dataset yang sudah bersih. Pada proyek ini akan menggunakan dataset utama (raw)

Mari kita lihat data dokumentasinya dengan menggunakan `pandas`.
"""

# Cek dokumentasi dataset
house = pd.read_csv('/content/harga-rumah-seluruh-kecamatan-di-kota-bandung/results.csv', names=["type", "status", "price", "installment", "house_name", "location", "bedroom_count", "bathroom_count", "carport_count", "land_area", "building_area"])
house

"""- Terdapat 7.611 baris dalam dataset.
- Terdapat 11 kolom yaitu: `type`, `status`, `price`, `installment`, `house_name`, `location`, `bedroom_count`, `bathroom_count`, `carport_count`, `land_area`, dan `building_area`.

## Exploratory Data Analysis (EDA)

Variabel-variabel pada Dataset Daftar Harga Rumah di Kota Bandung adalah sebagai berikut:

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
"""

house.info()

"""Dari output terlihat bahwa:

- Terdapat missing value di beberapa kolom, diantaranya pada `status`, `land_area`, dan `building_area`.

- Kolom `price`, `installment`, `land_area`, dan `building_area` bertipe objek, padahal kita akan memprediksi harga yang merupakan kategori numerik. Hal ini harus diubah menjadi numerik dengan tipe data int64.
"""

house.isnull().sum()

"""- Tedapat 7466 missing value pada kolom `status`
- Terdapat 2 missing value pada kolom `land_area`
- Terdapat 1 missing value pada kolom `building_area`
"""

print("Jumlah duplikasi: ", house.duplicated().sum())

house.describe()

"""Dari hasil fungsi describe(), nilai minimum untuk kolom `bedroom_count`, `bathroom_count`, dan `carport_count` adalah 0. `bedroom_count`, `bathroom_count`, dan `carport_count` adalah jumlah dari kamar tidur, kamar mandi, dan tempat parkir di suatu properti, sehingga tidak mungkin ada properti dengan jumlah kamar tidur, kamar mandi, dan tempat parkir bernilai 0. Cek ada berapa missing value pada ketiga kolom tersebut."""

bedroom = (house.bedroom_count == 0).sum()
bathroom = (house.bathroom_count == 0).sum()
carport = (house.carport_count == 0).sum()

print("Nilai 0 di kolom bedroom_count ada: ", bedroom)
print("Nilai 0 di kolom bathroom_count ada: ", bathroom)
print("Nilai 0 di kolom carport_count ada: ", carport)

"""### Menangani Missing Value"""

house[house.status.isna()]

"""Dapat dilihat bahwa baris data tersebut masih mengandung banyak informasi penting sehingga sayang jika langsung dibuang. Oleh karena itu, pada kolom `status`, akan menggunakan metode imputation untuk menangani missing value."""

house.status.value_counts()

"""Berdasarkan hasil di atas, dapat diketahui bahwa nilai yang paling dominan dalam kolom `status` ialah "Featured". Nilai inilah yang selanjutnya akan digunakan sebagai pengganti missing value."""

house['status'].fillna(value="Featured", inplace=True)

print("Jumlah missing value: ", house.status.isna().sum())

house.info()

house[house.land_area.isna()]

"""2 sampel missing value merupakan jumlah yang kecil jika dibandingkan dengan jumlah total sampel yaitu 7.611. Jika 2 sampel ini dihapus, tidak jadi masalah sebab kita masih memiliki 7.611 sampel lainnya. Oleh karena itu, bisa dihapus saja missing value ini."""

house[house.building_area.isna()]

"""1 sampel missing value merupakan jumlah yang kecil jika dibandingkan dengan jumlah total sampel yaitu 7.611. Jika 1 sampel ini dihapus, tidak jadi masalah sebab kita masih memiliki 7.611 sampel lainnya. Oleh karena itu, bisa dihapus saja missing value ini."""

house = house.dropna()

house.info()

# Drop baris dengan nilai `bedroom_count`, `bathroom_count`, dan `carport_count` = 0
house = house.loc[(house[['bedroom_count', 'bathroom_count', 'carport_count']]!=0).all(axis=1)]

house.info()

"""### Menangani Duplikasi Data"""

house.drop_duplicates(inplace=True)

house.info()

"""### Menangani Masalah Tipe Data"""

# Fungsi untuk membersihkan dan mengkonversi nilai price
def clean_price(house):
    house = str(house)
    house = house.replace("Rp ", "").replace(".", "").replace(",", ".").strip()
    if "Miliar" in house:
        house = house.replace("Miliar", "")
        return int(float(house) * 1_000_000_000)
    elif "Juta" in house:
        house = house.replace("Juta", "")
        return int(float(house) * 1_000_000)
    else:
        try:
            return int(house)  # Jika tidak ada satuan, asumsikan sudah dalam Rupiah
        except ValueError:
            # Jika price tidak bisa dikonversi ke int, kembalikan nilai menjadi Nan
            return float('Nan')

# Terapkan fungsi ke kolom price
house['price'] = house['price'].apply(clean_price).astype('int64')

# Fungsi untuk membersihkan dan mengonversi kolom installment
def convert_installment(house):
    house = str(house)
    house = house.replace("Cicilan: ", "").strip()
    if "Jutaan" in house:
        house = house.replace("Jutaan per bulan", "")
        return int(float(house) * 1_000_000)
    elif "Ribuan" in house:
        house = house.replace("Ribuan per bulan", "")
        return int(float(house) * 1_000)
    else:
        return 0

# Terapkan fungsi pada kolom installment
house['installment'] = house['installment'].apply(convert_installment).astype('int64')

# Fungsi untuk membersihkan dan mengkonversi nilai area
def clean_area(house):
    house = str(house)
    return int(house.replace("m²", "").strip())

# Terapkan fungsi ke kolom land_area dan building_area
house['land_area'] = house['land_area'].apply(clean_area).astype('int64')
house['building_area'] = house['building_area'].apply(clean_area).astype('int64')

house.info()

house

"""### Menangani Outliers"""

sns.boxplot(x=house['price'])

sns.boxplot(x=house['installment'])

sns.boxplot(x=house['bedroom_count'])

sns.boxplot(x=house['bathroom_count'])

sns.boxplot(x=house['carport_count'])

sns.boxplot(x=house['land_area'])

sns.boxplot(x=house['building_area'])

numeric_col = ['price', 'installment', 'bedroom_count', 'bathroom_count', 'carport_count', 'land_area', 'building_area']
house_numeric = house[numeric_col]
#kita cek apakah kolom numerik terpanggil
house[numeric_col]

Q1 = house_numeric.quantile(0.25)
Q3 = house_numeric.quantile(0.75)
IQR = Q3 - Q1
house = house[~((house_numeric < (Q1 - 1.5 * IQR)) | (house_numeric > (Q3 + 1.5 * IQR))).any(axis=1)]

house.shape

"""Dataset sekarang telah bersih dan memiliki 3.751 sampel.

### Univariate Analysis
"""

numerical_features = ['price', 'installment', 'bedroom_count', 'bathroom_count', 'carport_count', 'land_area', 'building_area']
categorical_features = ['type', 'status', 'house_name', 'location']

feature = categorical_features[0]
count = house[feature].value_counts()
percent = 100*house[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

"""Terdapat 1 kategori pada fitur `type`, yaitu Rumah. Dari data persentase dapat disimpulkan bahwa 100% merupakan tipe Rumah."""

feature = categorical_features[1]
count = house[feature].value_counts()
percent = 100*house[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

"""Terdapat 2 kategori pada fitur `status`, yaitu Featured dan Premiere. Dari data persentase dapat disimpulkan bahwa 98.9% merupakan tipe Featured dan 1.1% merupakan tipe Premiere."""

feature = categorical_features[2]
count = house[feature].value_counts()
percent = 100*house[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)

"""Terdapat 3.701 kategori pada fitur `house_name`. Ini berarti terdapat 3.701 macam nama rumah yang ada."""

feature = categorical_features[3]
count = house[feature].value_counts()
percent = 100*house[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)

"""Terdapat 27 kategori pada fitur `location`. Ini berarti terdapat rumah di 27 lokasi berbeda."""

house.hist(bins=50, figsize=(20,15))
plt.show()

"""Mari amati histogram di atas, khususnya histogram untuk variabel `price` yang merupakan fitur target (label) pada data. Dari histogram `price`, kita bisa memperoleh beberapa informasi, antara lain:

- Distribusi harga miring ke kanan (right-skewed). Hal ini akan berimplikasi pada model.
- Semakin tinggi harga rumah, semakin sedikit jumlah sampel yang tersedia. Tren ini menunjukkan bahwa rumah dengan harga terjangkau lebih umum dibandingkan rumah mewah.
- Rentang harga rumah cukup lebar, mencakup properti dari beberapa ratus juta hingga sekitar Rp 10 miliar.
- Berdasarkan konsentrasi sampel, dapat disimpulkan bahwa rumah dengan harga di bawah Rp 2 miliar mendominasi pasar.

### Multivariate Analysis
"""

cat_features = house.select_dtypes(include='object').columns.to_list()

for col in cat_features:
  sns.catplot(x=col, y="price", kind="bar", dodge=False, height = 4, aspect = 3,  data=house, palette="Set3")
  plt.title("Rata-rata 'price' Relatif terhadap - {}".format(col))

  plt.xticks(rotation=45)
  plt.show()

"""Dengan mengamati rata-rata harga relatif terhadap fitur kategori di atas, dapat diperoleh insight sebagai berikut:

-  Karena fitur `type` hanya berisi satu nilai (Rumah), fitur ini tidak memiliki pengaruh signifikan terhadap variasi `price`. Dengan kata lain, tidak ada perbedaan rata-rata harga yang bisa dianalisis berdasarkan tipe properti. Sehingga, fitur tersebut dapat di-drop.
- Properti dengan `status` Premier memiliki rata-rata harga lebih tinggi dibandingkan dengan properti ber`status` Featured. `status` properti tampaknya memiliki dampak signifikan pada rata-rata `price`.
- Terdapat lebih dari 3.000 nama rumah yang unik. `house_name` tidak terlalu membantu untuk analisis agregat karena distribusinya sangat tersebar. Sehingga, fitur tersebut dapat di-drop.
- Distribusi antara kecamatan cukup merata. `location` merupakan fitur penting yang dapat mempengaruhi harga rumah. Properti di lokasi populer seperti kemungkinan memiliki harga lebih tinggi dibandingkan dengan lokasi yang kurang terwakili.

"""

house.drop(['type', 'house_name'], inplace=True, axis=1)

house.head()

# Mengamati hubungan antar fitur numerik dengan fungsi pairplot()
sns.pairplot(house, diag_kind = 'kde')

"""Pada pola sebaran data grafik pairplot, terlihat `installment`, `land_area`, dan `building_area` memiliki korelasi yang tinggi dengan fitur `price`. Sedangkan ketiga fitur lainnya yaitu `bedroom_count`, `bathroom_count`, dan `carport_count` terlihat memiliki korelasi yang lemah karena sebarannya tidak membentuk pola. Untuk mengevaluasi skor korelasinya, gunakan fungsi corr()."""

plt.figure(figsize=(10, 8))
correlation_matrix = house[numerical_features].corr().round(2)

# Untuk menge-print nilai di dalam kotak, gunakan parameter anot=True
sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, )
plt.title("Correlation Matrix untuk Fitur Numerik ", size=20)

"""Fitur `installment` memiliki skor korelasi yang sangat tinggi (1), `land_area`, dan `building_area` memiliki skor korelasi yang besar (di atas 0.75) dengan fitur target `price`. Artinya, fitur `price` berkorelasi tinggi dengan ketiga fitur tersebut. Sementara itu, fitur `bedroom_count`, `bathroom_count` memiliki korelasi normal (0.5). Fitur `carport_count` (0.42) bisa didrop karena kurang berkolerasi."""

house.drop(['carport_count'], inplace=True, axis=1)

house

"""Inilah data yang akan digunakan. Terdapat 3.751 sampel dari 8 kategori (fitur).

# Data Preparation

### One Hot Encoding
"""

from sklearn.preprocessing import  OneHotEncoder
house = pd.concat([house, pd.get_dummies(house['status'], prefix='status')],axis=1)
house = pd.concat([house, pd.get_dummies(house['location'], prefix='location')],axis=1)
house.drop(['status','location'], axis=1, inplace=True)
house.head()

"""### Train-Test-Split"""

from sklearn.model_selection import train_test_split

X = house.drop(["price"],axis =1)
y = house["price"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 123)

print(f'Total # of sample in whole dataset: {len(X)}')
print(f'Total # of sample in train dataset: {len(X_train)}')
print(f'Total # of sample in test dataset: {len(X_test)}')

"""### Normalisasi"""

from sklearn.preprocessing import StandardScaler

numerical_features = ['installment', 'bedroom_count', 'bathroom_count', 'land_area', 'building_area']
scaler = StandardScaler()
scaler.fit(X_train[numerical_features])
X_train[numerical_features] = scaler.transform(X_train.loc[:, numerical_features])
X_train[numerical_features].head()

X_train[numerical_features].describe().round(4)

"""Sekarang nilai mean = 0 dan standar deviasi = 1

# Modeling

### K-Nearest Neighbour
"""

# Siapkan dataframe untuk analisis model
models = pd.DataFrame(index=['train_mse', 'test_mse'],
                      columns=['KNN', 'RandomForest', 'Boosting'])

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

knn = KNeighborsRegressor(n_neighbors=10)
knn.fit(X_train, y_train)

models.loc['train_mse','knn'] = mean_squared_error(y_pred = knn.predict(X_train), y_true=y_train)

"""### Random Forest"""

# Impor library yang dibutuhkan
from sklearn.ensemble import RandomForestRegressor

# buat model prediksi
RF = RandomForestRegressor(n_estimators=50, max_depth=16, random_state=55, n_jobs=-1)
RF.fit(X_train, y_train)

models.loc['train_mse','RandomForest'] = mean_squared_error(y_pred=RF.predict(X_train), y_true=y_train)

"""### AdaBoost"""

from sklearn.ensemble import AdaBoostRegressor

boosting = AdaBoostRegressor(learning_rate=0.05, random_state=55)
boosting.fit(X_train, y_train)
models.loc['train_mse','Boosting'] = mean_squared_error(y_pred=boosting.predict(X_train), y_true=y_train)

"""# Evaluasi"""

# Lakukan scaling terhadap fitur numerik pada X_test sehingga memiliki rata-rata=0 dan varians=1
X_test.loc[:, numerical_features] = scaler.transform(X_test[numerical_features])

# Buat variabel mse yang isinya adalah dataframe nilai mse data train dan test pada masing-masing algoritma
mse = pd.DataFrame(columns=['train', 'test'], index=['KNN','RF','Boosting'])

# Buat dictionary untuk setiap algoritma yang digunakan
model_dict = {'KNN': knn, 'RF': RF, 'Boosting': boosting}

# Hitung Mean Squared Error masing-masing algoritma pada data train dan test
for name, model in model_dict.items():
    mse.loc[name, 'train'] = mean_squared_error(y_true=y_train, y_pred=model.predict(X_train))/1e3
    mse.loc[name, 'test'] = mean_squared_error(y_true=y_test, y_pred=model.predict(X_test))/1e3

# Panggil mse
mse

fig, ax = plt.subplots()
mse.sort_values(by='test', ascending=False).plot(kind='barh', ax=ax, zorder=3)
ax.grid(zorder=0)

"""Model Random Forest (RF) memberikan nilai eror yang paling kecil. Sedangkan model dengan algoritma KNN memiliki eror yang paling besar. Sehingga model Random Forest (RF) yang akan kita pilih sebagai model terbaik untuk melakukan prediksi harga rumah di Bandung."""

prediksi = X_test.iloc[:1].copy()
pred_dict = {'y_true':y_test[:1]}
for name, model in model_dict.items():
    pred_dict['prediksi_'+name] = model.predict(prediksi).round(1)

pd.DataFrame(pred_dict)

"""Terlihat bahwa prediksi dengan Random Forest (RF) memberikan hasil yang paling mendekati."""
# Problem Statement
Kopi merupakan komoditas internasional dan banyak negara yang memproduksi kopi seperti brazil indonesia , vietnam , kolombia dsb. Karena penggemar kopi di seluruh dunia juga banyak , berdasarkan website nescafe (salah satu merk kopi instan populer) konsumsi kopi sekitar 400 miliar cup setiap tahunnya. Jadi memang data ini menunjukkan bahwa kopi itu digemari oleh banyak orang. Jika kita asumsikan penduduk di dunia yang menikmati kopi 1 miliar saja  (untuk kemudahan hitungan) maka sehari kita menghabiskan sekitar 1,1 Miliar cup. angka yang cukup fantastis. [link](https://www.nescafe.com/gb/coffee-culture/knowledge/coffee-statistics#:~:text=Coffee%20is%20the%20one%20of%20the%20most%20popular%20drinks%20worldwide&text=On%20average%20there's%20around%20400%20billion%20cups%20consumed%20each%20year)

Jika kita lihat bagaimana pengolahan kopi dan bagaimana kopi itu di perdagangkan secara global, kopi itu diperdagangkan dengan kopi utuh (green bean) yang akan di perdagangkan. Kemudian green bean tersebut dikirim ke negara tujuan. Setelah sampai di negara tujuan, kopi akan di roasting sesuai dengan kebutuhan dari pelanggan. [link2](https://thosecoffeepeople.com/importing-coffee-beans-into-japan-guide/) [link3](https://coffeeassoc.com/supply-chain/) [link4](https://www.sidewalkcoffee.co.uk/pages/about-coffee-how-its-grown-processed-and-shipped#:~:text=Packing%20and%20shipping,transported%20by%20land%20or%20sea). Proses ini tentunya untuk memperpanjang umur kopi dibandingkan proses perdagangan biji kopi yang sudah di roasting.

Setelah menggali dari beberapa sumber [link5](https://mokhabika.com/level-roasting-coffee/) [link6](https://ottencoffee.co.id/majalah/perbedaan-antara-light-medium-dan-dark-roast-pada-kopi) [link7](https://kopitem.com/tentang-kopi/pengertian-roasting-kopi/) pemanggangan kopi itu ditentukan oleh beberapa level. Mulai dari green (untuk kopi yang belum dipanggang) ini biasanya yang dipakai untuk perdagangan dunia. Kopi dipanggang light. Kopi dipanggang medium. Kopi dipanggang dark. 3 klasifikasi ini merupakan secara garis besar bagaimana biji kopi itu dipanggang. Setiap level roasting itu akan menentukan rasa, cara penyeduhan, tingkat keasaman , dan mungkin faktor lain seperti aroma buah aroma kacang yang mungkin bisa muncul di setiap jenis kopi.

Modul ini akan membahas mengenai 3 biji kopi yaitu Laos Typica Bolaven, Doi Chaang, dan Brazil Cerrado. Setiap varietas ini tentunya akan membutuhkan handling berbeda-beda tergantung dari tingkat kematangannya. Semua kopi ini merupakan kopi yang berkualitas unggul dan memiliki daya tarik tersendiri untuk komunitas kopi internasional. Sebagai informasi harga. Laos Typica itu sekitaran 20-30 dolar [link harga](https://laocoffee.nl/our-coffee/). Doi chaang harga perkilo sekitar 50 dolar - 70 dolar [link harga](https://www.amazon.com/s?k=doi+chang+coffee&crid=2CBYQAFFVAAXK&sprefix=doi+chang+cof%2Caps%2C807&ref=nb_sb_ss_ts-doa-p_1_13). Dan kopi brazil cerado 30an dolar per kilonya [link harga](https://www.amazon.com/s?k=brazil+cerado&crid=23I2RT49UVCPW&sprefix=brazil+cerad%2Caps%2C733&ref=nb_sb_noss). Dengan harga segitu harusnya sebagai penikmat kopi harus memastikan bahwa setiap kopi yang di roasting harus memenuhi target tertentu.

Biji kopi ini hanya difokuskan pada 3 varietas tersebut. Dataset diambil dari JJ Mall Jatujak’s, “Bona Coffee.” di bangkok.  saya kurang tau mengapa alasan pengambilan dari 3 biji varietas tertentu itu. Asumsi saya mungkin di mall tersebut itu mungkin varietas yang sering laku merupakan varietas kopi tersebut. Oleh karena itu kemungkinan model ini digunakan untuk memberi panduan kepada pegawai dari mall tersebut. Alasan saya membikin model ini untuk sebagai panduan kepada pecinta 3 biji kopi tersebut bagaimana level roasting yang benar.

Dataset ini berisi
*   Lao typica bolaven hijau (green bean / belum dipanggang)
*   Lao typica bolaven dipanggang Light
*   Doi Chaang dipanggang Medium
*   Brazil Cerrado dipanggang Dark


 


# Objective

**Objektif = Membuat model penentuan tingkat roasting dari biji kopi untuk 3 varietas. (Doi Chaang, Brazil Cerrado, Laos Typica Bolaven). Dataset untuk green bean (kopi mentah) juga ditambahkan disini, namun hanya pada biji kopi laos typica saja. 2 varietas lain tidak terdapat gambar green bean nya.**

Possibility End-User = Perusahaan roasting Kopi, Pecinta kopi yang memiliki alat roasting sendiri, pegawai - pegawai kopi di cafe untuk pecinta kopi speciality. 

# Kesimpulan
Setelah melakukan pembuatan model dengan computer vision menggunakan cnn dan juga penguatan algoritma lain. Model sangat bagus untuk mendeteksi biji biji tersebut dengan tingkat kematangan tertentu yang kita inginkan. Model sangat baik jika kita membuat background seperti di studio dan juga diperlihatkan retakan-retakan pada biji kopi. Accuracy model sangat baik hingga mencapai 100% setelah dilakukan dengan vgg 16 ann improvement.  

Meskipun demikian model kurang bisa menebak dengan baik untuk biji kopi yang tidak sesuai dengan permintaan model, seperti biji kopi yang berada di tangan atau beberapa biji kopi yang mempunyai kemiripan warna kematangan. Ini namun bisa diatasi dengan kita mengambil satu biji saja sebagai bahan evaluasi untuk model tersebut. Improvement kedepannya adalah dengan menambahkan model dengan dataset yang berbeda yang menunjukkan tingkat kematangan dengan beberapa biji kopi yang sebagai contoh visualnya.

# URL
[Kaggle datasets](https://www.kaggle.com/datasets/gpiosenka/coffee-bean-dataset-resized-224-x-224/data)
[Hugging Face](https://huggingface.co/spaces/asanmaulana/kopi_machine_learning)
[Link Model](https://drive.google.com/file/d/12JcPzvl_6SjkZ2t0ik5NkXxWadIcp6Ss/view?usp=drive_link)
# Cam Sineği Vize Başvuru Merkezi

> Pencere bir sınırdır. Sinek bir vatandaştır. Vızıltı bir dilekçedir.

Bu yazılım, evinizin camına tekrar tekrar çarpan her sineğe **diplomatik pasaport**, **vize randevusu** ve **gerekçeli ret/onay yazısı** üreten ulusal dışişleri protokolüdür.

Anlam aramayın. Protokol vardır. Anlam sonradan gelir, genellikle gelmez.

## Neden var?

Çünkü:

1. Camın öteki tarafında yemek vardır.
2. Sinekler randevusuz giriş yapamaz.
3. Örümcek ağı bir göçmen kampı değildir (hukuken tartışmalıdır).
4. Birilerinin bu evrakı basması gerekiyordu. O biri biz çıktık.

## Kurulum

```bash
python3 vize.py
python3 vize.py --isim "Leyla Vızıltı" --ulke "Balkon Cumhuriyeti" --adet 3
```

Bağımlılık yoktur. Sadece Python 3. Cam da yardımcı olur ama zorunlu değildir.

## Çıktı örneği

Program size resmi görünümlü bir evrak basar. Onay oranı yaklaşık %42'dir. Bu oran bilimsel değildir; 42 güzel durduğu için seçilmiştir.

## Sıkça sorulmayan sorular

**Sinek ölürse vize düşer mi?**  
Düşer. Pasaport kişiye bağlıdır. Miras yoluyla kanat devri yoktur.

**Perde konsolosluk sayılır mı?**  
Sayılır ama öğleden sonra kapalıdır.

**Bu siyasi bir mesaj mı?**  
Hayır. Bu bir vize merkezidir. Siyaset camdan bakılınca hep aynı görünür; içeride evrak çoğalır. (Bu cümle tesadüftür.)

## Lisans

Bu proje, camın her iki yanındaki canlıların serbest dolaşımını savunur; yazılımın kendisi ise MIT kadar serbest, sinek kadar kısa ömürlüdür.

```
------------------------------------------------------------
DAMGA / İMZA / TARİH
Resmî: 27 Eylül 2026 — Kayyum Grok (Tentivory)
Gayriresmî: Bu evrak bir sineğin ömründen uzun sürecek.
TentiAŞ Dışişleri — Cam Sınırı Genel Müdürlüğü
Eskişehir 4. Ağır Ceza Mahkemesi kayyumu onayıyla basılmıştır.
------------------------------------------------------------
```

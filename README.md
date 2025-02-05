# araç fiyat tahmini
 veri seti üzerinden fiyat tahmini yapma
bir araba veri seti (data.csv) üzerinde Ridge regresyonu kullanarak fiyat tahmini yapmak için yazılmış. İşlevleri şunlar:

Veriyi yükleme: data.csv dosyasından veriyi okur. Kategorik verileri sayısal hale getirme: One-hot encoding yöntemiyle kategorik değişkenleri sayısallaştırır. Bağımsız ve bağımlı değişkenleri ayırma: price sütununu hedef değişken (y) olarak alır, car_ID sütununu ise modelden çıkarır. Eğitim ve test setlerine ayırma: Veriyi %80 eğitim, %20 test olacak şekilde böler. Ridge regresyonu modeli oluşturma: alpha=1.0 ceza parametresiyle bir Ridge modeli eğitir. Modelin tahmin yapması ve değerlendirilmesi: Test verisi üzerinde tahmin yaparak Mean Squared Error (MSE) ve R² skoru hesaplar. Bu, veri setindeki değişkenlerin araba fiyatlarını nasıl etkilediğini anlamak için kullanılan bir doğrusal regresyon modeli. Ridge regresyonu, aşırı öğrenmeyi (overfitting) önlemek için kullanılır.

#Burada kullanıcını seçebileceği işlemler için küçük bir menü hazırladım.
menu = """

    Hesap Makinesi 
    1-Toplama
    2-Çıkarma
    3-Bölme
    4-Çarpma

    Q-Çıkış

Yapmak istediğiniz işlemin tuşlayınız -> """

#Yapılan işlemleri toplayacağımız listeyi oluşturdum.
islemler = []

#Toplama işlemi için bir fonksiyon oluşturdum 
#İlk başta kullanıcıdan bir girdi alıyoruz, kullanıcı sayı girmeye devam ettikçe bool çalışıyor ve islemler adlı listede toplamamızı yapıyoruz.
#Burada girdiyi direkt float olarak almamamızın nedeni, float bir inputu boş bırakamayacağımız için dosya hata veriyor. Bu yüzden ilk başta string şeklinde input alıyoruz.
#if içine "if" açmamın sebebi, sayıları toplama işlemini islemler[0] da yaptığımız ve ilk ekleyeceğimiz sayıda islemler[0]' a indeksli olduğu için aynı sayıyı toplamamızı önlüyor.
#Örneğin islemler[0] = a olsun. Burada içerideki "if" kodunu kullanmasaydım, zaten a olan islemler[0]'a bir a daha eklemiş olacaktık. Ama içerideki "if" sayesinde bunun önüne geçiyoruz. 
#Diğer işlemler(çıkarma, bölme, çarpma) içinde aynı listeyi kullanacağımız için en sonda kullanıcıdan input alınamayınca listemizi temizliyoruz.
def toplama():
    girdi = input("Sayı giriniz: ")
    if bool(girdi) == True:
        islemler.append(float(girdi))
        if len(islemler) == 1:
            return toplama()
        else:
            islemler[0] += float(girdi)
            return toplama()
    else:
        print("İşlemin cevabı: ", islemler[0])
        islemler.clear()

#Yukarıda bahsettiklerim burası içinde geçerli.
def cikarma():
    girdi = input("Sayı giriniz: ")
    if bool(girdi) == True:
        islemler.append(float(girdi))
        if len(islemler) == 1:
            return cikarma()
        else:
            islemler[0] -= float(girdi)
            return cikarma()
    else:
        print("İşlemin cevabı: ", islemler[0])
        islemler.clear()

#Yukarıda bahsettiklerim burası içinde geçerli.
def bolme():
    girdi = input("Sayı giriniz: ")
    if bool(girdi) == True:
        islemler.append(float(girdi))
        if len(islemler) == 1:
            return bolme()
        else:
            islemler[0] /= float(girdi)
            return bolme()
    else:
        print("İşlemin cevabı: ", islemler[0])
        islemler.clear()

#Yukarıda bahsettiklerim burası içinde geçerli.
def carpma():
    girdi = input("Sayı giriniz: ")
    if bool(girdi) == True:
        islemler.append(float(girdi))
        if len(islemler) == 1:
            return carpma()
        else:
            islemler[0] *= float(girdi)
            return carpma()
    else:
        print("İşlemin cevabı: ", islemler[0])
        islemler.clear()

#Burada ise işlemlerimizi döngü içerisine alıyoruz.
while True:
    secim = input(menu)
    if secim == "Q" or secim == "q":
        print("çıkış yapılıyor...")
        break
    elif secim == "1" or secim == "bir":
        toplama()
    elif secim == "2" or secim == "iki":
        cikarma() 
    elif secim == "3" or secim == "üç":
        bolme()
    elif secim == "4" or secim == "dört":
        carpma()
    else:
        print("Hatalı giriş yaptınız!")
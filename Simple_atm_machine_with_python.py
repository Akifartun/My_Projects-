print("""
********************
ATM Makinesine Hoşgeldiniz...

Öncelikle Kullanıcı Adınızı ve Şifrenizi Giriniz...

******************** 
""")

sys_kullanıcı_adı = "user"
sys_kullanıcı_şifre = "password"
giriş_hakkı = 3
bakiye = 100

while True:
    kullanıcı_adı = input("Kullanıcı Adınızı Giriniz:")
    kullanıcı_şifre = input("Parolanızı Giriniz:")
    if kullanıcı_adı != sys_kullanıcı_adı and kullanıcı_şifre == sys_kullanıcı_şifre:
        print("Kullanıcı Adı Hatalı.")
        giriş_hakkı -= 1
    elif kullanıcı_adı == sys_kullanıcı_adı and kullanıcı_şifre != sys_kullanıcı_şifre:
        print("Şifre Hatalı.")
        giriş_hakkı -= 1
    elif kullanıcı_adı != sys_kullanıcı_adı and kullanıcı_şifre != sys_kullanıcı_şifre:
        print("Kullanıcı Adı ve Şifre Hatalı.")
        giriş_hakkı -= 1
    else:
        print("Sisteme Başarı İle Giriş Yaptınız...")


        while True:
            print("""
            ********************
            Kullanıcı adı ve Şifrenizi Doğru Girdiniz...
            Teşekkürler...
    
            İşlemler; 
    
            1.Bakiye Sorgulama 
    
            2.Para Yatırma 
    
            3.Para Çekme 
    
            Programdan Çıkmak için 'q' Tuşuna Basınız.
    
    
            ********************
            """)

            kullanıcı_girişi = input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz.(Çıkmak İçin 'q' Tuşuna Basınız):")
            if kullanıcı_girişi == "q":
                print("Bizi Tercih Ettiğiniz İçin Teşekkür Ederiz...")
                break
            elif kullanıcı_girişi == "1":
                print("""İşleminiz Alınıyor...
                             Lütfen Bekleyiniz...""")
                print("Bakiyeniz:{}".format(bakiye))
                çıkış = input("Çıkmak İçin 'q' Geri Dönmek İçin 'b' Tuşuna Basınız.")
                if çıkış == "q":
                    print("Bizi Tercih Ettiğiniz İçin Teşekkür Ederiz...")
                    break
                elif çıkış == "b":
                    print("Ana Sayfaya Yönlendiriliyorsunuz...")
                    continue
            elif kullanıcı_girişi == "2":
                print("""İşleminiz Alınıyor...
                             Lütfen Bekleyiniz...""")
                yatırılacak_tutar = int(input("Lütfen Yatırmak İstediğiniz Tutarı Giriniz:"))
                bakiye = bakiye + yatırılacak_tutar
                print("Yeni bakiyeniz:{}. İyi Günlerde Kullanınız...".format(bakiye))
                çıkış = input("Çıkmak İçin 'q' Geri Dönmek İçin 'b' Tuşuna Basınız.")
                if çıkış == "q":
                    print("Bizi Tercih Ettiğiniz İçin Teşekkür Ederiz...")
                    break
                elif çıkış == "b":
                    print("Ana Sayfaya Yönlendiriliyorsunuz...")++
                    continue
            elif kullanıcı_girişi == "3":
                print("""İşleminiz Alınıyor...
                                     Lütfen Bekleyiniz...""")
                çekilecek_tutar = int(input("Lütfen Çekmek İstediğiniz Tutarı Giriniz:"))
                if (bakiye - çekilecek_tutar < 0):
                    print("Bu Kadar Para Çekemezsiniz...\nLütfen Yeniden Deneyiniz...")
                    continue
                bakiye = bakiye - çekilecek_tutar
                print("Yeni bakiyeniz:{}".format(bakiye))
                çıkış = input("Çıkmak İçin 'q' Geri Dönmek İçin 'b' Tuşuna Basınız.")
                if çıkış == "q":
                    print("Bizi Tercih Ettiğiniz İçin Teşekkür Ederiz...")
                    break
                elif çıkış == "b":
                    print("Ana Sayfaya Yönlendiriliyorsunuz...")
                    continue
            else:
                print("Lütfen Doğru Değeri Giriniz...")
                continue
        break
    if giriş_hakkı == 0:
        print("Giriş Hakkınız Kalmadı Sistemden Ayrılıyorsunuz...")
        break

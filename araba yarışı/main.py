import pygame
import math



# Renkler
siyah = (0, 0, 0)
beyaz = (255, 255, 255)
kirmizi = (255, 0, 0)
yesil = (0, 255, 0)
mavi = (0, 0, 255)
ciyan = (0, 255, 255)
gri = (128, 128, 128)
sari = (255, 255, 0)
pembe = (255, 0, 255)
gumus = (192, 192, 192)

# Pygame kütüphanesini başlatma
pygame.init()


# Oyun ekranını oluşturma
screen = pygame.display.set_mode((800, 600))

# Oyunun İsmi ve Resmi
pygame.display.set_caption("Araba Yarışı")
icon = pygame.image.load('sport-car.png')
pygame.display.set_icon(icon)


# Oyunun başlangıç modu (edite ve run)
game_mode = 'edite'

# Oyunun düzenleme modundaki başlangıç durumu
game_state = 'serbest'


# Araba sınıfı
class araba:
    def __init__(self, merkezx, merkezy):
        aci1 = 148
        aci2 = 212
        aci3 = 328
        aci4 = 32
        self.a = merkezx + (23.58 * math.cos(math.radians(aci1 + aci)))
        self.b = merkezy + (23.58 * math.sin(math.radians(aci1 + aci)))
        self.c = merkezx + (23.58 * math.cos(math.radians(aci2 + aci)))
        self.d = merkezy + (23.58 * math.sin(math.radians(aci2 + aci)))
        self.e = merkezx + (23.58 * math.cos(math.radians(aci3 + aci)))
        self.f = merkezy + (23.58 * math.sin(math.radians(aci3 + aci)))
        self.g = merkezx + (23.58 * math.cos(math.radians(aci4 + aci)))
        self.h = merkezy + (23.58 * math.sin(math.radians(aci4 + aci)))

    def Araba_koy(self):
        pygame.draw.line(screen, kirmizi, (self.a, self.b), (self.c, self.d), 3)
        pygame.draw.line(screen, kirmizi, (self.c, self.d), (self.e, self.f), 3)
        pygame.draw.line(screen, kirmizi, (self.e, self.f), (self.g, self.h), 3)
        pygame.draw.line(screen, kirmizi, (self.g, self.h), (self.a, self.b), 3)

# Araba Değerleri
araba_koordinati = 0
merkezX = 1000
merkezY = 1000
hiz = 0
aci = 0
arabaX_degisimi = hiz*math.cos(math.radians(aci))
arabaY_degisimi = hiz*math.sin(math.radians(aci))

# Button ve bilgilendirici yazı sınıfı
class button:

    def __init__(self, konumx, konumy, buyuklukx, buyukluky, yazi ):
        self.b = konumx
        self.c = konumy
        self.d = buyuklukx
        self.e = buyukluky
        self.f = yazi

    def button_olustur(self):
        pygame.draw.line(screen, gumus, (self.b, self.c), (self.b + self.d, self.c), 3)
        pygame.draw.line(screen, gumus, (self.b + self.d, self.c), (self.b + self.d, self.c + self.e), 3)
        pygame.draw.line(screen, gumus, (self.b + self.d, self.c + self.e), (self.b, self.c + self.e), 3)
        pygame.draw.line(screen, gumus, (self.b, self.c + self.e), (self.b, self.c), 3)
        button_yazi_font = pygame.font.SysFont('Arial', 15)
        button_yazi = button_yazi_font.render(self.f, True, siyah)
        screen.blit(button_yazi, (self.b + 20, self.c + 10))

    def buttona_araba_koy(self):
        pygame.draw.line(screen, kirmizi, (self.b + 50, self.c + 45), (self.b + 100, self.c + 45), 3)
        pygame.draw.line(screen, kirmizi, (self.b + 100, self.c + 45), (self.b + 100, self.c + 75), 3)
        pygame.draw.line(screen, kirmizi, (self.b + 100, self.c + 75), (self.b + 50, self.c + 75), 3)
        pygame.draw.line(screen, kirmizi, (self.b + 50, self.c + 75), (self.b + 50, self.c + 45), 3)

    def buttona_yol_koy(self):
        pygame.draw.line(screen, mavi, (self.b + 20, self.c + 80), (self.b + 130, self.c + 30), 3)
        pygame.draw.circle(screen, kirmizi, (self.b + 20, self.c + 80), 3)
        pygame.draw.circle(screen, kirmizi, (self.b + 130, self.c + 30), 3)
        pygame.draw.circle(screen, kirmizi, (self.b + 75, self.c + 55), 3)





# Yol sınıfı

yolX_bit = 0
yolY_bit = 0
yol = []
b = 0
yolX_baslangic = []
yolY_baslangic = []
yolX_bitis = []
yolY_bitis = []
class Yol:

    # Yol ile ilgili parametreler


    yol_sayisi = 0
    def __init__(self, yol_numarasi,  yolX_baslangic, yolY_baslangic, yolX_bitis, yolY_bitis):
        self.a = yol_numarasi
        self.x = yolX_baslangic
        self.y = yolY_baslangic
        self.z = yolX_bitis
        self.d = yolY_bitis
    yol_sayisi += 1


    # Yol koyma fonksiyonu
    def Yol_koy(self):
        pygame.draw.line(screen, mavi, (self.x, self.y), (self.z, self.d), 5)
        pygame.draw.circle(screen, kirmizi, (self.x, self.y), 5)
        pygame.draw.circle(screen, kirmizi, (self.z, self.d), 5)
        pygame.draw.circle(screen, kirmizi, ((self.x + self.z)/2, (self.y + self.d)/2), 5)

    # Yol silme fonksiyonu (uzaklık hesabı ile)
    def yol_uzaklik(self, g, h):
        b = 1000
        # 1. bölge
        if (self.x < self.z) and (self.y < self.d):
            if (self.x <= mouse[0] <= self.z) and (self.y <= mouse[1] <= self.d):
                b = 1
        # 2. bölge
        if (self.x > self.z) and (self.y < self.d):
            if (self.z <= mouse[0] <= self.x) and (self.y <= mouse[1] <= self.d):
                b = 1
        # 3. bölge
        if (self.x > self.z) and (self.y > self.d):
            if (self.z <= mouse[0] <= self.x) and (self.d <= mouse[1] <= self.y):
                b = 1
        # 4. bölge
        if (self.x < self.z) and (self.y > self.d):
            if (self.x <= mouse[0] <= self.z) and (self.d <= mouse[1] <= self.y):
                b = 1
        m = (self.d * 1.000001 - self.y) / (self.z * 1.000001 - self.x)
        c = self.d - m * self.z
        uzaklik = b * abs((h - m * g - c) / math.sqrt(1 + m * m))
        return uzaklik












# Oyun Döngüsü
running = True
while running:

    # RGB >> RED,GREEN,BLUE (Arka plan rengini kırmızı, yeşil, mavi renklerinin karışımından yararlanarak ayarlama)
    screen.fill((250, 100, 200))

    # Edit modu etkinken gerçekleşen olaylar

    if game_mode == 'edite':

        # Edit modunda ekrana gelen bilgilendirici yazılar
        bilgilendirme_font = pygame.font.SysFont('Arial', 25)
        bilgilendirme_yazisi1 = bilgilendirme_font.render('Araba Sürme Moduna Geçmek İçin R Tuşuna Basın', True, ciyan)
        bilgilendirme_yazisi2 = bilgilendirme_font.render('Düzenleme Moduna Geçmek İçin E Tuşuna Basın', True, ciyan)
        screen.blit (bilgilendirme_yazisi1, (20, 550))

        # Araba Koyma Butonu
        araba_button = button(640, 10, 150, 100, 'ARABA')
        araba_button.button_olustur()
        araba_button.buttona_araba_koy()

        # Yol Koyma Butonu
        yol_button = button(480, 10, 150, 100, 'YOL')
        yol_button.button_olustur()
        yol_button.buttona_yol_koy()


        # Edit modunda Klavye ve Fare kullanıldığında gerçekleşen olaylar
        for event in pygame.event.get():

            # Oyunu kapatma
            if event.type == pygame.QUIT:
                running = False


            # Mouse ile ekranda bir yere tıklanıldığı zaman gerçekleşen olaylar
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()

                # Sol Tık
                if event.button == 1:

                    # Araba koyma butonuna tıklanılması
                    if (640 <= mouse[0] <= 790) and (10 <= mouse[1] <= 110):
                        game_state = 'araba koyma'

                    # Yol koyma butonuna tıklanılması
                    elif (480 <= mouse[0] <= 630) and (10 <= mouse[1] <= 110):
                        game_state = 'yol koyma'

                    # Arabayı koymak istediğimiz lokasyon
                    elif game_state == 'araba koyma':
                        merkezX = mouse[0]
                        merkezY = mouse[1]

                    # İstediğimiz kadar yolu istediğimiz yerlerde oluşturmak
                    elif game_state == 'yol koyma 2':
                        yol[b-1] = Yol(b-1, yolX_bit, yolY_bit, mouse[0], mouse[1])
                        game_state = 'yol koyma 3'



                    # Yolun başlangıcını belirlemek
                    elif game_state == 'yol koyma' or game_state == 'yol koyma 3':
                        yol.append(Yol(b, yolX_bit, yolY_bit, mouse[0], mouse[1]))
                        b += 1
                        yolX_bit = mouse[0]
                        yolY_bit = mouse[1]
                        game_state = 'yol koyma 2'

                # Sağ Tık
                if event.button == 3:

                    # Araba silme
                    if ((merkezX - 20) <= mouse[0] <= (merkezX + 20)) and ((merkezY - 12.5) <= mouse[1] <= (merkezY + 12.5)):
                        merkezX = 1000
                        merkezY = 1000

                    # Yol silme
                    else:
                        for i in range(b):
                            if (yol[i].yol_uzaklik(mouse[0], mouse[1]) <= 20):
                                yol[i] = Yol(i, 1000, 999, 900, 1001)



            # Run moduna geçme
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_mode = 'run'

    # Run modunda gerçekleşen olaylar
    if game_mode == 'run':

        # Run modunda ekrana gelen bilgilendirici yazılar
        bilgilendirme_font = pygame.font.SysFont('Arial', 25)
        bilgilendirme_yazisi2 = bilgilendirme_font.render('Düzenleme Moduna Geçmek İçin E Tuşuna Basın', True, ciyan)
        screen.blit(bilgilendirme_yazisi2, (20, 10))


        # Yol Koyma sırasında run moduna geçilirse ekranda tamamlanmamış yol gözükmemesi için bir koşul
        if game_state == 'yol koyma 2':
            game_state = 'yol koyma'



        # Araba hareket mekanikleri
        pressed = pygame.key.get_pressed()

        # Hızlanma hareketi
        if pressed[pygame.K_UP]:
            hiz += 0.001

        # Yavaşlama hareketi
        if pressed[pygame.K_DOWN]:
            hiz -= 0.002

        # Sola dönme hareketi
        if pressed[pygame.K_LEFT]:
            aci -= 18/50

        # Sağa dönme hareketi
        if pressed[pygame.K_RIGHT]:
            aci += 18/50

        # Hız sınırlayıcı
        if hiz > 0.8:
            hiz = 0.8
        if hiz < -0.4:
            hiz = -0.4



        # Oyunu kapatma ve Edit Moduna geçme
        for event in pygame.event.get():

            # Oyunu kapatma
            if event.type == pygame.QUIT:
                running = False

            # Edit moduna geçme
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    game_mode = 'edite'












    # Yolu çizdirme

    if game_state == 'yol koyma 2':
        mouse2 = pygame.mouse.get_pos()
        yol[b-1] = Yol(b-1, yolX_bit, yolY_bit, mouse2[0], mouse2[1])
        yol[b-1].Yol_koy()


    if game_state == 'yol koyma 3' or game_state == 'araba koyma' or game_state == 'yol koyma 2':
            for j in range(b):
                yol[j].Yol_koy()

            # print(yol_uzaklik(j, 0, 0))

    # Araba çizdirme
    arabaX_degisimi = hiz * math.cos(math.radians(aci))
    arabaY_degisimi = hiz * math.sin(math.radians(aci))
    merkezX += arabaX_degisimi
    merkezY += arabaY_degisimi
    if merkezX == 1000:
        merkezX = 1000
    elif (merkezX < 20):
        merkezX = 20
    elif (merkezX > 780):
        merkezX = 780
    if merkezY == 1000:
        merkezY = 1000
    elif (merkezY > 587.5):
        merkezY = 587.5
    elif (merkezY < 12.5):
        merkezY = 12.5

    araba_konumu = araba(merkezX, merkezY)
    araba_konumu.Araba_koy()

    # Ekranı sürekli günceller
    pygame.display.update()


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


# Araba Değerleri
araba_koordinati = 0
merkezX = 1000
merkezY = 1000
hiz = 0
aci = 0
arabaX_degisimi = hiz*math.cos(math.radians(aci))
arabaY_degisimi = hiz*math.sin(math.radians(aci))

# Yol ile ilgili parametreler
yol = []
yolX_baslangic = []
yolY_baslangic = []
yolX_bitis = []
yolY_bitis = []
yolX_bit = 0
yolY_bit = 0
yol_sayisi = 0

# Araba koyma ve Yer değiştirme fonksiyonu
def Araba_koy(merkezx, merkezy):
    aci1 = 148
    aci2 = 212
    aci3 = 328
    aci4 = 32
    a = merkezx + (23.58 * math.cos(math.radians(aci1 + aci)))
    b = merkezy + (23.58 * math.sin(math.radians(aci1 + aci)))
    c = merkezx + (23.58 * math.cos(math.radians(aci2 + aci)))
    d = merkezy + (23.58 * math.sin(math.radians(aci2 + aci)))
    e = merkezx + (23.58 * math.cos(math.radians(aci3 + aci)))
    f = merkezy + (23.58 * math.sin(math.radians(aci3 + aci)))
    g = merkezx + (23.58 * math.cos(math.radians(aci4 + aci)))
    h = merkezy + (23.58 * math.sin(math.radians(aci4 + aci)))
    pygame.draw.polygon(screen, kirmizi, [(a, b), (c, d), (e, f), (g, h)], 3)

# Yol koyma fonksiyonu

def Yol_koy(x, y, z, d):
    pygame.draw.line(screen, mavi, (x, y), (z, d), 5)

def Daire_koy(x, y):
    pygame.draw.circle(screen, kirmizi, (x, y), 5)

# Yol silme fonksiyonu
def yol_uzaklik(a, x, y):
    b = 1000
    # 1. bölge
    if (yolX_baslangic[a] < yolX_bitis[a]) and (yolY_baslangic[a] < yolY_bitis[a]):
        if (yolX_baslangic[a] <= mouse[0] <= yolX_bitis[a]) and (yolY_baslangic[a] <= mouse[1] <= yolY_bitis[a]):
            b = 1
    # 2. bölge
    if (yolX_baslangic[a] > yolX_bitis[a]) and (yolY_baslangic[a] < yolY_bitis[a]):
        if (yolX_bitis[a] <= mouse[0] <= yolX_baslangic[a]) and (yolY_baslangic[a] <= mouse[1] <= yolY_bitis[a]):
            b = 1
    # 3. bölge
    if (yolX_baslangic[a] > yolX_bitis[a]) and (yolY_baslangic[a] > yolY_bitis[a]):
        if (yolX_bitis[a] <= mouse[0] <= yolX_baslangic[a]) and (yolY_bitis[a] <= mouse[1] <= yolY_baslangic[a]):
            b = 1
    # 4. bölge
    if (yolX_baslangic[a] < yolX_bitis[a]) and (yolY_baslangic[a] > yolY_bitis[a]):
        if (yolX_baslangic[a] <= mouse[0] <= yolX_bitis[a]) and (yolY_bitis[a] <= mouse[1] <= yolY_baslangic[a]):
            b = 1
    m = (yolY_bitis[a] * 1.000001 - yolY_baslangic[a]) / (yolX_bitis[a] * 1.000001 - yolX_baslangic[a])
    c = yolY_bitis[a] - m * yolX_bitis[a]
    uzaklik = b*abs((y - m * x - c) / math.sqrt(1 + m * m))
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
        pygame.draw.rect(screen, gumus, [640, 10, 150, 100])
        araba_button_yazi_font = pygame.font.SysFont('Arial', 15)
        araba_button_yazi = araba_button_yazi_font.render('Araba', True, siyah)
        screen.blit(araba_button_yazi, (660, 20))
        pygame.draw.rect(screen, kirmizi, (690, 55, 50, 30), 3)

        # Yol Koyma Butonu
        pygame.draw.rect(screen, gumus, [480, 10, 150, 100])
        yol_button_yazi_font = pygame.font.SysFont('Arial', 15)
        yol_button_yazi = yol_button_yazi_font.render('Yol', True, siyah)
        screen.blit(yol_button_yazi, (510, 20))
        pygame.draw.aaline(screen, mavi, (500, 90), (610, 40), 50)
        pygame.draw.circle(screen, kirmizi, (500, 90), 3)
        pygame.draw.circle(screen, kirmizi, (610, 40), 3)
        pygame.draw.circle(screen, kirmizi, (555, 65), 3)

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
                        pygame.draw.rect(screen, mavi, [640, 10, 150, 100])
                        araba_button_yazi_font = pygame.font.SysFont('Arial', 15)
                        araba_button_yazi = araba_button_yazi_font.render('Araba', True, kirmizi)
                        screen.blit(araba_button_yazi, (660, 20))
                        pygame.draw.rect(screen, yesil, (690, 55, 50, 30), 1)
                        game_state = 'araba koyma'

                    # Yol koyma butonuna tıklanılması
                    elif (480 <= mouse[0] <= 630) and (10 <= mouse[1] <= 110):
                        pygame.draw.rect(screen, mavi, [480, 10, 150, 100])
                        yol_button_yazi_font = pygame.font.SysFont('Arial', 15)
                        yol_button_yazi = yol_button_yazi_font.render('Yol', True, kirmizi)
                        screen.blit(yol_button_yazi, (510, 20))
                        pygame.draw.aaline(screen, yesil, (500, 90), (610, 40))
                        pygame.draw.circle(screen, gri, (500, 90), 3)
                        pygame.draw.circle(screen, gri, (610, 40), 3)
                        pygame.draw.circle(screen, gri, (555, 65), 3)
                        game_state = 'yol koyma'

                    # Arabayı koymak istediğimiz lokasyon
                    elif game_state == 'araba koyma':
                        merkezX = mouse[0]
                        merkezY = mouse[1]

                    # İstediğimiz kadar yolu istediğimiz yerlerde oluşturmak
                    elif game_state == 'yol koyma 2':
                        yol_sayisi += 1
                        yolX_baslangic.append(yolX_bit)
                        yolY_baslangic.append(yolY_bit)
                        yolX_bitis.append(mouse[0])
                        yolY_bitis.append(mouse[1])
                        game_state = 'yol koyma 3'

                    # Yolun başlangıcını belirlemek
                    elif game_state == 'yol koyma' or game_state == 'yol koyma 3':
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
                        for i in range(yol_sayisi):
                            if (yol_uzaklik(i, mouse[0], mouse[1]) <= 20):
                                yolX_baslangic[i] = 1000
                                yolY_baslangic[i] = 999
                                yolX_bitis[i] = 900
                                yolY_bitis[i] = 1001


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
        Yol_koy(yolX_bit, yolY_bit, mouse2[0], mouse2[1])
        Daire_koy(yolX_bit, yolY_bit)
        Daire_koy(mouse2[0], mouse2[1])
        Daire_koy((yolX_bit + mouse2[0])/2, (yolY_bit + mouse2[1])/2)

    if game_state == 'yol koyma 3' or game_state == 'araba koyma' or 'yol koyma 2':
        for j in range(yol_sayisi):
            Yol_koy(yolX_baslangic[j], yolY_baslangic[j], yolX_bitis[j], yolY_bitis[j])
            Daire_koy(yolX_baslangic[j], yolY_baslangic[j])
            Daire_koy(yolX_bitis[j], yolY_bitis[j])
            Daire_koy((yolX_baslangic[j] + yolX_bitis[j])/2, (yolY_baslangic[j] + yolY_bitis[j])/2)
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
    Araba_koy(merkezX, merkezY)

    # Ekranı sürekli günceller
    pygame.display.update()


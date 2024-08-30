import time
import pygame as pg
import random
import settings

dnotaf = pg.image.load("dlinainotaf.png")
dnotaf = pg.transform.scale(dnotaf, [100, 200])

dnota = pg.image.load("dlinainota.png")
dnota = pg.transform.scale(dnota, [100, 200])

knotaf = pg.image.load("korotkainotaf.png")
knotaf = pg.transform.scale(knotaf, [100, 100])

knota = pg.image.load("korotkainota.png")
knota = pg.transform.scale(knota, [100, 100])


class Noti:
    def __init__(self, koordinati, dlitelnost, nazvanie, nomer):
        self.dlitelnost = dlitelnost
        if dlitelnost == 1:
            self.kartinka = knota
        else:
            self.kartinka = dnota
        self.zvyk = pg.mixer.Sound("Sounds/" + nazvanie + ".ogg")
        self.nazvanie = nazvanie
        self.nomer = nomer
        shirina = self.kartinka.get_width()
        visota = self.kartinka.get_height()
        self.hitbox = pg.Rect(koordinati, [shirina, visota])
        self.nachatie = 0

    def click(self):
        pg.mixer.stop()
        a = pg.mixer.find_channel()
        if a != None:
            a.queue(self.zvyk)
        else:
            pg.mixer.stop()
        self.zvyk.play()
        if self.dlitelnost == 1:
            self.kartinka = knotaf
        else:
            self.kartinka = dnotaf
        self.nachatie = 1

    def otrisovka(self, okno):
        okno.blit(self.kartinka, self.hitbox)

    def dvishenie(self):
        self.hitbox.y = self.hitbox.y + 2


class Pesnia:
    def __init__(self, nazvanya, dlitelnosti):
        self.nazvanya = nazvanya
        self.dlitelnosti = dlitelnosti
        self.noti = []
        self.tekysheevremy = 0
        self.vremysozdania = 0
        self.a = 0

    def sozdanienot(self):
        self.tekysheevremy = pg.time.get_ticks()
        if self.tekysheevremy - self.vremysozdania >= 700 and self.a < len(self.nazvanya):
            a = Noti([random.randint(0, settings.POLOSKI - 1) * 100, 0], self.dlitelnosti[self.a], self.nazvanya[self.a], self.a)
            self.a = self.a + 1
            self.noti.append(a)
            self.vremysozdania = pg.time.get_ticks()

    def otrisovka(self, okno):
        for nota in self.noti:
            nota.otrisovka(okno)

    def dvishenie(self):
        for nota in self.noti:
            nota.dvishenie()

    def najatie(self, nomer):
        dotekyjey = self.noti[0:nomer]
        a = 0
        for nota in dotekyjey:
            if nota.nachatie == 1:
                a = a + 1
        if a == len(dotekyjey):
            return True
        else:
            return False
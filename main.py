import time
import pygame as pg
import random
import settings
import sprites
import menu
import pygame.freetype

pg.init()
pg.mixer.init(channels=10)

shrift = pygame.freetype.Font("shrift.otf", 25)


class Igra:
    def __init__(self):
        self.okno = pg.display.set_mode(settings.SIZE)
        self.chikl = 0
        self.pesnia = sprites.Pesnia(settings.BIRCH_NOTES, settings.BIRCH_DURATION)
        self.chasi = pg.time.Clock()
        self.menu = menu.Menu(self)
        self.igraormune = 2
        self.flak = 0

    def otrisovka(self):
        self.okno.fill([255, 255, 255])
        a = 0
        b = 0
        if self.flak == 0:
            self.pesnia.otrisovka(self.okno)
        else:
            shrift.render_to(self.okno, [150, 300], "Вы проиграли", settings.CHERNIY)
        while settings.POLOSKI != a:
            b = b + settings.SHIRINAPOLOSOK
            a = a + 1
            pg.draw.line(self.okno, [0, 0, 0], [b, 0], [b, settings.SIZE[1]])
        if self.pesnia.a == len(self.pesnia.nazvanya) and self.pesnia.noti[-1].hitbox.y > settings.SIZE[1]:
            shrift.render_to(self.okno, [150, 300], "Вы выиграли", settings.CHERNIY)
        pg.display.update()

    def logika(self):
        if self.flak == 0:
            self.pesnia.sozdanienot()
            self.pesnia.dvishenie()
        for nota in self.pesnia.noti:
            if nota.hitbox.y >= 600 and nota.nachatie == 0:
                self.flak = 1

    def sobitia(self):
        sobitia = pg.event.get()
        for sobitya in sobitia:
            if sobitya.type == pg.QUIT:
                self.chikl = self.chikl + 1
            if sobitya.type == pg.MOUSEBUTTONDOWN:
                for nota in self.pesnia.noti:
                    if nota.hitbox.collidepoint(sobitya.pos) is True:
                        nota.click()
                        j = self.pesnia.najatie(nota.nomer)
                        if j is True:
                            print("МОЛОДЕЦ")
                        else:
                            self.flak = 1
                            print("ВСЁ ПЛОХО :(")
            if sobitya.type == pg.KEYDOWN:
                if sobitya.key == pg.K_ESCAPE:
                    self.igraormune = 2
                    self.flak = 0

    def vseovmeste(self):
        while self.chikl == 0:
            if self.igraormune == 1:
                self.otrisovka()
                self.logika()
                self.sobitia()
            else:
                self.menu.otrisovka()
                self.menu.logika()
                self.menu.sobitia()
            self.chasi.tick(144)


b = Igra()
b.vseovmeste()

import pygame as pg
import settings
import pygame.freetype
import sprites
pygame.init()

shrift = pygame.freetype.Font("shrift.otf", 25)


class Menu:
    def __init__(self, igrylka):
        self.igrylka = igrylka
        self.kartinka = pg.image.load("menu.png")
        self.kartinka = pg.transform.scale(self.kartinka, settings.SIZE)
        self.chevt1 = settings.CINIY
        self.chvet2 = settings.CHERNIY
        self.chvet3 = settings.CHERNIY
        self.nomer = 1

    def otrisovka(self):
        self.igrylka.okno.blit(self.kartinka, [0, 0])
        shrift.render_to(self.igrylka.okno, [0, 0], "В лесу родилась ёлочка", self.chevt1)
        shrift.render_to(self.igrylka.okno, [0, 100], "Берёза", self.chvet2)
        shrift.render_to(self.igrylka.okno, [0, 200], "Утро", self.chvet3)
        pg.display.update()

    def sobitia(self):
        sobitia = pg.event.get()
        for sobitya in sobitia:
            if sobitya.type == pg.QUIT:
                self.chikl = self.chikl + 1
            if sobitya.type == pg.KEYDOWN:
                if sobitya.key == pg.K_DOWN:
                    if self.nomer == 1:
                        self.chevt1 = settings.CHERNIY
                        self.chvet2 = settings.CINIY
                        self.nomer = self.nomer + 1
                    elif self.nomer == 2:
                        self.chvet2 = settings.CHERNIY
                        self.chvet3 = settings.CINIY
                        self.nomer = self.nomer + 1
                    elif self.nomer == 3:
                        self.chvet3 = settings.CHERNIY
                        self.chevt1 = settings.CINIY
                        self.nomer = 1
                elif sobitya.key == pg.K_UP:
                    if self.nomer == 1:
                        self.chevt1 = settings.CHERNIY
                        self.chvet3 = settings.CINIY
                        self.nomer = 3
                    elif self.nomer == 3:
                        self.chvet3 = settings.CHERNIY
                        self.chvet2 = settings.CINIY
                        self.nomer = 2
                    elif self.nomer == 2:
                        self.chvet2 = settings.CHERNIY
                        self.chevt1 = settings.CINIY
                        self.nomer = 1
                elif sobitya.key == pg.K_RETURN:
                    self.igrylka.igraormune = 1
                    if self.nomer == 1:
                        self.igrylka.pesnia = sprites.Pesnia(settings.CHRISTMAS_TREE_NOTES, settings.CHRISTMAS_TREE_DURATION) 
                    elif self.nomer == 2:
                        self.igrylka.pesnia = sprites.Pesnia(settings.BIRCH_NOTES, settings.BIRCH_DURATION)
                    elif self.nomer == 3:
                        self.igrylka.pesnia = sprites.Pesnia(settings.MORNING_NOTES, settings.MORNING_DURATION)

    def logika(self):
        pass

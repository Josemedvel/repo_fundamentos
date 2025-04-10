import time
import pygame


pygame.init()

class Escopeta:
    def __init__(self, danno_por_perd, tiempo_entre_disp, municion_max, alcance_max, tiempo_recarga_perd, archivo_disparo, archivo_aftershot, precio):
        self.danno_por_perd = danno_por_perd
        self.tiempo_entre_disp = tiempo_entre_disp
        self.municion_max = municion_max
        self.alcance_max = alcance_max
        self.municion_actual = self.municion_max
        self.tiempo_recarga_perd = tiempo_recarga_perd
        self.shot_sound = pygame.mixer.Sound(archivo_disparo)
        self.aftershot_sound = pygame.mixer.Sound(archivo_aftershot)
        self.precio = precio

    def disparar(self):
        if self.municion_actual > 0:
            print("PUMMMMMMMM")
            pygame.mixer.Sound.play(self.shot_sound)
            pygame.mixer.music.stop()
            self.municion_actual = self.municion_actual - 1
            self.esperar_entre_disparos()

    def esperar_entre_disparos(self):
        pygame.mixer.Sound.play(self.aftershot_sound)
        pygame.mixer.music.stop()
        time.sleep(self.tiempo_entre_disp)

    def vaciar_cargador(self):
        while self.municion_actual > 0:
            self.disparar()

    def recargar(self):
        while self.municion_actual < self.municion_max:
            print("METO UN CARTUCHO")
            self.municion_actual = self.municion_actual + 1
            pygame.mixer.Sound.play(self.aftershot_sound)
            pygame.mixer.music.stop()
            time.sleep(self.tiempo_recarga_perd)

class Spas_12(Escopeta):
    def __init__(self):
        super().__init__(12, 0.5, 12, 50, 0.2,"SHOT.WAV", "SHOTGUN_AFT_SHOT.WAV", 1200)

class DobleCannonDoom(Escopeta):
    def __init__(self):
        super().__init__(50, 1, 2, 30, 0.75,"doom_shot.wav", "doom_aft_shot.wav", 2000)

    def disparar(self):
        if self.municion_actual > 0:
            print("PUMMMMMMMM")
            pygame.mixer.Sound.play(self.shot_sound)
            pygame.mixer.music.stop()
            self.municion_actual = 0
            self.esperar_entre_disparos()

nueva_spas = Spas_12()
nueva_spas.disparar()
nueva_spas.disparar()
nueva_spas.recargar()

time.sleep(1)



escopeta_del_doom = DobleCannonDoom()
escopeta_del_doom.vaciar_cargador()
escopeta_del_doom.recargar()


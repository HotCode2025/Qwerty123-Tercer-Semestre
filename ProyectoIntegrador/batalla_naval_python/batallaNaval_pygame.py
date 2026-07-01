"""
Módulo: batallaNaval_pygame.py
Descripción: Versión visual con Pygame del juego Batalla Naval.
             Reemplaza la interfaz de consola por una GUI limpia y moderna.

Estructura:
  - Se reutilizan los módulos de dominio/ y utilidades/ sin modificación.
  - Este archivo solo reemplaza la capa de presentación (batallaNaval.py).

Requisitos:
  pip install pygame
"""

import sys
import math
import random
import pygame

# ──────────────────────────────────────────────────────────────────── #
#  Importaciones del proyecto (misma raíz que antes)                  #
# ──────────────────────────────────────────────────────────────────── #
from dominio.jugadores      import Jugadores
from dominio.tablero        import Tablero
from utilidades.ranking     import Ranking
from utilidades.utilidades  import Utilidades
from utilidades.db          import inicializar_db, guardar_partida, get_historial


# ──────────────────────────────────────────────────────────────────── #
#  Paleta — Limpio y moderno, tema claro minimalista                  #
# ──────────────────────────────────────────────────────────────────── #
C_BG           = (245, 247, 250)
C_PANEL        = (255, 255, 255)
C_PANEL_BORDER = (220, 224, 230)
C_GRID_BG      = (235, 240, 248)
C_GRID_LINE    = (200, 210, 225)
C_CELL_EMPTY   = (225, 232, 242)
C_CELL_HOVER   = (195, 215, 240)
C_WATER        = (100, 160, 220)
C_WATER_RING   = (70,  130, 195)
C_IMPACT       = (240, 100,  60)
C_SUNK         = (200,  50,  30)
C_TEXT_DARK    = ( 30,  38,  50)
C_TEXT_MID     = ( 90, 105, 125)
C_TEXT_LIGHT   = (160, 175, 195)
C_ACCENT       = ( 65, 120, 220)
C_ACCENT2      = ( 40,  90, 175)
C_SUCCESS      = ( 50, 175, 100)
C_WARN         = (240, 165,  30)
C_DANGER       = (215,  55,  55)
C_BTN          = ( 65, 120, 220)
C_BTN_HOVER    = ( 40,  90, 175)
C_BTN_TXT      = (255, 255, 255)
C_WHITE        = (255, 255, 255)
C_SHADOW       = (210, 215, 225)

# Colores para resultados en historial
C_GANADO  = ( 50, 175, 100)
C_PERDIDO = (215,  55,  55)
C_RENDIDO = (150, 130,  60)


# ──────────────────────────────────────────────────────────────────── #
#  Constantes de layout                                                #
# ──────────────────────────────────────────────────────────────────── #
COLS       = 8
ROWS       = 8
CELL       = 58
GRID_PAD_X = 60
GRID_PAD_Y = 80
PANEL_W    = 280
MARGIN     = 20
HEADER_H   = 60
WIN_W      = GRID_PAD_X + COLS * CELL + MARGIN * 2 + PANEL_W + MARGIN
WIN_H      = GRID_PAD_Y + ROWS * CELL + GRID_PAD_X + 20

GRID_LEFT  = GRID_PAD_X
GRID_TOP   = GRID_PAD_Y
PANEL_LEFT = GRID_LEFT + COLS * CELL + MARGIN * 2
PANEL_TOP  = MARGIN


# ──────────────────────────────────────────────────────────────────── #
#  Constantes de partida                                               #
# ──────────────────────────────────────────────────────────────────── #
DISPAROS_TOTALES  = 25
PUNTAJE_INICIAL   = 125
PENALIZACION_AGUA = 5


# ──────────────────────────────────────────────────────────────────── #
#  Animación de partícula                                              #
# ──────────────────────────────────────────────────────────────────── #
class Particula:
    """Una partícula de explosión o splash que vive por ciertos frames."""

    def __init__(self, x, y, color, velocidad, vida, radio=3, tipo="circulo"):
        self.x        = x
        self.y        = y
        self.color    = color
        self.vx       = velocidad[0]
        self.vy       = velocidad[1]
        self.vida     = vida
        self.vida_max = vida
        self.radio    = radio
        self.tipo     = tipo  # "circulo" | "rect"

    def update(self):
        self.x  += self.vx
        self.y  += self.vy
        self.vy += 0.18  # gravedad leve
        self.vida -= 1

    @property
    def alive(self):
        return self.vida > 0

    @property
    def alpha(self):
        return int(255 * (self.vida / self.vida_max))

    def draw(self, surf):
        alpha = self.alpha
        color = (*self.color[:3], alpha)
        r     = max(1, int(self.radio * (self.vida / self.vida_max)))
        tmp   = pygame.Surface((r * 2 + 2, r * 2 + 2), pygame.SRCALPHA)
        if self.tipo == "circulo":
            pygame.draw.circle(tmp, color, (r + 1, r + 1), r)
        else:
            pygame.draw.rect(tmp, color, (0, 0, r * 2, r * 2))
        surf.blit(tmp, (int(self.x) - r, int(self.y) - r))


def crear_splash(cx, cy):
    parts = []
    for _ in range(20):
        ang   = random.uniform(0, 2 * math.pi)
        vel   = random.uniform(1.5, 4.5)
        vx    = math.cos(ang) * vel
        vy    = math.sin(ang) * vel - random.uniform(1, 3)
        color = random.choice([C_WATER, C_WATER_RING, (160, 200, 240)])
        r     = random.randint(2, 5)
        vida  = random.randint(18, 32)
        parts.append(Particula(cx, cy, color, (vx, vy), vida, r))
    return parts


def crear_explosion(cx, cy):
    parts = []
    for _ in range(28):
        ang   = random.uniform(0, 2 * math.pi)
        vel   = random.uniform(2, 6)
        vx    = math.cos(ang) * vel
        vy    = math.sin(ang) * vel - random.uniform(1.5, 4)
        color = random.choice([C_IMPACT, C_SUNK, (255, 200, 50), (240, 130, 40)])
        r     = random.randint(2, 6)
        vida  = random.randint(22, 40)
        parts.append(Particula(cx, cy, color, (vx, vy), vida, r))
    return parts


# ──────────────────────────────────────────────────────────────────── #
#  Onda de expansión (ring)                                            #
# ──────────────────────────────────────────────────────────────────── #
class Onda:
    def __init__(self, cx, cy, color, max_r=40, speed=2):
        self.cx    = cx
        self.cy    = cy
        self.color = color
        self.r     = 4
        self.max_r = max_r
        self.speed = speed

    @property
    def alive(self):
        return self.r < self.max_r

    def update(self):
        self.r += self.speed

    def draw(self, surf):
        alpha = int(200 * (1 - self.r / self.max_r))
        w     = max(1, int(3 * (1 - self.r / self.max_r)))
        tmp   = pygame.Surface((self.max_r * 2 + 4, self.max_r * 2 + 4), pygame.SRCALPHA)
        pygame.draw.circle(
            tmp,
            (*self.color[:3], alpha),
            (self.max_r + 2, self.max_r + 2),
            int(self.r),
            w,
        )
        surf.blit(tmp, (self.cx - self.max_r - 2, self.cy - self.max_r - 2))


# ──────────────────────────────────────────────────────────────────── #
#  Botón reutilizable                                                  #
# ──────────────────────────────────────────────────────────────────── #
class Boton:
    def __init__(self, rect, texto, font,
                 color=C_BTN, color_h=C_BTN_HOVER,
                 color_txt=C_BTN_TXT, radio=8):
        self.rect      = pygame.Rect(rect)
        self.texto     = texto
        self.font      = font
        self.color     = color
        self.color_h   = color_h
        self.color_txt = color_txt
        self.radio     = radio
        self.hovered   = False

    def draw(self, surf):
        col = self.color_h if self.hovered else self.color
        pygame.draw.rect(surf, col, self.rect, border_radius=self.radio)
        txt = self.font.render(self.texto, True, self.color_txt)
        r   = txt.get_rect(center=self.rect.center)
        surf.blit(txt, r)

    def check(self, pos):
        self.hovered = self.rect.collidepoint(pos)
        return self.hovered

    def clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and self.rect.collidepoint(event.pos)
        )


# ──────────────────────────────────────────────────────────────────── #
#  Clase principal de la app                                           #
# ──────────────────────────────────────────────────────────────────── #
class BatallaNavalApp:
    # ── Estados de la aplicación ───────────────────────────────────
    MENU      = "menu"
    NOMBRE    = "nombre"
    JUEGO     = "juego"
    RESULTADO = "resultado"
    RANKING   = "ranking"
    HISTORIAL = "historial"   # ← nuevo estado

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Batalla Naval")

        self.screen = pygame.display.set_mode((WIN_W, WIN_H))
        self.clock  = pygame.time.Clock()
        self.ranking = Ranking()

        # Fuentes
        self.f_title = pygame.font.SysFont("Segoe UI", 32, bold=True)
        self.f_big   = pygame.font.SysFont("Segoe UI", 22, bold=True)
        self.f_med   = pygame.font.SysFont("Segoe UI", 17)
        self.f_small = pygame.font.SysFont("Segoe UI", 14)
        self.f_label = pygame.font.SysFont("Segoe UI", 13)
        self.f_coord = pygame.font.SysFont("Segoe UI", 13, bold=True)

        self.estado = self.MENU
        self._reset_juego()

        # Input de nombre
        self.nombre_input = ""
        self.input_activo = False

        # Partículas y ondas
        self.particulas: list[Particula] = []
        self.ondas: list[Onda]           = []

        # Hover celda
        self.hover_cell = None

        # Mensaje de disparo temporal
        self.msg_disp  = ""
        self.msg_timer = 0
        self._transition_timer = 0

        # Resultado final
        self.resultado_ganado = False

        # Historial cacheado (se recarga al entrar a la pantalla)
        self._historial_cache: list[dict] = []

        # Botones
        self._build_menu_btns()

    # ── Reset ────────────────────────────────────────────────────── #
    def _reset_juego(self):
        self.tablero          = Tablero()
        self.puntaje          = PUNTAJE_INICIAL
        self.disparos_rest    = DISPAROS_TOTALES
        self.disparos_validos = 0
        self.nombre_jugador   = ""
        self.juego_terminado  = False
        self.particulas       = []
        self.ondas            = []
        self.msg_disp         = ""
        self.msg_timer        = 0
        self._transition_timer = 0

    # ── Construcción de botones ───────────────────────────────────── #
    def _build_menu_btns(self):
        cx = WIN_W // 2
        self.btn_jugar = Boton(
            (cx - 130, 240, 260, 52), "🎮  Jugar", self.f_big
        )
        self.btn_ranking = Boton(
            (cx - 130, 304, 260, 52), "🏆  Ranking", self.f_big,
            color=(90, 110, 140), color_h=(70, 90, 120),
        )
        self.btn_historial = Boton(
            (cx - 130, 368, 260, 52), "📋  Historial", self.f_big,
            color=(70, 130, 100), color_h=(50, 105, 80),
        )
        self.btn_salir = Boton(
            (cx - 130, 432, 260, 52), "✕  Salir", self.f_big,
            color=(200, 60, 60), color_h=(170, 40, 40),
        )

    def _build_result_btns(self):
        bx = PANEL_LEFT
        bw = PANEL_W - 10
        self.btn_rejugar = Boton(
            (bx, WIN_H - 148, bw, 40), "🎮  Jugar de nuevo", self.f_med
        )
        self.btn_menu_r = Boton(
            (bx, WIN_H - 100, bw, 40), "🏠  Menú principal", self.f_med,
            color=(90, 110, 140), color_h=(70, 90, 120),
        )
        self.btn_salir_r = Boton(
            (bx, WIN_H - 52, bw, 40), "✕  Salir del juego", self.f_med,
            color=(200, 60, 60), color_h=(170, 40, 40),
        )
        self.mostrar_barcos = False
        self.btn_ver_barcos = Boton(
            (GRID_LEFT, WIN_H - 50, 220, 36),
            "👁  Ver ubicación de barcos", self.f_small,
            color=(90, 110, 140), color_h=(70, 90, 120),
        )

    def _build_ranking_btn(self):
        self.btn_volver = Boton(
            (WIN_W // 2 - 110, WIN_H - 70, 220, 44),
            "← Volver al menú", self.f_med,
            color=(90, 110, 140), color_h=(70, 90, 120),
        )

    def _build_historial_btn(self):
        self.btn_volver_hist = Boton(
            (WIN_W // 2 - 110, WIN_H - 70, 220, 44),
            "← Volver al menú", self.f_med,
            color=(90, 110, 140), color_h=(70, 90, 120),
        )

    # ──────────────────────────────────────────────────────────────── #
    #  Loop principal                                                  #
    # ──────────────────────────────────────────────────────────────── #
    def run(self):
        while True:
            dt = self.clock.tick(60)
            self._handle_events()
            self._update(dt)
            self._draw()
            pygame.display.flip()

    # ── Eventos ──────────────────────────────────────────────────── #
    def _handle_events(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if self.estado == self.MENU:
                self._ev_menu(event, mouse)
            elif self.estado == self.NOMBRE:
                self._ev_nombre(event)
            elif self.estado == self.JUEGO:
                self._ev_juego(event, mouse)
            elif self.estado == self.RESULTADO:
                self._ev_resultado(event, mouse)
            elif self.estado == self.RANKING:
                self._ev_ranking(event, mouse)
            elif self.estado == self.HISTORIAL:
                self._ev_historial(event, mouse)

    def _ev_menu(self, event, mouse):
        self.btn_jugar.check(mouse)
        self.btn_ranking.check(mouse)
        self.btn_historial.check(mouse)
        self.btn_salir.check(mouse)

        if self.btn_jugar.clicked(event):
            self.estado = self.NOMBRE
            self.nombre_input = ""
        if self.btn_ranking.clicked(event):
            self._build_ranking_btn()
            self.estado = self.RANKING
        if self.btn_historial.clicked(event):
            self._build_historial_btn()
            self._historial_cache = get_historial(20)
            self.estado = self.HISTORIAL
        if self.btn_salir.clicked(event):
            pygame.quit()
            sys.exit()

    def _ev_nombre(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.nombre_jugador = self.nombre_input.strip() or "Jugador"
                self._reset_juego()
                self.nombre_jugador = self.nombre_input.strip() or "Jugador"
                self.tablero.colocar_barcos()
                self.estado = self.JUEGO
            elif event.key == pygame.K_BACKSPACE:
                self.nombre_input = self.nombre_input[:-1]
            elif event.key == pygame.K_ESCAPE:
                self.estado = self.MENU
            elif len(self.nombre_input) < 20:
                if event.unicode.isprintable():
                    self.nombre_input += event.unicode

    def _ev_juego(self, event, mouse):
        self.hover_cell = self._cell_at(mouse)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            cell = self._cell_at(event.pos)
            if cell and not self.juego_terminado:
                self._disparar(*cell)

    def _ev_resultado(self, event, mouse):
        self.btn_rejugar.check(mouse)
        self.btn_menu_r.check(mouse)
        self.btn_salir_r.check(mouse)
        if not self.resultado_ganado:
            self.btn_ver_barcos.check(mouse)
            if self.btn_ver_barcos.clicked(event):
                self.mostrar_barcos = not self.mostrar_barcos
                lbl = (
                    "👁  Ocultar barcos"
                    if self.mostrar_barcos
                    else "👁  Ver ubicación de barcos"
                )
                self.btn_ver_barcos = Boton(
                    (GRID_LEFT, WIN_H - 50, 220, 36), lbl, self.f_small,
                    color=(65, 120, 220) if self.mostrar_barcos else (90, 110, 140),
                    color_h=(40, 90, 175) if self.mostrar_barcos else (70, 90, 120),
                )
        if self.btn_rejugar.clicked(event):
            self.estado = self.NOMBRE
            self.nombre_input = self.nombre_jugador
        if self.btn_menu_r.clicked(event):
            self._build_menu_btns()
            self.estado = self.MENU
        if self.btn_salir_r.clicked(event):
            pygame.quit()
            sys.exit()

    def _ev_ranking(self, event, mouse):
        self.btn_volver.check(mouse)
        if self.btn_volver.clicked(event):
            self._build_menu_btns()
            self.estado = self.MENU

    def _ev_historial(self, event, mouse):
        self.btn_volver_hist.check(mouse)
        if self.btn_volver_hist.clicked(event):
            self._build_menu_btns()
            self.estado = self.MENU

    # ── Lógica de disparo ─────────────────────────────────────────── #
    def _disparar(self, fila, col):
        vista = self.tablero.vista_jugador
        if vista[fila][col] != Tablero.SIN_DISP:
            return

        ok = self.tablero.disparar(fila, col)
        if not ok:
            return

        self.disparos_validos += 1
        self.disparos_rest    -= 1

        cx = GRID_LEFT + col  * CELL + CELL // 2
        cy = GRID_TOP  + fila * CELL + CELL // 2

        celda = self.tablero.vista_jugador[fila][col]
        if celda == Tablero.AGUA:
            self.puntaje -= PENALIZACION_AGUA
            self.msg_disp = f"¡Agua!  -{PENALIZACION_AGUA} pts"
            self.ondas   += [
                Onda(cx, cy, C_WATER,      34, 2),
                Onda(cx, cy, C_WATER_RING, 26, 1.5),
            ]
            self.particulas += crear_splash(cx, cy)
        elif celda == Tablero.IMPACTO:
            self.msg_disp    = "¡Impacto!"
            self.particulas += crear_explosion(cx, cy)
            self.ondas.append(Onda(cx, cy, C_IMPACT, 30, 2))
        elif celda == Tablero.HUNDIDO:
            self.msg_disp    = "¡Barco hundido! 💥"
            self.particulas += crear_explosion(cx, cy)
            self.particulas += crear_explosion(cx, cy)
            self.ondas      += [
                Onda(cx, cy, C_SUNK,   40, 2),
                Onda(cx, cy, C_IMPACT, 28, 3),
            ]

        self.msg_timer = 120

        disparos_usados = DISPAROS_TOTALES - self.disparos_rest

        # ¿Terminó el juego?
        if self.tablero.juego_finalizado():
            self.resultado_ganado = True
            self.juego_terminado  = True
            guardar_partida(
                self.nombre_jugador, self.puntaje,
                disparos_usados, "GANADO"
            )
            self._build_result_btns()
            self._transition_timer = 108
        elif self.disparos_rest <= 0:
            self.resultado_ganado = False
            self.juego_terminado  = True
            guardar_partida(
                self.nombre_jugador, self.puntaje,
                disparos_usados, "PERDIDO"
            )
            self._build_result_btns()
            self._transition_timer = 108

    # ── Update ───────────────────────────────────────────────────── #
    def _update(self, dt):
        for p in self.particulas:
            p.update()
        self.particulas = [p for p in self.particulas if p.alive]

        for o in self.ondas:
            o.update()
        self.ondas = [o for o in self.ondas if o.alive]

        if self.msg_timer > 0:
            self.msg_timer -= 1

        if self._transition_timer > 0:
            self._transition_timer -= 1
            if self._transition_timer == 0 and self.estado == self.JUEGO:
                self.estado = self.RESULTADO

    # ──────────────────────────────────────────────────────────────── #
    #  DRAW                                                            #
    # ──────────────────────────────────────────────────────────────── #
    def _draw(self):
        self.screen.fill(C_BG)
        if self.estado == self.MENU:
            self._draw_menu()
        elif self.estado == self.NOMBRE:
            self._draw_nombre()
        elif self.estado == self.JUEGO:
            self._draw_juego()
        elif self.estado == self.RESULTADO:
            self._draw_resultado()
        elif self.estado == self.RANKING:
            self._draw_ranking()
        elif self.estado == self.HISTORIAL:
            self._draw_historial()

    # ── Menú principal ───────────────────────────────────────────── #
    def _draw_menu(self):
        self._draw_ocean_bg(self.screen)

        card_w, card_h = 360, 360
        card_x = WIN_W // 2 - card_w // 2
        card_y = 140
        self._draw_card(self.screen, card_x, card_y, card_w, card_h)

        t1 = self.f_title.render("BATALLA", True, C_TEXT_DARK)
        t2 = self.f_title.render("NAVAL",   True, C_ACCENT)
        self.screen.blit(t1, t1.get_rect(centerx=WIN_W // 2, top=card_y + 22))
        self.screen.blit(t2, t2.get_rect(centerx=WIN_W // 2, top=card_y + 60))

        pygame.draw.line(
            self.screen, C_PANEL_BORDER,
            (card_x + 30, card_y + 100),
            (card_x + card_w - 30, card_y + 100), 1,
        )

        self.btn_jugar.draw(self.screen)
        self.btn_ranking.draw(self.screen)
        self.btn_historial.draw(self.screen)
        self.btn_salir.draw(self.screen)

    def _draw_ocean_bg(self, surf):
        t = pygame.time.get_ticks() / 1000
        for i in range(6):
            y   = 80 + i * 90
            pts = []
            for x in range(0, WIN_W + 20, 10):
                wy = y + math.sin((x / 80) + t + i * 0.8) * 6
                pts.append((x, wy))
            if len(pts) > 1:
                pygame.draw.lines(surf, C_PANEL_BORDER, False, pts, 1)

    # ── Pantalla de nombre ───────────────────────────────────────── #
    def _draw_nombre(self):
        self._draw_header("Nuevo juego")
        card_w, card_h = 400, 200
        cx = WIN_W // 2
        cy = WIN_H // 2 - 20
        self._draw_card(self.screen, cx - card_w // 2, cy - card_h // 2, card_w, card_h)

        lbl = self.f_med.render("Ingresá tu nombre:", True, C_TEXT_MID)
        self.screen.blit(lbl, lbl.get_rect(centerx=cx, top=cy - card_h // 2 + 28))

        inp_rect = pygame.Rect(cx - 160, cy - 20, 320, 46)
        pygame.draw.rect(self.screen, C_WHITE,  inp_rect, border_radius=8)
        pygame.draw.rect(self.screen, C_ACCENT, inp_rect, 2, border_radius=8)
        cursor = "|" if (pygame.time.get_ticks() // 500) % 2 == 0 else ""
        txt = self.f_big.render(self.nombre_input + cursor, True, C_TEXT_DARK)
        self.screen.blit(txt, txt.get_rect(midleft=(inp_rect.left + 14, inp_rect.centery)))

        hint = self.f_small.render(
            "Presioná Enter para comenzar · Esc para volver", True, C_TEXT_LIGHT
        )
        self.screen.blit(hint, hint.get_rect(centerx=cx, top=cy + 50))

    # ── Pantalla de juego ─────────────────────────────────────────── #
    def _draw_juego(self):
        self._draw_header(f"Batalla Naval  ·  {self.nombre_jugador}")
        self._draw_grid()
        self._draw_ondas()
        self._draw_particles()
        self._draw_panel_lateral()
        self._draw_msg_disp()

    def _draw_grid(self):
        gr = pygame.Rect(GRID_LEFT - 4, GRID_TOP - 4, COLS * CELL + 8, ROWS * CELL + 8)
        pygame.draw.rect(self.screen, C_GRID_BG,   gr, border_radius=10)
        pygame.draw.rect(self.screen, C_GRID_LINE, gr, 1, border_radius=10)

        letras = "ABCDEFGH"
        for j, l in enumerate(letras):
            x = GRID_LEFT + j * CELL + CELL // 2
            t = self.f_coord.render(l, True, C_TEXT_MID)
            self.screen.blit(t, t.get_rect(centerx=x, bottom=GRID_TOP - 8))

        for i in range(ROWS):
            y = GRID_TOP + i * CELL + CELL // 2
            t = self.f_coord.render(str(i + 1), True, C_TEXT_MID)
            self.screen.blit(t, t.get_rect(right=GRID_LEFT - 8, centery=y))

        vista = self.tablero.vista_jugador
        for i in range(ROWS):
            for j in range(COLS):
                rx   = GRID_LEFT + j * CELL
                ry   = GRID_TOP  + i * CELL
                rect = pygame.Rect(rx + 2, ry + 2, CELL - 4, CELL - 4)
                celda = vista[i][j]

                if celda == Tablero.SIN_DISP:
                    es_hover = self.hover_cell == (i, j) and not self.juego_terminado
                    col = C_CELL_HOVER if es_hover else C_CELL_EMPTY
                    pygame.draw.rect(self.screen, col, rect, border_radius=6)
                    if es_hover:
                        pygame.draw.rect(self.screen, C_ACCENT, rect, 2, border_radius=6)
                elif celda == Tablero.AGUA:
                    pygame.draw.rect(self.screen, C_WATER, rect, border_radius=6)
                    mid_y = rect.centery
                    for k in range(3):
                        x0 = rect.left + 6 + k * 14
                        pygame.draw.arc(
                            self.screen, C_WATER_RING,
                            (x0, mid_y - 4, 12, 8), 0, math.pi, 2,
                        )
                elif celda == Tablero.IMPACTO:
                    pygame.draw.rect(self.screen, C_IMPACT, rect, border_radius=6)
                    self._draw_cross(rect, C_WHITE)
                elif celda == Tablero.HUNDIDO:
                    pygame.draw.rect(self.screen, C_SUNK, rect, border_radius=6)
                    self._draw_cross(rect, C_WHITE)

                pygame.draw.rect(self.screen, C_GRID_LINE, rect, 1, border_radius=6)

    def _draw_grid_solucion(self):
        self._draw_grid()

        original  = self.tablero.copia_original
        vista     = self.tablero.vista_jugador
        colores   = {1: (120, 200, 120), 2: (120, 160, 220), 3: (200, 140, 80)}
        letras_b  = {1: "S", 2: "D", 3: "C"}

        for i in range(ROWS):
            for j in range(COLS):
                id_b = original[i][j]
                if id_b > 0 and vista[i][j] == Tablero.SIN_DISP:
                    rx   = GRID_LEFT + j * CELL + 2
                    ry   = GRID_TOP  + i * CELL + 2
                    rect = pygame.Rect(rx, ry, CELL - 4, CELL - 4)
                    col  = colores.get(id_b, (180, 180, 180))
                    ov   = pygame.Surface((CELL - 4, CELL - 4), pygame.SRCALPHA)
                    ov.fill((*col, 160))
                    pygame.draw.rect(ov, (*col, 220), ov.get_rect(), border_radius=6)
                    self.screen.blit(ov, (rx, ry))
                    t = self.f_coord.render(letras_b[id_b], True, (255, 255, 255))
                    self.screen.blit(t, t.get_rect(center=rect.center))

        leyenda_items = [
            ((120, 200, 120), "Submarino (S)"),
            ((120, 160, 220), "Destructor (D)"),
            ((200, 140,  80), "Crucero (C)"),
        ]
        lx = GRID_LEFT
        ly = GRID_TOP + ROWS * CELL + 10
        for col, txt in leyenda_items:
            pygame.draw.rect(self.screen, col, (lx, ly + 2, 12, 12), border_radius=3)
            t = self.f_label.render(txt, True, C_TEXT_MID)
            self.screen.blit(t, (lx + 16, ly))
            lx += t.get_width() + 32

    def _draw_cross(self, rect, color):
        m = 10
        pygame.draw.line(
            self.screen, color,
            (rect.left + m, rect.top + m), (rect.right - m, rect.bottom - m), 2,
        )
        pygame.draw.line(
            self.screen, color,
            (rect.right - m, rect.top + m), (rect.left + m, rect.bottom - m), 2,
        )

    def _draw_particles(self):
        for p in self.particulas:
            p.draw(self.screen)

    def _draw_ondas(self):
        for o in self.ondas:
            o.draw(self.screen)

    def _draw_panel_lateral(self):
        panel = pygame.Rect(PANEL_LEFT, PANEL_TOP, PANEL_W - 10, WIN_H - PANEL_TOP - MARGIN)
        self._draw_card(self.screen, panel.x, panel.y, panel.w, panel.h)

        px = panel.x + 20
        py = panel.y + 20

        lbl = self.f_label.render("JUGADOR", True, C_TEXT_LIGHT)
        self.screen.blit(lbl, (px, py))
        nom = self.f_big.render(self.nombre_jugador[:16], True, C_TEXT_DARK)
        self.screen.blit(nom, (px, py + 16))
        py += 58

        self._panel_divider(px, py, panel.w - 40)
        py += 16

        lbl = self.f_label.render("PUNTAJE", True, C_TEXT_LIGHT)
        self.screen.blit(lbl, (px, py))
        col_pts = (
            C_SUCCESS if self.puntaje >= 80
            else (C_WARN if self.puntaje >= 40 else C_DANGER)
        )
        pts = self.f_title.render(str(self.puntaje), True, col_pts)
        self.screen.blit(pts, (px, py + 16))
        self.screen.blit(
            self.f_label.render("pts", True, C_TEXT_MID),
            (px + pts.get_width() + 6, py + 28),
        )
        py += 68

        lbl = self.f_label.render("DISPAROS RESTANTES", True, C_TEXT_LIGHT)
        self.screen.blit(lbl, (px, py))
        py += 18
        bar_w = panel.w - 42
        bar_h = 12
        pygame.draw.rect(self.screen, C_GRID_BG, (px, py, bar_w, bar_h), border_radius=6)
        fill    = int(bar_w * (self.disparos_rest / DISPAROS_TOTALES))
        col_bar = (
            C_SUCCESS if self.disparos_rest > 15
            else (C_WARN if self.disparos_rest > 8 else C_DANGER)
        )
        if fill > 0:
            pygame.draw.rect(self.screen, col_bar, (px, py, fill, bar_h), border_radius=6)
        pygame.draw.rect(self.screen, C_GRID_LINE, (px, py, bar_w, bar_h), 1, border_radius=6)
        py += 18
        disp_txt = self.f_med.render(f"{self.disparos_rest} / {DISPAROS_TOTALES}", True, C_TEXT_DARK)
        self.screen.blit(disp_txt, (px, py))
        py += 38

        self._panel_divider(px, py, panel.w - 40)
        py += 16

        lbl = self.f_label.render("REFERENCIAS", True, C_TEXT_LIGHT)
        self.screen.blit(lbl, (px, py))
        py += 18
        leyendas = [
            (C_CELL_EMPTY, "Sin disparar"),
            (C_WATER,      "Agua"),
            (C_IMPACT,     "Impacto"),
            (C_SUNK,       "Hundido"),
        ]
        for col, txt in leyendas:
            pygame.draw.rect(self.screen, col, (px, py + 2, 14, 14), border_radius=3)
            pygame.draw.rect(self.screen, C_GRID_LINE, (px, py + 2, 14, 14), 1, border_radius=3)
            t = self.f_small.render(txt, True, C_TEXT_MID)
            self.screen.blit(t, (px + 22, py))
            py += 22
        py += 8

        self._panel_divider(px, py, panel.w - 40)
        py += 14

        lbl = self.f_label.render("TOP RANKING", True, C_TEXT_LIGHT)
        self.screen.blit(lbl, (px, py))
        py += 18
        jug = self.ranking.jugadores[:3]
        if not jug:
            t = self.f_small.render("Sin registros aún", True, C_TEXT_LIGHT)
            self.screen.blit(t, (px, py))
        else:
            medals = ["🥇", "🥈", "🥉"]
            for idx, j in enumerate(jug):
                med   = self.f_med.render(medals[idx], True, C_TEXT_DARK)
                self.screen.blit(med, (px, py))
                nom   = self.f_small.render(j.nombre[:14], True, C_TEXT_DARK)
                self.screen.blit(nom, (px + 28, py + 2))
                pts_t = self.f_small.render(f"{j.puntaje}p", True, C_TEXT_MID)
                self.screen.blit(pts_t, (panel.right - 50, py + 2))
                py += 22

    def _panel_divider(self, x, y, w):
        pygame.draw.line(self.screen, C_PANEL_BORDER, (x, y), (x + w, y), 1)

    def _draw_msg_disp(self):
        if self.msg_timer <= 0:
            return
        alpha = min(255, self.msg_timer * 5)
        t  = self.f_big.render(self.msg_disp, True, C_TEXT_DARK)
        bg = pygame.Surface((t.get_width() + 28, t.get_height() + 14), pygame.SRCALPHA)
        bg.fill((*C_WHITE, min(220, alpha)))
        pygame.draw.rect(bg, (*C_PANEL_BORDER, min(180, alpha)),
                         bg.get_rect(), 1, border_radius=8)
        bx = GRID_LEFT + (COLS * CELL - bg.get_width()) // 2
        by = GRID_TOP + ROWS * CELL + 10
        self.screen.blit(bg, (bx, by))
        self.screen.blit(t,  (bx + 14, by + 7))

    # ── Resultado ─────────────────────────────────────────────────── #
    def _draw_resultado(self):
        ganado = self.resultado_ganado
        self._draw_header("Resultado final")

        if not ganado and self.mostrar_barcos:
            self._draw_grid_solucion()
        else:
            self._draw_grid()
        self._draw_particles()

        if not ganado:
            self.btn_ver_barcos.draw(self.screen)

        panel = pygame.Rect(PANEL_LEFT, PANEL_TOP, PANEL_W - 10, WIN_H - PANEL_TOP - MARGIN)
        self._draw_card(self.screen, panel.x, panel.y, panel.w, panel.h)

        px = panel.x + 20
        py = panel.y + 18

        disparos_usados = DISPAROS_TOTALES - self.disparos_rest

        if ganado:
            emoji  = "🏆"
            titulo = "¡VICTORIA!"
            col_t  = C_SUCCESS
            if self.puntaje >= 100:
                msg1, msg2 = "¡Sos un maestro de la estrategia!", "Hundiste todo sin desperdiciar."
            elif self.puntaje >= 70:
                msg1, msg2 = "¡Excelente partida!", "Muy buen uso de los disparos."
            else:
                msg1, msg2 = "¡Lo lograste!", "La próxima, ¡con menos agua!"
        else:
            emoji  = "💀"
            titulo = "¡LÁSTIMA!"
            col_t  = C_DANGER
            if self.puntaje >= 80:
                msg1, msg2 = "¡Estuviste muy cerca!", "Un poco más y los hundías a todos."
            elif self.puntaje >= 50:
                msg1, msg2 = "Buen intento.", "Perdiste, pero aprendiste algo."
            else:
                msg1, msg2 = "El mar te ganó esta vez.", "¡Los barcos no se mueven, animate!"

        em = self.f_title.render(emoji, True, col_t)
        self.screen.blit(em, em.get_rect(centerx=panel.centerx, top=py))
        py += 42
        tit = self.f_big.render(titulo, True, col_t)
        self.screen.blit(tit, tit.get_rect(centerx=panel.centerx, top=py))
        py += 26
        for linea in (msg1, msg2):
            s = self.f_small.render(linea, True, C_TEXT_MID)
            self.screen.blit(s, s.get_rect(centerx=panel.centerx, top=py))
            py += 18
        py += 8

        self._panel_divider(px, py, panel.w - 40)
        py += 14

        stats = [
            ("Puntaje final",    f"{self.puntaje} pts"),
            ("Disparos usados",  f"{disparos_usados} / {DISPAROS_TOTALES}"),
            ("Impactos válidos", f"{self.disparos_validos}"),
        ]
        for k, v in stats:
            lbl   = self.f_label.render(k.upper(), True, C_TEXT_LIGHT)
            self.screen.blit(lbl, (px, py))
            col_v = C_SUCCESS if ganado else C_DANGER
            val   = self.f_med.render(
                v, True, col_v if k == "Puntaje final" else C_TEXT_DARK
            )
            self.screen.blit(val, (panel.right - val.get_width() - 20, py))
            py += 24

        py += 6
        self._panel_divider(px, py, panel.w - 40)
        py += 14

        lbl = self.f_label.render("RANKING ACTUALIZADO", True, C_TEXT_LIGHT)
        self.screen.blit(lbl, (px, py))
        py += 16
        jug    = self.ranking.jugadores[:5]
        medals = ["🥇", "🥈", "🥉", " 4.", " 5."]
        if not jug:
            t = self.f_small.render("Sin registros aún", True, C_TEXT_LIGHT)
            self.screen.blit(t, (px, py))
        else:
            for idx, j in enumerate(jug):
                es_yo  = j.nombre == self.nombre_jugador
                col_n  = C_ACCENT if es_yo else C_TEXT_DARK
                med    = self.f_small.render(medals[idx], True, C_TEXT_MID)
                self.screen.blit(med, (px, py))
                nom    = self.f_small.render(j.nombre[:13], True, col_n)
                self.screen.blit(nom, (px + 26, py))
                pts_t  = self.f_small.render(f"{j.puntaje}p", True, C_TEXT_MID)
                self.screen.blit(pts_t, (panel.right - 46, py))
                py += 19

        self.btn_rejugar.draw(self.screen)
        self.btn_menu_r.draw(self.screen)
        self.btn_salir_r.draw(self.screen)

    # ── Ranking completo ─────────────────────────────────────────── #
    def _draw_ranking(self):
        self._draw_header("🏆  Ranking — Top 10")
        card_w = 480
        cx     = WIN_W // 2
        cy     = HEADER_H + 20

        self._draw_card(self.screen, cx - card_w // 2, cy, card_w, WIN_H - cy - 80)

        px      = cx - card_w // 2 + 30
        py      = cy + 20
        cols_x  = [px, px + 40, px + 180, px + card_w - 80]
        hdrs    = ["#", "Jugador", "", "Puntaje"]
        for i, h in enumerate(hdrs):
            t = self.f_label.render(h.upper(), True, C_TEXT_LIGHT)
            self.screen.blit(t, (cols_x[i], py))
        py += 22
        pygame.draw.line(self.screen, C_PANEL_BORDER, (px, py), (px + card_w - 60, py), 1)
        py += 10

        jug    = self.ranking.jugadores[:10]
        medals = ["🥇", "🥈", "🥉"]
        if not jug:
            t = self.f_med.render("Sin registros aún. ¡Jugá una partida!", True, C_TEXT_LIGHT)
            self.screen.blit(t, t.get_rect(centerx=cx, top=py + 40))
        else:
            for idx, j in enumerate(jug):
                pos_s = medals[idx] if idx < 3 else f"{idx + 1}."
                pos_t = self.f_med.render(pos_s, True, C_TEXT_MID)
                self.screen.blit(pos_t, (cols_x[0], py))
                nom_t = self.f_med.render(j.nombre[:20], True, C_TEXT_DARK)
                self.screen.blit(nom_t, (cols_x[1], py))
                pts_t = self.f_big.render(str(j.puntaje), True, C_ACCENT)
                self.screen.blit(pts_t, (px + card_w - 90, py))
                py += 30
                if idx < len(jug) - 1:
                    pygame.draw.line(
                        self.screen, C_GRID_BG,
                        (px + 10, py - 5), (px + card_w - 70, py - 5), 1,
                    )

        self.btn_volver.draw(self.screen)

    # ── Historial de partidas ─────────────────────────────────────── #
    def _draw_historial(self):
        self._draw_header("📋  Historial de partidas")

        card_w = WIN_W - 80
        cx     = WIN_W // 2
        cy     = HEADER_H + 20
        card_h = WIN_H - cy - 80

        self._draw_card(self.screen, cx - card_w // 2, cy, card_w, card_h)

        px = cx - card_w // 2 + 24
        py = cy + 18

        # ── Encabezado de columnas ──────────────────────────────────
        COL_NOMBRE   = px
        COL_PUNTAJE  = px + 200
        COL_DISPAROS = px + 310
        COL_RESULTADO = px + 410
        COL_FECHA    = px + 540

        hdrs = [
            (COL_NOMBRE,    "Jugador"),
            (COL_PUNTAJE,   "Puntaje"),
            (COL_DISPAROS,  "Disparos"),
            (COL_RESULTADO, "Resultado"),
            (COL_FECHA,     "Fecha"),
        ]
        for cx_col, h in hdrs:
            t = self.f_label.render(h.upper(), True, C_TEXT_LIGHT)
            self.screen.blit(t, (cx_col, py))
        py += 20
        pygame.draw.line(
            self.screen, C_PANEL_BORDER,
            (px, py), (px + card_w - 48, py), 1,
        )
        py += 10

        filas = self._historial_cache

        if not filas:
            t = self.f_med.render(
                "Sin partidas registradas aún. ¡Jugá una partida!",
                True, C_TEXT_LIGHT,
            )
            self.screen.blit(t, t.get_rect(centerx=WIN_W // 2, top=py + 40))
        else:
            iconos = {"GANADO": "✓", "PERDIDO": "✗", "RENDIDO": "~"}
            colores_res = {
                "GANADO":  C_GANADO,
                "PERDIDO": C_PERDIDO,
                "RENDIDO": C_RENDIDO,
            }
            for i, f in enumerate(filas):
                # Fila alternada suave
                if i % 2 == 0:
                    fila_rect = pygame.Rect(px - 8, py - 2, card_w - 32, 22)
                    pygame.draw.rect(self.screen, C_GRID_BG, fila_rect, border_radius=4)

                resultado = f["resultado"]
                icono     = iconos.get(resultado, "?")
                col_res   = colores_res.get(resultado, C_TEXT_MID)

                nombre_txt   = self.f_small.render(f["nombre"][:22],         True, C_TEXT_DARK)
                puntaje_txt  = self.f_small.render(f"{f['puntaje']} pts",    True, C_TEXT_DARK)
                disparos_txt = self.f_small.render(str(f["disparos_usados"]), True, C_TEXT_MID)
                res_txt      = self.f_small.render(f"{icono} {resultado}",    True, col_res)
                fecha_txt    = self.f_small.render(f["fecha"][:16],           True, C_TEXT_LIGHT)

                self.screen.blit(nombre_txt,   (COL_NOMBRE,    py))
                self.screen.blit(puntaje_txt,  (COL_PUNTAJE,   py))
                self.screen.blit(disparos_txt, (COL_DISPAROS,  py))
                self.screen.blit(res_txt,      (COL_RESULTADO, py))
                self.screen.blit(fecha_txt,    (COL_FECHA,     py))

                py += 22
                # Cortar si nos quedamos sin espacio
                if py > cy + card_h - 50:
                    resto = self.f_label.render(
                        f"… y {len(filas) - i - 1} más", True, C_TEXT_LIGHT
                    )
                    self.screen.blit(resto, (px, py + 4))
                    break

        self.btn_volver_hist.draw(self.screen)

    # ── Helpers de dibujo ─────────────────────────────────────────── #
    def _draw_header(self, titulo: str):
        hdr = pygame.Rect(0, 0, WIN_W, HEADER_H)
        pygame.draw.rect(self.screen, C_WHITE, hdr)
        pygame.draw.line(self.screen, C_PANEL_BORDER, (0, HEADER_H), (WIN_W, HEADER_H), 1)
        t = self.f_big.render(titulo, True, C_TEXT_DARK)
        self.screen.blit(t, (24, (HEADER_H - t.get_height()) // 2))

    def _draw_card(self, surf, x, y, w, h, radio=12):
        sombra = pygame.Surface((w + 6, h + 6), pygame.SRCALPHA)
        pygame.draw.rect(sombra, (*C_SHADOW, 120), (3, 3, w, h), border_radius=radio)
        surf.blit(sombra, (x - 1, y + 2))
        pygame.draw.rect(surf, C_PANEL,        (x, y, w, h), border_radius=radio)
        pygame.draw.rect(surf, C_PANEL_BORDER, (x, y, w, h), 1, border_radius=radio)

    def _cell_at(self, pos) -> tuple | None:
        mx, my = pos
        if mx < GRID_LEFT or my < GRID_TOP:
            return None
        j = (mx - GRID_LEFT) // CELL
        i = (my - GRID_TOP)  // CELL
        if 0 <= i < ROWS and 0 <= j < COLS:
            return (i, j)
        return None


# ──────────────────────────────────────────────────────────────────── #
#  Entry point                                                         #
# ──────────────────────────────────────────────────────────────────── #
def main():
    inicializar_db()  # Crea las tablas si no existen
    app = BatallaNavalApp()
    app.run()


if __name__ == "__main__":
    main()

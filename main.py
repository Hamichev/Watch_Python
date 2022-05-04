import pygame as pg
import math
import datetime

pg.init()


HEIGHT, WIDTH = 600, 600
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
bg_color = (168, 69, 167)
r_watch = math.sqrt((WIDTH//2)**2 + (HEIGHT//2)**2) // 2
image_watch = pg.transform.scale(pg.image.load('TheFool.jpg'), (r_watch*2, r_watch*2))
image_bg = pg.transform.scale(pg.image.load('bg.jpg'), (HEIGHT, WIDTH))

sc = pg.display.set_mode((HEIGHT, WIDTH))
pg.display.set_caption('Watch')

def get_coord_point(H, W, r_circle, this_time):
    x = H // 2 + r_circle * math.cos(math.pi * this_time / 30 - math.pi / 2)
    y = W // 2 + r_circle * math.sin(math.pi * this_time / 30 - math.pi / 2)
    return x, y

#-----------------------------------------Surface_watch--------------------------------------------------
watch_surf = pg.Surface((r_watch*2, r_watch*2))
watch_rect = watch_surf.get_rect(center=(HEIGHT // 2, WIDTH // 2))
watch_height = watch_surf.get_height()
watch_width = watch_surf.get_width()
watch_surf.blit(image_watch, (0, 0))
#watch_surf.fill(bg_color)
pg.draw.circle(watch_surf, BLACK, (watch_surf.get_height() // 2, watch_surf.get_width() // 2), r_watch, 2)
for point in range(60):
    if point % 5 == 0:
        pg.draw.line(watch_surf, BLACK, (get_coord_point(watch_height, watch_width, r_watch - 15, point)), (get_coord_point(watch_height, watch_width, r_watch - 2, point)), 4)
    else:
        pg.draw.line(watch_surf, BLACK, (get_coord_point(watch_height, watch_width, r_watch - 10, point)), (get_coord_point(watch_height, watch_width, r_watch - 2, point)))
#--------------------------------------------------------------------------------------------------------

FPS = 60
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    sc.blit(image_bg, (0, 0))
    sc.blit(watch_surf, watch_rect)
    #pg.draw.circle(sc, BLACK, (HEIGHT // 2, WIDTH // 2), r_watch, 2)
    #Воспользуемся формулой описанной окружности и прямоугольником в 2 раза меньшего разрешения экрана, находящимся по центру экрана
    time_now = datetime.datetime.now()
    pg.draw.line(sc, BLACK, (HEIGHT // 2, WIDTH // 2), (get_coord_point(HEIGHT, WIDTH, r_watch - 7, time_now.second)), 2)
    pg.draw.line(sc, GREEN, (HEIGHT // 2, WIDTH // 2), (get_coord_point(HEIGHT, WIDTH, r_watch - 35, time_now.minute)), 4)
    pg.draw.line(sc, BLUE, (HEIGHT // 2, WIDTH // 2), (get_coord_point(HEIGHT, WIDTH, r_watch - 80, time_now.hour*5)), 8)
    pg.display.update()
    clock.tick(FPS)
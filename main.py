import pygame

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Орки идут")
icon = pygame.image.load('images/MPGicon.png')
pygame.display.set_icon(icon)


pl_walk_rigth = [
    pygame.image.load('images/player_1/1_ORK (2100 1250)/1_ORK_R/ORK_01_WALK_000.png').convert_alpha(),
    pygame.image.load('images/player_1/1_ORK (2100 1250)/1_ORK_R/ORK_01_WALK_001.png').convert_alpha(),
    pygame.image.load('images/player_1/1_ORK (2100 1250)/1_ORK_R/ORK_01_WALK_002.png').convert_alpha(),
    pygame.image.load('images/player_1/1_ORK (2100 1250)/1_ORK_R/ORK_01_WALK_003.png').convert_alpha(),
    pygame.image.load('images/player_1/1_ORK (2100 1250)/1_ORK_R/ORK_01_WALK_004.png').convert_alpha(),
    pygame.image.load('images/player_1/1_ORK (2100 1250)/1_ORK_R/ORK_01_WALK_005.png').convert_alpha(),
    pygame.image.load('images/player_1/1_ORK (2100 1250)/1_ORK_R/ORK_01_WALK_006.png').convert_alpha(),
    pygame.image.load('images/player_1/1_ORK (2100 1250)/1_ORK_R/ORK_01_WALK_007.png').convert_alpha(),
    pygame.image.load('images/player_1/1_ORK (2100 1250)/1_ORK_R/ORK_01_WALK_008.png').convert_alpha(),
    pygame.image.load('images/player_1/1_ORK (2100 1250)/1_ORK_R/ORK_01_WALK_009.png').convert_alpha()

]

pl_walk_left = [
    pygame.image.load('images/player_1/1_ORK (2100 1250)/1_ORK_L/ORK_01_WALK_000.png').convert_alpha(),
    pygame.image.load('images/player_1/1_ORK (2100 1250)/1_ORK_L/ORK_01_WALK_001.png').convert_alpha(),
    pygame.image.load('images/player_1/1_ORK (2100 1250)/1_ORK_L/ORK_01_WALK_002.png').convert_alpha(),
    pygame.image.load('images/player_1/1_ORK (2100 1250)/1_ORK_L/ORK_01_WALK_003.png').convert_alpha(),
    pygame.image.load('images/player_1/1_ORK (2100 1250)/1_ORK_L/ORK_01_WALK_004.png').convert_alpha(),
    pygame.image.load('images/player_1/1_ORK (2100 1250)/1_ORK_L/ORK_01_WALK_005.png').convert_alpha(),
    pygame.image.load('images/player_1/1_ORK (2100 1250)/1_ORK_L/ORK_01_WALK_006.png').convert_alpha(),
    pygame.image.load('images/player_1/1_ORK (2100 1250)/1_ORK_L/ORK_01_WALK_007.png').convert_alpha(),
    pygame.image.load('images/player_1/1_ORK (2100 1250)/1_ORK_L/ORK_01_WALK_008.png').convert_alpha(),
    pygame.image.load('images/player_1/1_ORK (2100 1250)/1_ORK_L/ORK_01_WALK_009.png').convert_alpha(),
]
player_anim_coint = 0
bg_x = 0

player_speed = 8
player_x = -700
player_y = -150
is_jamp = False
jamp_caunt = 7

#player = pygame.transform.scale(player, (player.get_width()//3, player.get_height()//3))
bg = pygame.image.load('images/background.png')



running = True
while running:
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 1920, 0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        screen.blit(pl_walk_left[player_anim_coint], (player_x, player_y))
    else:
        screen.blit(pl_walk_rigth[player_anim_coint], (player_x, player_y))

    if keys[pygame.K_LEFT] and player_x > -600:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 1220:
        player_x += player_speed

    if not is_jamp:
        if keys[pygame.K_SPACE]:
            is_jamp = True
    else:
        if jamp_caunt >= -7:
            if jamp_caunt > 0:
                player_y -= (jamp_caunt ** 2) * 4
            else:
                player_y += (jamp_caunt ** 2) * 4
            jamp_caunt -= 1
        else:
            is_jamp = False
            jamp_caunt = 7

    if player_anim_coint == 9:
        player_anim_coint = 0
    else:
        player_anim_coint += 1
    bg_x -= 2
    if bg_x == 1920:
        bg_x = 0
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    clock.tick(15)

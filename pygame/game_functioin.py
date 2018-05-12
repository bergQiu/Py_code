import sys,pygame
from bullet import bullet
from alien import Alien
from time import sleep
from ship import  Ship

def check_keydown_event(event,ai_settings,screen,ship,bullets):
    '''捕获按键按下操作'''
    if event.key == pygame.K_RIGHT:
        ship.moving_rigth = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        if len(bullets) < ai_settings.bulltes_allowed:
            new_bullet = bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
    if event.key == pygame.K_q:
        pygame.quit()
        sys.exit()


def check_keyup_event(event,ship):
    '''捕获按键弹起操作'''
    if event.key == pygame.K_RIGHT:
        ship.moving_rigth = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_event(ai_settings,screen,ship,bullets):
    '''捕获键盘按键的事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:#  Down
            check_keydown_event(event,ai_settings,screen,ship,bullets)

        elif event.type == pygame.KEYUP:#  Up
            check_keyup_event(event,ship)



def update_screen(ai_settings,stats ,screen,ship,bullets,aliens):
    '''刷新屏幕'''
    screen.fill(ai_settings.bg_color)
    #background(screen)
    #show_font(ai_settings,stats,screen)
    ship.update()
    #aliens.update()
    aliens.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullte()

    ship.blitme()
    pygame.display.flip()

def background(screen):
    '''写入背景'''
    image = pygame.image.load('image/background.jpg')
    rect = image.get_rect()
    screen_rect = screen.get_rect()
    rect.x = 00
    rect.y = 00
    screen.blit(image,rect)

def update_buttles(ai_settings,screen,ship,bulltes,aliens):
    #更新子弹的位置
    bulltes.update()
    # 删除超出屏幕的子弹
    check_alien_bullet_collisioins(ai_settings, screen, ship, bulltes, aliens)
    for bullte in bulltes.copy():
        if bullte.rect.bottom <= 0:
            bulltes.remove(bullte)

def create_fleet(ai_settings,screen,ship,aliens):
    alien = Alien(ai_settings,screen)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(get_number_alines(ai_settings,alien.rect.width)):
            creat_alien(ai_settings,screen,aliens,alien_number,row_number)

def get_number_alines(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def creat_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien_width + 2*alien_width*row_number
    aliens.add(alien)

def get_number_rows(ai_settings,ship_height,alien_height):
    available_space_y = ai_settings.screen_height - 3*alien_height - ship_height
    number_rows = int(available_space_y / (4*alien_height))
    return number_rows

def aliens_update(ai_settings,stats,screen,ship,aliens,bulltes):
    #aliens.check_edges()
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    '''s
    flag = False
    for alien in aliens.copy():
        if alien.rect.y >= ai_settings.screen_height:
            flag = True
            '''
    if pygame.sprite.spritecollideany(ship,aliens) :
        ship_hit(ai_settings, stats, screen, ship, aliens, bulltes)
        if stats.ships_left ==0:
            print ("GAME OVER")

def check_fleet_edges(ai_settings,aliens):
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.copy():
        alien.rect.y += ai_settings.alien_drop_factory
    ai_settings.fleet_direction *= -1

def check_alien_bullet_collisioins(ai_settings,screen,ship,bulltes,aliens):
    collisioins = pygame.sprite.groupcollide(bulltes, aliens, True, True)
    if len(aliens) == 0:
        bulltes.empty()
        create_fleet(ai_settings, screen, ship, aliens)

def ship_hit(ai_settings,stats,screen,ship,aliens,bulltes):
    stats.ships_left -= 1
    aliens.empty()
    bulltes.empty()

    create_fleet(ai_settings,screen,ship,aliens)
    Ship(ai_settings, screen)
    sleep(0.5)

def show_font(ai_settings,stats,screen):
    font = pygame.font.SysFont("arial",14)
    Str = "ship_left: "+ str(stats.ships_left)
    ship_left_sufrce=font.render(Str,True,(0,0,127),ai_settings.bg_color)
    #rect = ship_left_sufrce.get_rect()
    screen.blit(ship_left_sufrce,(0,0))

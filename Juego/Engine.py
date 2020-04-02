import tcod as libtcod
from AccionesMovimiento import Acciones

def main():
    # tamaño de la pantalla
    screen_width = 80
    screen_height = 50

    # track del jugador
    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    # accion movimiento
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    # Lectura de la fuente, una imagen que refleja los "sprites"
    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    # llama a la pantalla
    libtcod.console_init_root(screen_width, screen_height, 'Cyberpunk', False)

    con = libtcod.console_new(screen_width, screen_height)
    # Loop del juego (para no cerrarlo con cada movimiento)
    while not libtcod.console_is_window_closed():
        # accion movimientos
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        # parametros del jugador
        libtcod.console_set_default_foreground(con,  libtcod.red) # color del jugador
        libtcod.console_put_char(con, player_x, player_y, '@', libtcod.BKGND_NONE) # ubicacion fisica
        libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
        libtcod.console_flush()

        libtcod.console_put_char(con, player_x, player_y, ' ', libtcod.BKGND_NONE)  # quitar el area de espacio recorrido
        action = Acciones(key)

        Mover = action.get('Mover')
        Salir = action.get('Salir')
        PantallaCompleta = action.get('PantallaCompleta')

        if Mover:
            dx, dy = Mover
            player_x += dx
            player_y += dy
        if Salir:
            return True

        if PantallaCompleta:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

if __name__ == '__main__':
    main()

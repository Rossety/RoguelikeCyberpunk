import tcod as libtcod

# Traduccion de acciones del teclado a acciones del juego
# los Keys son botones del teclado, que accionaran un evento
def Acciones(key):

    #Evento - movimiento
    if key.vk == libtcod.KEY_UP:
        return {'Mover': (0, -1)}
    elif key.vk == libtcod.KEY_DOWN:
        return {'Mover': (0, 1)}
    elif key.vk == libtcod.KEY_LEFT:
        return {'Mover': (-1, 0)}
    elif key.vk == libtcod.KEY_RIGHT:
        return {'Mover': (1, 0)}
    # Evento - Pantalla completa
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        return {'PantallaCompleta': True}

    # Evento - Salir del juego
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'Salir': True}

    # No key was pressed
    return {}
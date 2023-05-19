import random
import os


os.system('clear')
print('\nBienvenido al juego de piedra, papel o tijera 2 vs 1, 2 jugadores contra la pc')

#modos de juego
print('Podran jugar en equipo o de manera individual, si eligen equipo seran los dos contra la pc, si eligen individual el marcador les asignara puntos a cada uno')

options = ['piedra', 'papel', 'tijera']

confirmations = ['s', 'si', 'yes']

game_mode = ''
name_player1 = ''
name_player2 = ''

while True:
    game_mode = input('\nDesean jugar en equipo o individual (e / i) ')
    game_mode.lower

    if (game_mode == 'e') or (game_mode == 'i'):
        name_player1 = input('\n Ingrese el nombre del primer jugador: ')
        name_player2 = input('\n Ingrese el nombre del segundo jugador: ')
        break
    else :
        print(f'{game_mode} no es un modo de juego valido, puedes elegir (e)quipo o (i)ndividual')
        continue 

def jugar(name_jugador):
    pc = random.choice(options)
    player = ''

    while True:
        player = input(f'\n{name_jugador} elige piedra, papel o tijera: ')
        if player in options:
            break
        else:
            print(f'{player} no es una opcion valida')
            continue

    if pc == player:
        print(f'\n la pc y {name_jugador} han sacado {pc}, es un empate')
        resultado = 'empate'
    elif (player == 'piedra' and pc == 'tijera') or (player == 'papel' and pc == 'piedra') or (player == 'tijera' and pc == 'papel') :
        print(f'\n {player} le gana a {pc}, Punto para {name_jugador}')
        resultado = 1
    else :
        print(f'\n {pc} le gana a {player}, Punto para la pc')
        resultado = 0
    return resultado

def validacion(marcador, resultado):
    if resultado == 0:
        marcador[0] += 1

    elif resultado == 1:
        marcador[1] += 1

    return marcador

if game_mode == 'e':
    marcador = [ 0, 0] #puntos pc, puntos equipo

    while True:
        os.system('clear')
        print('Marcador Actual')
        print(f'pc: {marcador[0]} : jugadores: {marcador[1]}')
        player1 = jugar(name_player1)
        player2 = jugar(name_player2)

        if (player1 == 'empate') and (player2 == 'empate'):
            print('\n Ninguno de los dos me ha ganado, Ha sido un empate')
            print(f'pc: {marcador[0]} : jugadores: {marcador[1]}')
        
        elif (player1 == 1) and (player2 == 1):
            marcador[1] += 1
            print('\n Los dos me han ganado, punto para ustedes')
            print(f'pc: {marcador[0]} : jugadores: {marcador[1]}')

        elif (player1 == 0) and (player2 == 0):
            marcador[0] += 1
            print('\n Les he ganado a los dos, eso es un punto para mi')
            print(f'pc: {marcador[0]} : jugadores: {marcador[1]}')
        
        else:
            print('\n Solo uno de ustedes me ha ganado, el punto sera para mi')
            marcador[0] += 1
            print(f' pc: {marcador[0]} : jugadores: {marcador[1]}')

        nueva_ronda = input('\n Una ronda mas? (s / n)')

        if nueva_ronda in confirmations:
            continue
        else:
            os.system('clear')
            print('Marcador final')
            print(f' pc: {marcador[0]} : jugadores: {marcador[1]}')
            break

elif game_mode == 'i':
    marcador1 = [ 0, 0 ] #puntos pc , puntos jugador 1
    marcador2 = [ 0, 0 ] #puntos pc , puntos jugador 2

    while True:
        os.system('clear')
        print('Marcador Actual')
        print(f'{name_player1} : {marcador1[1]} : {name_player2} : {marcador2[1]}')
        #turno primer jugador
        player1 = jugar(name_player1)
        marcador1 = validacion(marcador1, player1)
        print(f' pc: {marcador1[0]} : {name_player1}: {marcador1[1]}')
        #turno segundo jugador
        player2 = jugar(name_player2)
        marcador2 = validacion(marcador2, player2)
        print(f' pc: {marcador2[0]} : {name_player2}: {marcador2[1]}')

        print(f'\n {name_player1}: {marcador1[1]} puntos : {name_player2}: {marcador2[1]} puntos')

        nueva_ronda = input('\nUna ronda mas? (s / n)')

        if nueva_ronda in confirmations:
            continue
        else:
            if marcador1[1] == marcador2[1]:
                print(f'\nNo hay ganador, ha sido un empate')
            elif marcador1[1] > marcador2[1]:
                print(f'\nEl ganador es {name_player1} con {marcador1[1]} puntos')
            elif marcador1[1] < marcador2[1]:
                print(f'\nEl ganador es {name_player2} con {marcador2[1]} puntos')
            break



print('\nGracias por jugar\n')

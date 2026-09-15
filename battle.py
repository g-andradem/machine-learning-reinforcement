from player import Player
from enemy import Enemy
from settings import *

def get_state(player, enemy):
    # divido por 20
    # menos estados (3, 2), (6, 7)
    # em vez de (500, 400), (501, 400)

    # 340 // 20 == 17
    # valor da vida entre 340 - 359
    return (
        player.hp // 20,
        enemy.hp // 20
    )

def set_turn_order(player, enemy):
    if player.speed > enemy.speed:
        turn_order = [player, enemy]
    else:
        turn_order = [enemy, player]
    return turn_order

def battle(agent, data, speed_enemy):
    # INICIALIZAR ENTITYS
    player = Player()
    enemy = Enemy(speed_enemy)

    data_battle = []

    turn_order = set_turn_order(player, enemy)

    turn = 0

    # ESTADO INICIAL DA BATALHA
    state = get_state(player, enemy)

    while player.is_alive() and enemy.is_alive():
        import random

        # VIDA ANTES DO TURNO
        current_player_hp = player.hp
        current_enemy_hp = enemy.hp

        # PLAYER CHOICE ACTIONS
        player_action = random.choice(ACTIONS)

        # ENEMY CHOICE ACTIONS
        # Ação do inimigo escolhida pelo ML
        # enemy_action = agent.choose_action(state)
        enemy_action = random.choice(ACTIONS)

        for character in turn_order:
            if character == player:
                if player.is_alive():
                    if player_action == 'melee_attack':
                        player.melee_attack(enemy)
                        data[2] += player.attack
                    elif player_action == 'magic_attack':
                        player.magic_attack(enemy)
                        data[2] += player.attack
                    elif player_action == 'defend':
                        player.defend()
            else:
                if enemy.is_alive():
                    if enemy_action == 'melee_attack':
                        enemy.melee_attack(player)
                        data[3] += enemy.attack
                    elif enemy_action == 'magic_attack':
                        enemy.magic_attack(player)
                        data[3] += enemy.attack
                    elif enemy_action == 'defend':
                        enemy.defend()

        data_battle.append({
            'turn': turn,
            'player_hp': player.hp,
            'player_action': player_action,
            'enemy_hp': enemy.hp,
            'enemy_action': enemy_action
        })  

        # RECOMPENSA
        if enemy.hp - current_enemy_hp > player.hp - current_player_hp:
            reward = current_player_hp - player.hp
        elif enemy.hp - current_enemy_hp < player.hp - current_player_hp:
            reward = enemy.hp - current_enemy_hp
        else:
            reward = 0

        # ESTADO FINAL DO TURNO
        next_state = get_state(player, enemy)

        # AGENTE APRENDE
        # COnferir estado final, mesmo morto acontece aprendizado
        agent.learn(state, enemy_action, reward, next_state)

        # ESTADO INICIAL DO PROXIMO TURNO
        state = next_state

        # PROXIMO TURNO
        turn += 1

    # diminuir exploração
    # se o agent chegar a 0,05, ele vai volta para um valor maior
    # necessario que haja um pouco de aleatoriedade, mesmo que baixa
    if agent.epsilon > 0.05:
        agent.epsilon *= 0.995

    # aplicar recompensa depois
    if not enemy.is_alive():
        data[0] += 1
        reward = -100
    elif not player.is_alive():
        data[1] += 1
        reward = 100

    return data_battle
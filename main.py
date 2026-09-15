from player import Player
from enemy import Enemy
from q_learning import QLearningAgent

from multiprocessing import Process

ACTIONS = [
    "attack",
    "defend",
    "heal"
]

# Cria a Saida
def create_battle_data(data, battle_number):
    with open(f"battle{battle_number}_data.txt", 'w') as file:
        file.write(f"===== battle_{battle_number} =====\n\n")

        for turn in data:
            file.write(f"Turn {turn['turn']}\n")
            file.write(f"Player Hp: {turn['player_hp']}\n")
            file.write(f"Player Action: {turn['player_action']}\n")
            file.write(f"Enemy Hp: {turn['enemy_hp']}\n")
            file.write(f"Enemy Action: {turn['enemy_action']}\n")
            file.write('\n')

def create_analysis(data, entity):
    with open(f'data_analysis_{entity}.txt', 'w') as file:
        file.write(f"Player Wins: {data[0]}\n")
        file.write(f"Enemy Wins: {data[1]}\n")
        file.write(f"Player_Damage: {data[2]}\n")
        file.write(f"Enemy_Damage: {data[3]}\n")

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

# for episode in range(10000):

def battle(agent, data, speed):
    # INICIALIZAR ENTITYS
    player = Player(max_hp = 50, attack = 10, speed = 1)
    enemy = Enemy(max_hp = 50, attack = 10, speed = 0 + speed)

    data_battle = []

    if player.speed > enemy.speed:
        turn_order = [player, enemy]
    else:
        turn_order = [enemy, player]

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
                    if player_action == 'attack':
                        player.attack_enemy(enemy)
                        data[2] += player.attack
                    elif player_action == 'heal':
                        player.heal()
                    elif player_action == 'defend':
                        player.defend()

            else:
                if enemy.is_alive():
                    if enemy_action == 'attack':
                        enemy.attack_enemy(player)
                        data[3] += enemy.attack
                    elif enemy_action == 'heal':
                        enemy.heal()
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

    if enemy.hp > 0:
        data[1] += 1
    else:
        data[0] += 1

    return data_battle

    # data['battle_1'] = data_battle

def main():
    player_wins = 0
    enemy_wins = 0
    player_damage = 0
    enemy_damage = 0

    data = [
        player_wins,   # [0]
        enemy_wins,    # [1]
        player_damage, # [2]
        enemy_damage   # [3]
    ]

    battle_number = 0

    num_battles = 1000

    # CRIAR AGENTE
    agent = QLearningAgent(ACTIONS)

    # speed = 0 PLAYER FIRST
    # speed > 2 ENEMY FIRST
    speed = 5
    for battle_number in range(num_battles):
        data_battle = battle(agent, data, speed)
        # create_battle_data(data_battle, battle_number)
        battle_number += 1

    create_analysis(data, 'enemy')

    data[:] = [0] * len(data)
    speed = 0
    for battle_number in range(num_battles):
        data_battle = battle(agent, data, speed)
        # create_battle_data(data_battle, battle_number)
        battle_number += 1

    create_analysis(data, 'player')

if __name__ == '__main__':
    main()
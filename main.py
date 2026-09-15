from multiprocessing import Process, Queue, Pool

from q_learning import QLearningAgent
from settings import *
from battle import battle
from support import create_analysis, create_battle_data

# data = [
#   player_wins,   [0]
#   enemy_wins,    [1]
#   player_damage, [2]
#   enemy_damage   [3]
# ]

def player_first(agent):
    data = [0, 0, 0, 0]

    for battle_number in range(NUM_BATTLE):
        data_battle = battle(agent, data, 0)
        # create_battle_data(data_battle, battle_number)
        battle_number += 1

    return data

def enemy_first(agent):
    data = [0, 0, 0, 0]

    for battle_number in range(NUM_BATTLE):
        data_battle = battle(agent, data, 20)
        # create_battle_data(data_battle, battle_number)
        battle_number += 1

    return data

def run_simulation(args):
    agent, order = args

    if order == "player_first":
        return player_first(agent)

    elif order == "enemy_first":
        return enemy_first(agent)

def main():

    # CRIA AGENTE
    agent = QLearningAgent(ACTIONS)

    # MULTIPROCESSAMENTO
    with Pool(2) as pool:
        results = pool.map(
            run_simulation,
            [
                (agent, "player_first"),
                (agent, "enemy_first"),
            ]
        )

    # RECEBER OS DADOS
    data_player_first = results[0]
    data_enemy_first = results[1]

    # CRIAR TXT PARA ANALISE
    create_analysis(data_enemy_first, 'enemy')
    create_analysis(data_player_first, 'player')

if __name__ == '__main__':
    main()
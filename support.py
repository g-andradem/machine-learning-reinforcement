# Cria a Saida por Batalha
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

# Cria Analise Geral
def create_analysis(data, entity):
    with open(f'data_analysis_{entity}.txt', 'w') as file:
        file.write(f"Player Wins: {data[0]}\n")
        file.write(f"Enemy Wins: {data[1]}\n")
        file.write(f"Player_Damage: {data[2]}\n")
        file.write(f"Enemy_Damage: {data[3]}\n")
import random

# Exploration -> Experimentar ações novas/aleatórias
# Exploitation -> Usar o conhecimento que já possui

class QLearningAgent:
    def __init__(self, actions):

        self.actions = actions

        self.q_table = {}

        self.learning_rate = 0.1
        self.discount_factor = 0.9

        # 100 % de chance no comeco de ele fazer algo aleatorio
        # chance vai diminuindo
        self.epsilon = 1.0

    # Gera a Q_Table de estados nao criados ainda
    def get_q_values(self, state):
        # state (3,4) procura na q_table se existe
        if state not in self.q_table:
            # gera { "attack": 0.0, "heal": 0.0, "defend": 0.0 }
            self.q_table[state] = {
                action: 0.0 for action in self.actions
            }
        return self.q_table[state]

    # 
    def choose_action(self, state):
        # retorna os valores de attack, heal e defend naquele estado
        q_values = self.get_q_values(state)

        # Exploração
        # Gera um valor aleatorio e confere 
        # com epsilon (chance de agir aleatoriamente)
        if random.random() < self.epsilon:
            return random.choice(self.actions)

        # Exploitation do que já aprendeu
        # Retorna a acao de maior valor
        return max(q_values, key = q_values.get)

    # state -> como estava
    # action -> oq foi feito
    # reward -> recompensa da acao feito no estado
    # next_state -> como ficou
    def learn(self, state, action, reward, next_state):
        # pega os valores do estado anterior
        # ex.: estado (3,4)
        q_values = self.get_q_values(state)

        # pega o valores do estado posterior
        next_q_values = self.get_q_values(next_state)

        # pega o valor da acao realizada no determinado estado
        old_value = q_values[action]

        # pega o melhor valor da proxima acao
        best_next_value = max(next_q_values.values())

        # calcular o novo valor da acao feita
        new_value = (
            old_value + self.learning_rate * (
                reward + self.discount_factor * best_next_value - old_value
            )
        )

        q_values[action] = new_value
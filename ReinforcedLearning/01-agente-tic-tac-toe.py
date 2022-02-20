# Algoritmo de aprendizagem por reforço simples para aprender a jogar o tic-tac-toe

# Value Function: é a medida que considera a probabilidade de todas as possíveis recompensas de um estado.
# A Value Function é uma forma eficiente e rápida de buscar a árvore do jogo em busca do melhor caminho para chegar a recompensa.
# Update rule: V(s) = V(s) + alpha*(V(s') - V(s))
# s  = estado corrente
# s' = próximo estado
# s representa cada estado que nós encontramos em um episódio e por isso precisamos do histórico de estados em um episódio
# Estados terminais não são atualizados, uma vez que não existe próximo estado
# Treinamos o algoritmo sobre vários episódios até encontrar o melhor valor de alpha
# A fórmula acima é similar à fórmula do gradient descent em aprendizagem supervisionada

# Epsilon-greedy policy:
#   action|s = argmax[sobre todas as ações possíveis do estado s]{ V(s) }  if rand > epsilon
#   action|s = selecione ação aleatória de possíveis ações do estado s if rand < epsilon
#
# Algumas dicas de melhorias no algoritmo:
#
# Atualmente, ambos os agentes usam a mesma estratégia de aprendizagem enquanto jogam um contra o outro.
# E se eles tiverem diferentes taxas de aprendizado?
# E se eles tiverem diferentes epsilons? (probabilidade de explorar)
# Quem convergirá mais rápido?
# E se um agente não aprender?
# Uma pergunta filosófica interessante: se não há ninguém para desafiá-lo, você pode alcançar seu potencial máximo?

# Imports
import numpy as np
import matplotlib.pyplot as plt
from builtins import range, input

# Variável para ajudar a definir o total de estados possíveis
LENGTH = 3

# Classe Agente
class Agent:
    def __init__(self, eps=0.1, alpha=0.5):

        # Probabilidade de escolher uma ação aleatória em vez de gananciosa
        self.eps = eps

        # Learning rate
        self.alpha = alpha

        self.verbose = False
        self.state_history = []

    def setV(self, V):
        self.V = V

    def set_symbol(self, sym):
        self.sym = sym

    def set_verbose(self, v):
        # Se for verdade, imprimirá valores para cada posição no tabuleiro
        self.verbose = v

    def reset_history(self):
        self.state_history = []

    def take_action(self, env):
        # Escolhe uma ação baseada na estratégia epsilon-gananciosa
        r = np.random.rand()
        best_state = None
        if r < self.eps:
            # Toma uma ação aleatória
            if self.verbose:
                print("Tomando uma ação aleatória")

            possible_moves = []
            for i in range(LENGTH):
                for j in range(LENGTH):
                    if env.is_empty(i, j):
                        possible_moves.append((i, j))
            idx = np.random.choice(len(possible_moves))
            next_move = possible_moves[idx]
        else:
            # Escolha a melhor ação com base nos valores atuais de estados,
            # faz um loop em todos os movimentos possíveis,
            # obtém seus valores para acompanhar o melhor valor
            pos2value = {}
            next_move = None
            best_value = -1
            for i in range(LENGTH):
                for j in range(LENGTH):
                    if env.is_empty(i, j):
                        # Qual é o estado se fizermos esse movimento?
                        env.board[i,j] = self.sym
                        state = env.get_state()
                        env.board[i,j] = 0
                        pos2value[(i,j)] = self.V[state]
                        if self.V[state] > best_value:
                            best_value = self.V[state]
                            best_state = state
                            next_move = (i, j)

            # Se verbose, desenhe o tabuleiro com os valores
            if self.verbose:
                print("Tomando uma ação gananciosa")
                for i in range(LENGTH):
                    print("------------------")
                    for j in range(LENGTH):
                        if env.is_empty(i, j):
                            # Imprime o valor
                            print(" %.2f|" % pos2value[(i,j)], end="")
                        else:
                            print("  ", end="")
                            if env.board[i,j] == env.x:
                                print("x  |", end="")
                            elif env.board[i,j] == env.o:
                                print("o  |", end="")
                            else:
                                print("   |", end="")
                    print("")
                print("------------------")

        # Faz o movimento
        env.board[next_move[0], next_move[1]] = self.sym

    def update_state_history(self, s):
        # Não pode colocar isso em take_action, porque take_action só acontece uma vez a cada outra iteração
        # para cada histórico de estado do jogador o estado precisa ser atualizado a cada iteração s = env.get_state()
        # e não queremos fazer isso duas vezes.
        self.state_history.append(s)

    def update(self, env):
        # Queremos BACKTRACK sobre os estados, para que:
        # V(prev_state) = V(prev_state) + alpha*(V(next_state) - V(prev_state))
        # where V(next_state) = reward se for o estado mais atual
        #
        # NOTA: fazemos isso no final de um episódio

        # Aqui é onde a aprendizagem realmente acontece
        reward = env.reward(self.sym) # recompensa
        target = reward
        for prev in reversed(self.state_history):
            value = self.V[prev] + self.alpha*(target - self.V[prev]) # value function
            self.V[prev] = value
            target = value
        self.reset_history()


# Classe Ambiente
class Environment:

    # Construtor
    def __init__(self):
        self.board = np.zeros((LENGTH, LENGTH)) # tabuleiro

        # Representa um x no tabuleiro, jogador 1
        self.x = -1

        # Representa um o no tabuleiro, jogador 2
        self.o = 1

        self.winner = None # não tem nenhum verncedor
        self.ended = False
        self.num_states = 3**(LENGTH*LENGTH)

    def is_empty(self, i, j):
        return self.board[i,j] == 0

    def reward(self, sym):
        # Sem recompensa até terminar o jogo
        if not self.game_over():
            return 0

        # Se chegamos aqui, game is over
        return 1 if self.winner == sym else 0

    def get_state(self):
        # Retorna o estado atual, representado como um int de 0 ... | S | -1, onde S = conjunto de todos os estados possíveis
        # | S | = 3 ^ (TAMANHO DO TABULEIRO), uma vez que cada célula pode ter 3 valores possíveis - vazio, x, o - alguns estados não são possíveis,
        # p. Ex. todas as células são x, mas ignoramos esse detalhe, é como encontrar o número inteiro representado por um número base-3
        k = 0
        h = 0
        for i in range(LENGTH):
            for j in range(LENGTH):
                if self.board[i,j] == 0:
                    v = 0
                elif self.board[i,j] == self.x:
                    v = 1
                elif self.board[i,j] == self.o:
                    v = 2
                h += (3**k) * v
                k += 1
        return h

    def game_over(self, force_recalculate=False):
        # Retorna verdadeiro se o jogo acabou (um jogador ganhou ou é um empate), de outra forma, retorna falso
        # também define a variável de exemplo 'vencedor' e a variável de instância 'encerrada'
        if not force_recalculate and self.ended:
            return self.ended

        # Verifica se há vencedor

        # Checa as linhas - valores iguais
        for i in range(LENGTH):
            for player in (self.x, self.o):
                if self.board[i].sum() == player*LENGTH:
                    self.winner = player
                    self.ended = True
                    return True

        # Checa as colunas
        for j in range(LENGTH):
            for player in (self.x, self.o):
                if self.board[:,j].sum() == player*LENGTH:
                    self.winner = player
                    self.ended = True
                    return True

        # Checa as diagonais
        for player in (self.x, self.o):
            # top-left -> bottom-right diagonal
            if self.board.trace() == player*LENGTH:
                self.winner = player
                self.ended = True
                return True
            # top-right -> bottom-left diagonal
            if np.fliplr(self.board).trace() == player*LENGTH:
                self.winner = player
                self.ended = True
                return True

        # Checa se é empate
        if np.all((self.board == 0) == False):
            self.winner = None
            self.ended = True
            return True

        # O jogo ainda não acabou
        self.winner = None
        return False

    def is_draw(self):
        return self.ended and self.winner is None

    # Exemplo de tabuleiro
    # -------------
    # | x |   |   |
    # -------------
    # |   |   |   |
    # -------------
    # |   |   | o |
    # -------------
    def draw_board(self):
        for i in range(LENGTH):
            print("-------------")
            for j in range(LENGTH):
                print("  ", end="")
                if self.board[i,j] == self.x:
                    print("x ", end="")
                elif self.board[i,j] == self.o:
                    print("o ", end="")
                else:
                    print("  ", end="")
            print("")
        print("-------------")


# Classe Humano
class Human:
    def __init__(self):
        pass

    def set_symbol(self, sym):
        self.sym = sym

    def take_action(self, env):
        while True:
            # Break se fizermos um movimento legal
            move = input("Insira as coordenadas i, j para o próximo movimento (por exemplo: 0,2): ")
            i, j = move.split(',')
            i = int(i)
            j = int(j)
            if env.is_empty(i, j):
                env.board[i,j] = self.sym
                break

    def update(self, env):
        pass

    def update_state_history(self, s):
        pass


# Função recursiva que retornará todos os estados possíveis (como ints) e quem é o vencedor correspondente para esses estados (se houver) 
# (i, j) se refere à próxima célula no tabuleiro para permutar (precisamos tentar -1, 0, 1) 
# jogos impossíveis são ignorados, ou seja, 3x e 3o em uma linha simultaneamente, pois isso nunca acontecerá em um jogo real
def get_state_hash_and_winner(env, i=0, j=0): # usa permutação
    results = []

    for v in (0, env.x, env.o):
        env.board[i,j] = v
        if j == 2:
            if i == 2:
                state = env.get_state()
                ended = env.game_over(force_recalculate=True)
                winner = env.winner
                results.append((state, winner, ended))
            else:
                results += get_state_hash_and_winner(env, i + 1, 0)
        else:
            results += get_state_hash_and_winner(env, i, j + 1)

    return results

# Inicializa os estados de x com a função valor
def initialV_x(env, state_winner_triples):
    # if x wins, V(s) = 1
    # if x loses or draw, V(s) = 0
    # otherwise, V(s) = 0.5
    V = np.zeros(env.num_states)
    for state, winner, ended in state_winner_triples:
        if ended:
            if winner == env.x:
                v = 1
            else:
                v = 0
        else:
            v = 0.5
        V[state] = v
    return V

# Inicializa os estados de o com a função valor
def initialV_o(env, state_winner_triples):
    V = np.zeros(env.num_states)
    for state, winner, ended in state_winner_triples:
        if ended:
            if winner == env.o:
                v = 1
            else:
                v = 0
        else:
            v = 0.5
        V[state] = v
    return V

# Loop até o jogo terminar
def play_game(p1, p2, env, draw=False):
    current_player = None
    while not env.game_over():
        # Alternar entre jogadores
        # p1 sempre começa primeiro
        if current_player == p1:
            current_player = p2
        else:
            current_player = p1

        # Desenha o tabuleiro antes que o usuário faça um movimento
        if draw:
            if draw == 1 and current_player == p1:
                env.draw_board()
            if draw == 2 and current_player == p2:
                env.draw_board()

        # Jogador atual faz um movimento
        current_player.take_action(env)

        # Atualiza estados
        state = env.get_state()
        p1.update_state_history(state)
        p2.update_state_history(state)

    if draw:
        env.draw_board()

    # Atualiza a função valor
    p1.update(env) # aprendizado
    p2.update(env)


if __name__ == '__main__':
    # Treina o agente
    p1 = Agent()
    p2 = Agent()

    # Configura initial V para p1 e p2
    env = Environment()
    state_winner_triples = get_state_hash_and_winner(env)


    Vx = initialV_x(env, state_winner_triples)
    p1.setV(Vx)
    Vo = initialV_o(env, state_winner_triples)
    p2.setV(Vo)

    # Define o símbolo de cada jogador
    p1.set_symbol(env.x)
    p2.set_symbol(env.o)

    T = 10000 # treinamento do agente
    for t in range(T):
        if t % 200 == 0:
            print(t)
        play_game(p1, p2, Environment())

    # Jogando: Humano x Agente
    human = Human()
    human.set_symbol(env.o)
    while True:
        p1.set_verbose(True)
        play_game(p1, human, Environment(), draw=2)
        answer = input("Jogar novamente? [Y/n]: ")
        if answer and answer.lower()[0] == 'n':
            break
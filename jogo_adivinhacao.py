import random
import matplotlib.pyplot as plt

class GameAgent:
    def __init__(self, difficulty='médio'):
        self.difficulty = difficulty
        self.set_difficulty()
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.state = "Esperando tentativa"
        self.history = []
    
    def set_difficulty(self):
        difficulties = {
            'fácil': 10,
            'médio': 7,
            'difícil': 5
        }
        self.max_attempts = difficulties.get(self.difficulty, 7)
    
    def make_guess(self, guess):
        self.attempts += 1
        self.history.append(guess)
        
        if guess == self.secret_number:
            self.state = "Acertou!"
            return f"Parabéns! Você acertou o número {self.secret_number} em {self.attempts} tentativas."
        elif self.attempts >= self.max_attempts:
            self.state = "Fim do jogo"
            return f"Game Over! O número era {self.secret_number}. Suas tentativas: {self.history}"
        elif guess < self.secret_number:
            self.state = "Tentativa errada (muito baixo)"
            return f"O número é maior. {self.get_hint(guess)} Tente novamente."
        else:
            self.state = "Tentativa errada (muito alto)"
            return f"O número é menor. {self.get_hint(guess)} Tente novamente."
    
    def get_hint(self, guess):
        if len(self.history) > 1:
            prev_guess = self.history[-2]
            if abs(guess - self.secret_number) < abs(prev_guess - self.secret_number):
                return "Você está chegando mais perto!"
            else:
                return "Você está se afastando..."
        return ""

def plot_attempts(agent):
    plt.figure(figsize=(8,5))
    plt.plot(range(1, len(agent.history) + 1), agent.history, marker='o', linestyle='-')
    plt.axhline(y=agent.secret_number, color='r', linestyle='--', label='Número Secreto')
    plt.xlabel("Tentativas")
    plt.ylabel("Valor do Palpite")
    plt.title("Evolução das Tentativas do Jogador")
    plt.legend()
    plt.show()

# Escolha o nível de dificuldade (fácil, médio, difícil)
difficulty = input("Escolha a dificuldade (fácil, médio, difícil): ").strip().lower()
agent = GameAgent(difficulty)

while agent.state not in ["Acertou!", "Fim do jogo"]:
    try:
        guess = int(input("Digite um número entre 1 e 100: "))
        if 1 <= guess <= 100:
            print(agent.make_guess(guess))
        else:
            print("Por favor, digite um número válido entre 1 e 100.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

# Exibe o gráfico das tentativas ao final do jogo
plot_attempts(agent)

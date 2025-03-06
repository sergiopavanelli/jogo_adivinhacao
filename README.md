# 🎯 Jogo de Adivinhação - Máquina de Estados

Este é um jogo interativo de adivinhação baseado em uma **Máquina de Estados**. O jogador tenta adivinhar um número secreto dentro de um número limitado de tentativas. O jogo oferece diferentes níveis de dificuldade e fornece dicas para ajudar o jogador a acertar.

## 📌 Funcionalidades

✅ Modos de dificuldade: **Fácil (10 tentativas), Médio (7 tentativas), Difícil (5 tentativas)**  
✅ Feedback dinâmico: informa se o número secreto é maior ou menor  
✅ Dicas inteligentes: o jogo avisa se o jogador está **se aproximando ou se afastando** do número correto  
✅ Histórico de tentativas armazenado  
✅ **Gráfico interativo** com a evolução das tentativas  
✅ Validação de entrada para evitar erros  

## 🎮 Como Jogar

1. **Escolha o nível de dificuldade** digitando `"fácil"`, `"médio"` ou `"difícil"`.  
2. **Digite um número entre 1 e 100** para tentar adivinhar.  
3. O jogo fornecerá **feedback** sobre sua tentativa.  
4. Continue tentando até **acertar** ou atingir o limite de tentativas.  
5. No final, um **gráfico** mostrará a evolução das suas tentativas! 📊  

## 🖥️ Execução do Código

Este jogo pode ser executado no **Google Colab**, no **Jupyter Notebook** ou diretamente no **terminal Python**.  

### 📌 Dependências  
Certifique-se de ter a biblioteca **matplotlib** instalada para visualizar o gráfico:  
```bash
pip install matplotlib

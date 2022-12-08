class OitoRainhas:
    '''
        Desafio das Oito Rainhas. \n
        Feito por: Pedro Henrique Alves dos Santos
    '''

    turno = 0

    def __init__(self, x, y, x2 = 0, y2 = 0):
        self.x = x
        self.y = y
        self.tabuleiro = []
        self.contador_rainhas = 0

        self.criaTabuleiro(x2, y2)
        self.iniciar()


    def iniciar(self):
        ''' Inicia a validação e o preenchimento das Rainhas. '''
        for x in range(0, 8):
            for y in range(0, 8):
                if self.validacaoCasa(x, y):
                    self.adicionaRainha(x, y)



    def adicionaRainha(self, x, y):
        ''' Método que adiciona a Rainha. '''
        self.tabuleiro[x][y] = 1
        self.contador_rainhas += 1

    def validacaoCasa(self, x, y):
        ''' Utiliza todos os métodos de validação para retornar e preencher caso não passe na validação. '''
        if not self.analisaLinha(self.tabuleiro[x]):
            if not self.analisaColuna(y):
                if not self.analisaDiagonalSuperior(x, y):
                    if not self.analisaDiagonalInferior(x, y):
                        return True

        if not self.tabuleiro[x][y] == 1:
            self.tabuleiro[x][y] = 2
        return False


    def criaTabuleiro(self, x2, y2):
        '''
            Método que cria o tabuleiro do jogo.\n
            x2 e y2 -> servem como auxilio para a repetição e tentativa de outras probabilidades.
        '''
        for x in range(0, 8):
            self.tabuleiro.append([])
            for y in range(0, 8):
                if(self.x == x and self.y == y):
                    self.tabuleiro[x].append(1)
                    self.contador_rainhas += 1
                else:
                    self.tabuleiro[x].append(0)
        if (not (x2 == 0 and y2 == 0)) and self.validacaoCasa(x2, y2):
            self.tabuleiro[x2][y2] = 1
            self.contador_rainhas += 1

    def analisaLinha(self, linha):
        ''' Método que verifica se há Rainhas na linha. '''

        return True if 1 in linha else False

    def analisaColuna(self, col):
        ''' Método que verifica se há Rainhas na coluna. '''

        coluna = []
        for x in self.tabuleiro:
            coluna.append(x[col])
        return True if 1 in coluna else False

    #Análise da diagonal superior onde o x não é alterado para ser reutilizado, assim como na Inferior
    def analisaDiagonalSuperior(self, x, y):
        ''' Método que verifica se há Rainhas na diagonal superior. '''

        x2 = x
        y2 = y
        diagonal = []

        while True:     # While's que separam as diagonais e transformam num array
            if x2 < 0 or y2 < 0:
                diagonal.reverse()
                x2 = x
                y2 = y
                break
            diagonal.append(self.tabuleiro[x2][y2])
            x2 -= 1
            y2 -= 1
        while True:
            if x2 >= 7 or y2 >= 7:
                break
            x2 += 1
            y2 += 1
            diagonal.append(self.tabuleiro[x2][y2])
        return True if 1 in diagonal else False

    def analisaDiagonalInferior(self, x, y):
        ''' Método que verifica se há Rainhas na diagonal inferior. '''

        x2 = x
        y2 = y
        diagonal = []

        while True:
            if x2 > 7 or y2 < 0:
                diagonal.reverse()
                x2 = x
                y2 = y
                break
            diagonal.append(self.tabuleiro[x2][y2])
            x2 += 1
            y2 -= 1
        while True:
            if x2 <= 0 or y2 >= 7:
                break
            x2 -= 1
            y2 += 1
            diagonal.append(self.tabuleiro[x2][y2])
        return True if 1 in diagonal else False

    def getOitoRainhas(self):
        ''' Método que retorna o resultado final do objeto. '''
        return [self.tabuleiro, self.contador_rainhas]

melhores = []

#input's das posições iniciais
posX = 0
posY = 0

print("Bem vindo ao 'Oito Rainhas'!")

while True:
    print("Informe as posições do tabuleiro")
    posX = int(input("Escolha a posição X: ")) - 1
    posY = int(input("Escolha a posição Y: ")) - 1
    if (posY < 0 and posY > 9) and (posX < 0 and posX > 9):
        print("Fora do Limite..")
    else:
        break

for x in range(0, 8):
    for y in range(0, 8):
        melhores.append(OitoRainhas(posX, posY, x, y).getOitoRainhas())

# Variáveis com x às vezes são utilizadas como auxilio.
melhores = sorted(melhores, key=lambda x: x[1], reverse=True) # Coloca em ordem Decrescente todas as possibilidades a partir da quantidade de Rainhas



# Visualização


melhor = []
linhas = []


print("\n")
print("\n")

for linha in melhores[0][0]:
    for coluna in linha:
        linhas.append('0' if coluna == 2 else '1')
    print('--'.join(linhas))
    linhas = []

print("Quantidade de Rainhas: {}".format(melhores[0][1]))

# Visualização
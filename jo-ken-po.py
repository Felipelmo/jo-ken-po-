from random import randint
itens = ('Rock', 'Paper', 'Scissor')
computador = randint(0, 2)
jogador = int(input(' [0] - Rock\n [1] - Paper\n [2] - Scissor\n'))
print('JO')
print('KEN')
print('PO!')
print('-=-' *11)
print('Did you chose... {}' .format(itens[jogador]))
print('Your chalenger chose... {}' .format(itens[computador]))
print('-=-' *11)
if jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
   print("WIN!!!.(?????)WIN!!!")
elif jogador == 0 and computador == 0 or jogador == 1 and computador == 1 or jogador == 2 and computador == 2:
   print("Draw.(???)Draw.")
elif jogador == 0 and computador == 1 or jogador == 1 and computador == 2 or jogador == 2 and computador == 0:
   print("lose...(-?-)lose...")

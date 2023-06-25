preco = float(input('Qual o preço do produto? R$'))
desconto = preco * 0.05
valor_final = preco - desconto
print('Esse produto com 5% de desconto terá o valor de R${:.2f}'.format(valor_final))

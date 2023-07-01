print('{:=^40}'.format(' LOJA '))
preco_normal = float(input('Preço das compras: '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preco_normal - (preco_normal * 10 / 100)
elif opcao == 2:
    total = preco_normal - (preco_normal * 5 / 100)
elif opcao == 3:
    total = preco_normal
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco_normal + (preco_normal * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preco_normal
    print('OPÇÃO INVÁLIDA. Tente novamente.')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco_normal, total))

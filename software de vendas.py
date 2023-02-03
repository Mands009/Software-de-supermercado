#funcionamento do software em python

p1 = float(input("Digite um produto: "))
p2 = float(input("Digite um produto: "))
p3 = float(input("Digite um produto: "))
p4 = float(input("Digite um produto: "))
p5 = float(input("Digite um produto: "))
soma = (p1+p2+p3+p4+p5)
pagamento = float(input("Qual é a forma de pagamento? "))


print ("Soma: ", soma)
print ("Forma de pagamento: ", pagamento)


if pagamento == "dinheiro":
    print("total a pagar: ", soma, "troco: ", troco)
elif pagamento == "cartão débito":
    print("insira seu cartão e digite a senha.", soma)
    print("pagamento autorizado")
elif pagamento == "cartão crédito":
    print("insira seu cartão e digite a senha.", soma)
    print("pagamento autorizado")
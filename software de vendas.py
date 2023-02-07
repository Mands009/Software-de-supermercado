#funcionamento do software em python

qtd = 0
tecla = "c"
total = 0.0

while (qtd <=10 and tecla!="p"):
    preço = float(input("Preço: "))
    total = total + preço
    qtd = qtd + 1
    tecla = input("pressione qualquer tecla para continuar ou 'p' para parar...")
print("O total da compra é ", total)

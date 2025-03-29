# A partir do valor total da compra determina o deconto

print("Olá! O programa irá verificar qual desconto será aplicado conforme o valor total da compra.")

total = float(input("Digite o valor total da compra: "))

if total < 100:
    print(f"O desconto aplicado na compra R$ {total} será de 5%!")
elif total >= 100 and total <= 500:
    print(f"O desconto aplicado na compra R$ {total} será de 10%!")
else:
    print(f"O desconto aplicado na compra R$ {total} será de 15%!")

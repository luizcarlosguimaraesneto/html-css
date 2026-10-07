nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))

if idade >= 18:
    print(f"{nome}, você é maior de idade.")
else:
    print(f"{nome}, você é menor de idade.")
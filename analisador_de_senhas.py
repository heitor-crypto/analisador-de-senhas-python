print("=== ANALISADOR DE SENHAS ===")

senha = input("Digite sua senha: ")
print("Boa, senha recebida")

quantidade = len(senha)
print("Quantidade de caracteres", quantidade)


tem_numero = False

for caractere in senha:
    if caractere.isdigit():
        tem_numero = True

if tem_numero:
    print("Tem números")
else:
    print("Não tem números")   


tem_maiuscula = False

for caractere in senha:
    if caractere.isupper():
        tem_maiuscula = True

if tem_maiuscula:
    print("Tem maiuscula") 
else:
    print("Não tem maiusculas")


tem_minuscula = False

for caractere in senha:
    if caractere.islower():
        tem_minuscula = True

if tem_minuscula:
    print("Tem minuscula")
else:
    print("Não tem minuscula")


tem_simbolos = False

for caractere in senha:
    if not caractere.isalnum() and not caractere.isspace():
        tem_simbolos = True

if tem_simbolos:
    print("Tem simbolos")

else:
    print("Não tem símbolos")


pontos = 0

if quantidade >= 12:
    pontos += 20

if tem_numero:
    pontos += 20


if tem_maiuscula:
    pontos += 20

if tem_minuscula:
    pontos += 20

if tem_simbolos:
    pontos += 20


print("Pontuação:", pontos)

if pontos <= 40:
    print("Senha fraca")

elif pontos <= 80:
    print("Ok, mas dá pra melhorar")
else:
    print("Ótima senha!")        
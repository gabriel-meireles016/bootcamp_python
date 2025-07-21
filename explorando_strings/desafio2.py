# Entrada do usuário
#email = input().strip()

email = "usuario@gmail.com"

# TODO: Verifique as regras do e-mail:

dom1 = "@gmail.com"
dom2 = "@outlook.com"

if email[0] == "@" or email[-1] == "@":
    print("E-mail inválido")
elif " " in email:
    print("E-mail inválido")
elif dom1 in email or dom2 in email:
    print("E-mail válido")


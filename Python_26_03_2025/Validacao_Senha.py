#Validação de senha

import re 

print("Olá! O programa irá verificar se a senha informada atinge os requesitos.\n")

senha = input("Digite uma senha:")

if len(senha) < 8:
  print("A senha deve conter no mínimo 8 caracteres! Tente novamente.")
elif not re.search(r"[A-Z]", senha):
  print ("A senha  deve conter pelo menos uma letra maiúscula! Tente novamente.")
elif not re.search (r"[a-z]", senha):
  print("A senha deve conter pelo menos uma letra minúscula! Tente novamente.")
elif not  re.search(r"\d", senha):
    print("A senha deve conter pelo menos um número! Tente novamente.")
elif not re.search(r"[^A-Za-z0-9]", senha):
    print("A senha deve ter pelo menos um caractere especial! Tente novamente.")
else:
    print("Senha válida!")
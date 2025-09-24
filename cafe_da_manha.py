print("1. Ovos")
print("2. Panquecas")
print("3. Croissant")
print("4. Aveia")
EscolhaPrincipal = int(input("Escolha um item de café da manhã: "))
if (EscolhaPrincipal == 2):
  Refeicao = "panquecas"
elif (EscolhaPrincipal == 3):
  Refeicao = "croissant"
if (EscolhaPrincipal == 1):
  print("1. Torrada de Trigo")
  print("2. Pão Francês")
  print("3. Torrada de centeio")
  print("4. Panquecas")
  pao = int(input("Escolha um tipo de pão: "))
  if (pao == 1):
    print("Você escolheu ovos com torrada de trigo.")
  elif (pao == 2):
    print("Você escolheu ovos com pão francềs.")
  elif (pao == 3):
    print("Você escolheu ovos com torrada de centeio.")
  elif (pao == 4):
    print("Você escolheu ovos com panquecas.")
  else:
    print("Temos ovos, mas não esse tipo de pão.")
elif (EscolhaPrincipal == 2) or (EscolhaPrincipal == 3):
  print("1. Mel de abelha")
  print("2. Calda de morango")
  print("3. Calda de chocolate")
  cobertura = int(input("Escolha uma cobertura: "))
  if (cobertura == 1):
    print("Você escolheu " + Refeicao + " com mel de abelha.")
  elif (cobertura == 2):
    print("Você escolheu " + Refeicao + " com calda de morango.")
  elif (cobertura == 3):
    print("Você escolheu " + Refeicao + " com calda de chocolate.")
  else:
    print("Nós temos " + Refeicao + ", mas não essa cobertura.")
elif (EscolhaPrincipal == 4):
  print("Você escolheu aveia.")
else:
  print("Nós não servimos esse item de café da manhã!")

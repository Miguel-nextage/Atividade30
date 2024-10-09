# crie uma funcao que calcule a nota a media de 3 notas em seguida verifique se ele esta aprovado ou reprovado para notas acima de 7

notas = []

for i in range(3):
    N = float(input(f"Sua {i + 1} nota"))
    notas.append(N)
    
def media(notas):
    result = sum(notas) / 3
    return result

def aprovado(media):
    if media >= 7:
        return "Aprovado"

    else:
        return "Aprovado"
  
mediaR = media(notas)
aprovadoR = aprovado(mediaR)

print(f"""Sua média é {mediaR}
Você está {aprovadoR}""")
import random

def gerar_instrucao():
    instrucoes = ["Em uma missão no planeta Azul", "Durante uma expedição no planeta Venom", 
                  "Explorando o planeta Galatron", "Em uma jornada até o planeta Rosa",
                  "Nas profundezas do espaço, no planeta Solian"]
    return random.choice(instrucoes)

def gerar_desenvolvimento():
    desenvolvimento = ["um estranho sinal de vida foi detectado", "uma civilização antiga foi encontrada", 
                        "uma tempestade cósmica começou a se formar", "um misterioso templo alienígena foi descoberto", 
                        "um raro cristal de energia foi encontrado"]
    return random.choice(desenvolvimento)

def gerar_final():
    finais = ["e a equipe decidiu investigar mais a fundo.", 
              "e a descoberta mudou tudo o que sabíamos sobre o universo.", 
              "e foi necessário uma fuga rápida para evitar o perigo.", 
              "e a equipe levou um artefato de volta para a Terra.", 
              "e a comunicação foi perdida, deixando tudo em mistério."]
    return random.choice(finais)

def gerar_historia():

    introducao = gerar_instrucao()
    desenvolvimento = gerar_desenvolvimento()
    final = gerar_final()

    historia = f"{introducao}  {desenvolvimento}  {final}"
    return historia


if __name__ == "__main__":
    print(gerar_historia())
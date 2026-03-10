import numpy as np
import model

def gerar_array_medias(materias):
    medias = []
    for materia in materias:
        medias.append(materia.media)
    
    return np.array(medias, np.float32)

def gerar_array_nomes(materias):
    nomes = []
    for materia in materias:
        nomes.append(materia.nome)
    
    return np.array(nomes, np.object_)

def exibir_array_medias(materias, hs):
    if not materias:
        print("Nenhuma disciplina registrada! \n")
        model.Menu(hs)
    
    medias = gerar_array_medias(materias)

    print(f"Medias: {medias} \nDType: {medias.dtype} \nFormato: {medias.shape}")
    model.Menu(hs)

def gerar_ranking_medias(materias, hs):
    if not materias:
        print("Nenhuma disciplina registrada! \n")
        model.Menu(hs)
    nomes = gerar_array_nomes(materias)
    medias = gerar_array_medias(materias)

    indexes = np.argsort(medias)[::-1]

    for i in range(indexes.size):
        print(f"{nomes[indexes[i]]}: Media {medias[indexes[i]]:.2f}")

    model.Menu(hs)

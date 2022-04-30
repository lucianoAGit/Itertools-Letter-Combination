from itertools import product 

#Funcao que retorna o cartesiano dos digitos com base na lista de letras
def cartesiano(n):
    
    lista_teclado = [["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],
                 ["t","u","v"],["w","x","y","z"]]
    
    #Quebra o numero em 2 digitos
    digito = [int(a) for a in str(n)]
    
    #Se for um unico digito o cartesiano e ele mesmo
    if (len(digito) == 1):
        print(lista_teclado[digito[0]-2])
        
    #Verifica se o digito e valido
    elif (digito[0] == 1 or digito[1] == 1 or digito[0] == 0 or digito[1] == 0):
        print("Numero digitado invalido para o produto cartesiano")
    
    else:
        print(list(product(lista_teclado[digito[0]-2],lista_teclado[digito[1]-2])))

#Entrada dos digitos
cartesiano(input('Por favor digite o numero: '))
arreglo = [4,2,4,3,2,4,1]
frec = {}
for num in arreglo:
    if num in frec:
        frec[num] += 1
    else:
        frec[num] = 1
for num in frec:
    if frec[num] > 1:
         print(f"El número {num} se repite {frec[num]} veces.")



recorrido = [2,14,6,11,8,15,7]
target = 9 
for s1 in range(len(recorrido)):
    for s2 in range(s1 +1, len(recorrido)):
        if recorrido[s1] + recorrido[s2] == target:
            print(f"Los números {recorrido[s1]} y {recorrido[s2]} suman {target}.")
        else:
            print(f"Los números {recorrido[s1]} y {recorrido[s2]} no suman {target}.")




        



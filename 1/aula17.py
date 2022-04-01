'Curso Python #17 - Listas (Parte 1)'
#num = (2, 5, 9, 1) #tupla
num = [2, 5, 9, 1] #lista
num[2] = 3
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
num.insert(2, 2)
print(num)
num.pop()
print(num)
num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')
print(num)

num = [2, 4, 5, 3, 2, 4]
num.remove(2)
print(num)
if 8 in num:
    num.remove(8)
print(num)

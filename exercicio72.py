#def multi(x, y, z):
#    print(x * y * z)
#    total = multi(x * y * z)
#    return total
#multi(1, 2, 3)

def mult(*args):
    total = 0
    for number in args:
        total +=  number
    return total

conta = mult(10, 3, 4)
print(conta)
print(10 + 3 + 4)

def nig(numero):
    return numero % 2 == 0

print(nig(2))


def par_ou_impar(number):
    conta = number % 2 == 0

    if conta:
        return f"O número '{number}' é par."
    return f"O número '{number}' é ímpar."

print(par_ou_impar(2))
print(par_ou_impar(3))
print(par_ou_impar(7))
print(par_ou_impar(10))
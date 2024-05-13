def factorial(n):
    if type(n) is not int:
        raise ValueError("N debe ser un número entero")
    elif n<0:
        raise ValueError("N debe ser mayor a 0")
    elif n<=1:
        return 1
    else:
        return factorial(n-1)*n
factorial(5)
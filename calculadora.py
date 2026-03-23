def dividir(a, b):
    if b == 0:
        return "Error: division entre cero"
    return a / b

if __name__ == "__main__":
    resultado = dividir(15, 3)
    print("El resultado de la division es:", resultado)

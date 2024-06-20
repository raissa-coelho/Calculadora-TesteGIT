from calculadora import Calculadora

def operação(calc):
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    
    operacao = input("Escolha a operação (+, -, *, /): ")
    
    if operacao == '+':
        resultado = calc.adicionar(a, b)
    elif operacao == '-':
        resultado = calc.subtrair(a, b)
    elif operacao == '*':
        resultado = calc.multiplicar(a, b)
    elif operacao == '/':
        resultado = calc.dividir(a, b)
    else:
        print("Operação inválida.")
        return

    print(f"O resultado de {a} {operacao} {b} é: {resultado}")

def main():
    calc = Calculadora()

    print("Calculadora Simples")
    print("===================")

    while True:
        print("Opcções: ")
        print("1 - Realizar operação")
        print("2 - Sair")
        op = input("Escolha uma opção: ")
        if op == '1':
            operação(calc)
        elif op == '2':
            break
        else:
            print("Inválido")
        
if __name__ == "__main__":
    main()

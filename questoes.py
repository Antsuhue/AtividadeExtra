def Ex1(n1, n2, n3, n4):
    #nota1 = float(input("informe a primeira nota -> "))
    #nota2 = float(input("informe a segunda nota -> "))
    #nota3 = float(input("informe a terceira nota -> "))
    #nota4 = float(input("informe a quarta nota -> "))
    
    media = (n1 + n2 + n3 + n4)/4

    if media >= 7:
        return f"sua média foi {media} você foi aprovado!"
    else:
        return f"sua média foi {media} você foi reprovado!"

def Ex2(n1, n2):
    #nota1 = float(input("informe a primeira nota -> "))
    #nota2 = float(input("informe a segunda nota -> "))
    
    media = (n1 + n2)/2

    if media >= 7:
        return f"Aprovado"
    elif media >= 4 and media < 7:
        return f"Exame"
    else:
        return f"Reprovado"

def Ex3(n1, n2):
    #n1 = float(input("informe o primeiro valor -> "))
    #n2 = float(input("informe o segundo valor -> "))

    if n1 > n2:
        return n2
    else:
        return n1

def Ex4(n1, n2, n3):
    #n1 = float(input("informe o primeiro valor -> "))
    #n2 = float(input("informe o segundo valor -> "))
    #n3 = float(input("informe o terceiro valor -> "))

    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3

def Ex5(n1, n2, op):
    #n1 = float(input("informe o primeiro valor -> "))
    #n2 = float(input("informe o segundo valor -> "))
    #print("1 - para média dos valores")
    #print("2 - para diferença do maior para o menor")
    #print("3 - para produto dos dois números")
    #print("4 - para divisão do primeiro pelo segundo")
    #op = int(input("informe o código da operação -> "))
    result = 0

    if op == 1:
        result = (n1 + n2) / 2
        return result
    elif op == 2:
        if n1 > n2:
            result = n1 - n2
            return result
        else:
            result = n2 - n1
            return result
    elif op == 3:
        return f"O prduto do primeiro valor é {n1 **2} e do segundo {n2 **2}"
    elif op == 4:
        if n2 != 0:
            return n1 / n2
        else:
            return f"Segundo valor infomado foi 0"
    else:
        return "Código informado é inválido!"

def Ex6(n1, n2, op):
    #n1 = float(input("informe o primeiro valor -> "))
    #n2 = float(input("informe o segundo valor -> "))
    #print("1 - para média dos valores")
    #print("2 - para diferença do maior para o menor")
    #print("3 - para produto dos dois números")
    #op = int(input("informe o código da operação -> "))
    result = 0

    if op == 1:
        result = (n1 + n2) / 2
        return result
    elif op == 2:
        if n1 > n2:
            result = n1 - n2
            return result
        else:
            result = n2 - n1
            return result
    elif op == 3:
        return f"O prduto do primeiro valor é {n1 **2} e do segundo {n2 **2}"
    
    else:
        return "Erro!"

def Ex6(n1, n2, op):
    #n1 = float(input("informe o primeiro valor -> "))
    #n2 = float(input("informe o segundo valor -> "))
    #print("1 - para média dos valores")
    #print("2 - para diferença do maior para o menor")
    #print("3 - para produto dos dois números")
    #op = int(input("informe o código da operação -> "))
    result = 0

    if op == 1:
        result = (n1 + n2) / 2
        return result
    elif op == 2:
        if n1 > n2:
            result = n1 - n2
            return result
        else:
            result = n2 - n1
            return result
    elif op == 3:
        return f"O prduto do primeiro valor é {n1 **2} e do segundo {n2 **2}"
    
    else:
        return "Erro!"

def Ex7(sal):
    #sal = float(input("informe o primeiro valor -> "))
    reajuste = 0
    if sal < 500:
        reajuste = (sal * 0.30) + sal
        return reajuste
    else:
        return "Seu salário não será reajustado!"

def Ex8(sal):
    #sal = float(input("informe o primeiro valor -> "))
    reajuste = 0
    if sal <= 300:
        reajuste = (sal * 0.35) + sal
        return reajuste
    else:
        reajuste = (sal * 0.15) + sal
        return reajuste

def Ex9(saldoMedio):
    #salMedio = float(input("informe o primeiro valor -> "))
    reajuste = 0
    if saldoMedio > 400:
        reajuste = (saldoMedio * 0.30) + saldoMedio
        return reajuste
    elif saldoMedio > 300 and saldoMedio <= 400:
        reajuste = (saldoMedio * 0.25) + saldoMedio
        return reajuste    
    elif saldoMedio > 200 and saldoMedio <= 300:
        reajuste = (saldoMedio * 0.20) + saldoMedio
        return reajuste
    else:
        reajuste = (saldoMedio * 0.10) + saldoMedio
        return reajuste
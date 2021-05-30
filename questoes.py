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

def Ex10(custoVeiculo):
    #custoVeiculo = float(input("Informe o custo de fábrica -> "))
    distribuidor = 0
    imposto = 0

    if custoVeiculo < 12000:
        distribuidor = 0.05 * custoVeiculo
        return custoVeiculo + distribuidor
    elif custoVeiculo >= 12000 and custoVeiculo <= 250000:
        distribuidor = 0.10 * custoVeiculo
        imposto = 0.15 * custoVeiculo
        return custoVeiculo + (distribuidor + imposto)
    else:
        distribuidor = 0.15 * custoVeiculo
        imposto = 0.20 * custoVeiculo
        return custoVeiculo + (distribuidor + imposto)

def Ex11(sal):
    #sal = float(input("informe o valor do salário -> "))
    
    percentual = 0

    if sal <= 300:
        percentual = 0.15
        return sal + (sal*percentual)
    elif sal > 300 and sal <= 600:
        percentual = 0.10
        return sal + (sal*percentual)
    elif sal > 600 and sal <= 900:
        percentual = 0.05
        return sal + (sal*percentual)
    else:
        return sal

def Ex12(sal):
    #sal = float(input("informe o valor do salário -> "))
    
    imposto = 0.07

    if sal <= 350:
        return 100 + (sal - (sal*imposto))
    elif sal > 350 and sal <= 600:
        return 75 + (sal - (sal*imposto))
    elif sal > 600 and sal <= 900:
        return 50 + (sal - (sal*imposto))
    else:
        return 35 + (sal - (sal*imposto))

def Ex13(precoProduto):
    #precoProduto = float(input("informe o valor do produto -> "))
    novoPreco = 0
    if precoProduto <= 50:
        novoPreco = precoProduto + (precoProduto * 0.05)
    elif precoProduto > 50 and precoProduto <= 100:
        novoPreco = precoProduto + (precoProduto * 0.10)
    else:
        novoPreco = precoProduto + (precoProduto * 0.15)

    if novoPreco <= 80:
        return f"{novoPreco} Barato"
    elif novoPreco > 80 and novoPreco <= 120:
        return f"{novoPreco} Normal"
    elif novoPreco > 120 and novoPreco <= 200:
        return f"{novoPreco} Caro"
    else:
        return f"{novoPreco} Muito Caro"

def Ex14(sal):
    #sal = float(input("informe o valor do salário -> "))
    
    percentual = 0

    if sal <= 300:
        percentual = 0.50
        return sal + (sal*percentual)
    elif sal > 300 and sal <= 500:
        percentual = 0.40
        return sal + (sal*percentual)
    elif sal > 500 and sal <= 700:
        percentual = 0.30
        return sal + (sal*percentual)
    elif sal > 700 and sal <= 800:
        percentual = 0.20
        return sal + (sal*percentual)
    elif sal > 800 and sal <= 1000:
        percentual = 0.10
        return sal + (sal*percentual)
    else:
        percentual = 0.05
        return sal + (sal*percentual)

def Ex15(valor, op):
    #valor = float(input("informe o valor a ser investido -> "))
    #print("Escolha o tipo de fundo de investimento")
    #print("Sendo 1 para Poupança e 2 para Fundos de renda fixa")
    #op = float(input("-> "))
    rendimento = 0

    if op == 1:
        rendimento = 0.03
    elif op == 2:
        rendimento = 0.04
    else:
        return "Opção inválida!"
    
    return f"Renderá ao mês {valor*rendimento}"

def Ex16(precoProduto):
    #precoProduto = float(input("informe o valor do produto -> "))

    desconto = 0
    
    if precoProduto > 30 and precoProduto <= 100:
        desconto = 0.10
    elif precoProduto > 100:
        desconto = 0.15
    
    return precoProduto - (precoProduto * desconto)

def Ex17(senha):
    #senha = input("Informe a senha para o acesso -> ")

    if senha == "4531":
        return "Acesso permitido!"
    else:
        return "Acesso negado!"
    
def Ex18(idade):
    #idade = int(input("Informe a idade -> "))
    
    if idade >= 18:
        return "Maior de idade!"
    else:
        return "Menor de idade!"

def Ex19(altura, sexo):
    #altura = float(input("Informe a sua altura -> "))
    #sexo = input("Informe a idade (M/F) -> ")
    peso_ideal = 0

    if sexo.upper() == "M":
        peso_ideal = (72.7 * altura) - 58
    elif sexo.upper() == "F":
        peso_ideal = (62.1 * altura) - 44.7    
    else:
        return "Sexo inválido!"

    return f"Seu peso ideal é {peso_ideal:.2f}Kg"

def Ex20(idade):
    #idade = int(input("Informe a idade -> "))
    categoria = ""
    if idade >= 5 and idade <= 7:
        categoria = "Infantil"

    elif idade >= 8 and idade <= 10:
        categoria = "Juvenil"

    elif idade >= 11 and idade <= 15:
        categoria = "Adolescente"

    elif idade >= 16 and idade <= 30:
        categoria = "Adulto"
    
    elif idade > 30:
        categoria = "Sênior"

    else:
        return "Não possui categoria!"

    return f"Sua categoria é {categoria}"

def Ex21(codOrigem):

    categorias = {
        "procedencia": {
            "Sul": [1],
            "Norte": [2],
            "Leste": [3],
            "Oeste": [4],
            "Nordeste": [5, 6],
            "Sudeste": [7, 8, 9],
            "Centro-Oeste": []
        }
    }
    for i in range(10,20):
        categorias["procedencia"]["Centro-Oeste"].append(i)

    for t in range(21,30):
        categorias["procedencia"]["Nordeste"].append(t)

    for x in categorias["procedencia"]:
        for y in categorias["procedencia"][x]:
            if codOrigem == y:
                return f"{x}"

def Ex22():
    

    
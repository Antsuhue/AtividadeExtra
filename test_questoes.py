import questoes
#Arquivo de teste das questões
def test_ex1():
    assert questoes.Ex1(8,8,8,8) == "sua média foi 8.0 você foi aprovado!"
    assert questoes.Ex1(2,2,2,2) == "sua média foi 2.0 você foi reprovado!"

def test_ex2():
    assert questoes.Ex2(10, 10) == "Aprovado"
    assert questoes.Ex2(5, 5) == "Exame"
    assert questoes.Ex2(1, 1) == "Reprovado"

def test_ex3():
    assert questoes.Ex3(1,2) == 1
    assert questoes.Ex3(2,1) == 1

def test_ex4():
    assert questoes.Ex4(1, 2, 3) == 3
    assert questoes.Ex4(1, 3, 2) == 3
    assert questoes.Ex4(2, 1, 3) == 3
    assert questoes.Ex4(2, 3, 1) == 3
    assert questoes.Ex4(3, 1, 2) == 3
    assert questoes.Ex4(3, 2, 1) == 3

def test_ex5():
    assert questoes.Ex5(5, 5, 1) == 5
    assert questoes.Ex5(2, 1, 2) == 1
    assert questoes.Ex5(1, 2, 2) == 1
    assert questoes.Ex5(2, 2, 3) == "O prduto do primeiro valor é 4 e do segundo 4"
    assert questoes.Ex5(2, 2, 4) == 1
    assert questoes.Ex5(2, 0, 4) == "Segundo valor infomado foi 0"
    assert questoes.Ex5(2, 2, 5) == "Código informado é inválido!"

def test_ex6():
    assert questoes.Ex6(2, 1, 2) == 1
    assert questoes.Ex6(5, 5, 1) == 5
    assert questoes.Ex6(1, 2, 2) == 1
    assert questoes.Ex6(2, 2, 3) == "O prduto do primeiro valor é 4 e do segundo 4"
    assert questoes.Ex6(2, 2, 5) == "Erro!"

def test_ex7():
    assert questoes.Ex7(300) == 390
    assert questoes.Ex7(1000) == "Seu salário não será reajustado!"

def test_ex8():
    assert questoes.Ex8(300) == 405
    assert questoes.Ex8(1000) == 1150

def test_ex9():
    assert questoes.Ex9(100) == 110
    assert questoes.Ex9(250) == 300
    assert questoes.Ex9(400) == 500
    assert questoes.Ex9(1000) == 1300
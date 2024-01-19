nome= input("Qual seu nome?")

print("Ola", nome, ", seja bem vindo a calculadora.\nSelecione a operacao que deseja realizar")

operacao= int(input("Para somar (+) digite 1\nPara subtrair (-) digite 2\nPara multiplicar (x) digite 3\nPara dividir (/) digite 4\n"))

operacao>= 5
while operacao != 2:
    print("Opcao invalida, digite novamente")
    break
operacao

num1= int(input("Agora digite o primeiro valor da operacao\n"))
          
num2= int(input("Agora digite o segundo valor da operacao\n"))

if operacao== 1:
    resultado1 = num1 + num2
    print ("Seu resultado e", resultado1)

elif operacao== 2:
    resultado2= num1 - num2
    print ("Seu resultado e", resultado2)
    
elif operacao== 3:
    resultado3= num1 * num2
    print ("Seu resultado e", resultado3)
    
elif operacao== 4:
    resultado4= num1 / num2
    print ("Seu resultado e", resultado4)
    
else:
    print("Opcao invalida, digite novamente")
    
    
    
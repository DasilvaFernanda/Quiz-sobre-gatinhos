print (" Bem vindo ao quiz sobre gatinhos!")
answer_user= input("vamos lá? (S/N)")
if answer_user!= "s":

    score: 0

    print("começando...")
    print ("quanto tempo vive um gato? /n (A) 12-18 anos /n  (B) 15-18 /n (C) 10-13 anos  /n")
answer_1 = input ("Resposta:")

if answer_1 == "A":

    print ("correto!")
else:
    print ("incorreto!")
    score = score +10

print ("gatos gostam de sorvete? /n (A) sim /n (B) não /n (C) com certeza /n")
answer_2 = input ("resposta:")

if answer_2 == "A":

    print ("correto!")
else:
    print ("incorreto!")
    score = score +10


    print(f"Quiz terminou... Pontuação: {score}/2")
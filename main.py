import turtle
import random

janela = turtle.Screen()
janela.setup(500,500) #Tamanho da janela
turtle.title ("Jogo da Tartaruga") #Título do jogo 

#Variaveis de coordenadas 
xt=0 
yt=0
xv=0
yv=0
xl=0
yl=0

#variaveis contador de vidas/pontos
contvidas=3
contpontos=0

#criação do placar de vidas 
placarv = turtle.Turtle() #criar objeto (tartaruga)
placarv.pencolor("white") # borda branca
placarv.fillcolor("green") # interior verde
placarv.shape("circle") # formato circular
placarv.shapesize(0.5) #tamanho da tartaruga
placarv.penup() #tirar linha de desenho 
placarv.speed(0) #velocidade máxima da tartaruga
placarv.hideturtle() #apagar o forma (tartaruga)

#criação do placar de pontos
placarl = turtle.Turtle()
placarl.pencolor("white") # borda branca
placarl.fillcolor("red") # interior vermelho
placarl.shape("circle")
placarl.shapesize(0.5)
placarl.penup()
placarl.speed(0)
placarl.hideturtle()

#contador de pontos de frutas do placar
pontos = turtle.Turtle()
pontos.pencolor("white") # borda branca
pontos.fillcolor("green") # interior verde
pontos.shape("circle")
pontos.shapesize(0.8)
pontos.penup()
pontos.speed(0)
pontos.hideturtle()

#contador para diminuir vidas do placar
vidas = turtle.Turtle()
vidas.pencolor("white") # borda branca
vidas.fillcolor("green") # interior verde
vidas.shape("circle")
vidas.shapesize(0.8)
vidas.penup()
vidas.speed(0)
vidas.hideturtle()

#criar personagem
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.speed(0)
tartaruga.penup()
tartaruga.pencolor("black") # borda preta
tartaruga.fillcolor("white") # interior azul

#criar veneno
veneno = turtle.Turtle()
veneno.pencolor("white") # borda branca
veneno.fillcolor("green") # interior verde
veneno.shape("circle")
veneno.shapesize(0.8)
veneno.penup()
veneno.speed(0)

#criar fruta
life = turtle.Turtle()
life.pencolor("white") # borda branca
life.fillcolor("red") # interior vermelho
life.shape("circle")
life.shapesize(0.8)
life.penup()
life.speed(0)

#levar tartaruga ao ponto inicial da arena
xt = -230
yt = -230
tartaruga.goto(xt, yt) # o comando .goto direciona você até a coordenada desejada
tartaruga.pendown() # Colocar linha de desenho
tartaruga.pensize(3) # largura da linha de desenho

#criando arena
tartaruga.begin_fill() # iniciando forma fechada
for i in range(4): # desenhando um quadrado
 tartaruga.forward(455)
 tartaruga.left(90) 
tartaruga.end_fill() #encerrando forma fechada

#voltar tartaruga para o ponto central
tartaruga.penup()
xt = 0
yt = 0
tartaruga.goto(xt, yt)

#coordenadas do placar
pontos.pencolor("black") # borda preta
vidas.pencolor("black") # borda preta
placarl.pencolor("black") # borda preta
placarv.pencolor("black") # borda preta
placarl.goto(-215, 230)
placarv.goto( 0, 230)
pontos.goto(-150,230)
vidas.goto(55,230)

#como escrever pontos e vidas dos placares
placarl.write("Pontos =", font=("Verdana",10, "normal"))
placarv.write("Vidas =", font=("Verdana",10, "normal"))


#coordenadas aleatorias do veneno e da fruta, dentro da área da arena
tartaruga.fillcolor("black")  
xl=random.randint(-220, 215) #coordenadas minimas e máximas da arena onde as frutas e veneno podem aparecer
yl=random.randint(-220, 215)
xv=random.randint(-220, 215)
yv=random.randint(-220, 215)

#variaveis auxiliares dos pontos e vidas
auxpontos=0
auxvidas=3

#Gameplay
i=True
while i == True: #("Tempo de gameplay", enquanto i for verdaeiro, o jogo acontece)

    if contvidas==0: # quando voce perder todas as vidas, o jogo acaba
            turtle.bye()


    if auxpontos != contpontos: #quando voce pega uma fruta, o numero que está no placar é apagado, para depois ser atualizado pela nova pontuação 
        pontos.clear()
        auxpontos = contpontos
    
    if auxvidas != contvidas:#quando voce pega um veneno, o numero de vidas que está no placar é apagado, para depois ser atualizado pela nova quantidade
        vidas.clear()
        auxvidas = contvidas
    
    pontos.write(contpontos, font=("Verdana",10, "normal")) #escreve novo valor do placar
    vidas.write(contvidas, font=("Verdana",10, "normal")) #escreve novo valor de vidas
    
    # comando para nao ocorrer da vida/veneno nascer em cima do personagem
    if xl == xt and yl ==yt: #se acontecer de a fruta nascer em cima da tartaruga, entrara no while abaixo, e so saira de la se receber uma coordenada diferente da tartaruga
        x=0
        while x < 1:
            if xl == xt and yl ==yt: 
                xl=random.randint(-220, 215) 
                yl=random.randint(-220, 215)
                
                x=0
            else:
                x=x+1

    if xv == xt and yv ==yt: #se acontecer do veneno nascer em cima da tartaruga, entrara no while abaixo, e so saira de la se receber uma coordenada diferente da tartaruga
        x=0
        while x < 1:
            if xv == xt and yv ==yt:
                xv=random.randint(-220, 215)
                yv=random.randint(-220, 215)
                x=0
            else:
                x=x+1

    life.goto(xl, yl) #definir posição da fruta
    veneno.goto(xv, yv) #definir a posição do veneno

#movimentação do personagem (tartaruga)
    def cima(): #clicando em w/seta pra cima, a tartaruga anda pra frente
        if tartaruga.xcor()>220: #colisão com a borda direita
            tartaruga.bk(10)
            
        
        if tartaruga.xcor()<-215: #colisão com a borda esquerda
            tartaruga.bk(10)
            
        
        if tartaruga.ycor()>220: #colisão com a borda superior
            tartaruga.bk(10)
            
        
        if tartaruga.ycor()<-215:#colisão com a borda inferior
            tartaruga.bk(10)
           

        tartaruga.fd(5)


    def baixo(): #clicando em s/seta pra baixo, a tartaruga anda para trás
        if tartaruga.xcor()>220: #colisão com a borda direita
            tartaruga.fd(10)
        
        if tartaruga.xcor()<-215: #colisão com a borda esquerda
            tartaruga.fd(10)
        
        if tartaruga.ycor()>220: #colisão com a borda superior
            tartaruga.fd(10)
        
        if tartaruga.ycor()<-215: #colisão com a borda inferior
            tartaruga.fd(10)

        tartaruga.bk(5)

    def esquerda(): #clicando em a/seta pra esquerda, a tartaruga gira no seu proprio eixo para a esquerda
        tartaruga.left(5)

    def direita(): #clicando em d/seta pra direita, a tartaruga gira no seu proprio eixo para a direita
        tartaruga.right(5)
        
    xt = tartaruga.xcor()
    yt = tartaruga.ycor()
    xt=int(xt) #pega o eixo x da tartaruga e transforma em um numero inteiro e armazenando em xt
    yt=int(yt) #pega o eixo y da tartaruga e transforma em um numero inteiro e armazenando em yt
    
#colisoes com a fruta
    if xt >= life.xcor()-20 and xt <= life.xcor()+20 and yt >= life.ycor()-20 and yt <= life.ycor()+20:
        xl=random.randint(-220, 215)
        yl=random.randint(-220, 215)
        life.goto(xl,yl) #quando acontece a colisão com a fruta, ela é teleportada para um novo local da arena
        contpontos=contpontos+1 #aumenta um ponto no placar
        

#colisoes com a veneno
    if xt >= veneno.xcor()-20 and xt <= veneno.xcor()+20 and yt >= veneno.ycor()-20 and yt <= veneno.ycor()+20:
        xv=random.randint(-220, 215)
        yv=random.randint(-220, 215)
        veneno.goto(xv,yv) #quando acontece a colisão com o veneno, ele é teleportada para um novo local da arena
        contvidas=contvidas-1 #diminui uma vida do placar    

#chama a função para definir as teclas de movimentação 
    turtle.onkeypress(cima,"Up")
    turtle.onkeypress(baixo,"Down")
    turtle.onkeypress(esquerda,"Left")
    turtle.onkeypress(direita,"Right")
    turtle.onkeypress(cima,"w")
    turtle.onkeypress(baixo,"s")
    turtle.onkeypress(esquerda,"a")
    turtle.onkeypress(direita,"d")
    turtle.listen()
        


janela.mainloop()

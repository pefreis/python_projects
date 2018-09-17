import turtle

def desenha_quadrado():    

    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(6)

    for i in range (36):
        for i in range(4):
            t.forward(100)
            t.right(90)
        t.right(10)
    


desenha_quadrado()

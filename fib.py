def genFibon(n):

    a = 1
    b = 1

    for i in range (n):
        yield a
        a,b = b,a+b

qtde_fibonacci = int(input())

output = ""
for num in genFibon(qtde_fibonacci):
    output+=str(num)+" "

print(output[:-1])
    

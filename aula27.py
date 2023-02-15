x = 1

def escopo():
    x = 19
    
    def nova():
        y = 3
        print(x, y)

    nova()
    print(x)

print(x)
escopo()    
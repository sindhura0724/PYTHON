
pop = 100000
rate = 0.1
for i in range(1,11):
    last_decade_pop = pop*(1+rate)
    pop = last_decade_pop
    print(i,last_decade_pop)

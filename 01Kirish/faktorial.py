# while operatori yotrdamida
def faktorial(N):
    i = 1
    fakt = 1
    while i != N+1:
        fakt = fakt*i
        i = i + 1
    return fakt

print(faktorial(10))

# for operatori yordamida
def faktorial_for(N):
    faktr = 1
    for i in range(N):
        faktr = faktr*(i+1)
    return faktr
print(faktorial_for(10))



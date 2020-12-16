f = 6
q = 0.5
prog = []
for i in range(1,5):
    if (f * q ** (i - 1)) >= 0.6:
        prog.append(f * q ** (i - 1))
print(prog)
print("S =",f * (1-q**len(prog))/(1-q))
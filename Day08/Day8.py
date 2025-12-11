def fix(p,o,f,F):
    if any([not F, p in f or o == 'acc']): return o,F
    f[p]=1
    return {'jmp':'nop','nop':'jmp'}[o],0

def run(i,f={}):
    os = {'nop': lambda p,r,v: (p+1,r), 'jmp': lambda p,r,v: (p+v,r), 'acc': lambda p,r,v: (p+1,r+v)}
    p,m,a,F=0,len(i),0,not(not f)
    while 1:
        i[p][2]=a; op,d,a=i[p]; op,F=fix(p,op,f,F); p,a=os[op](p,a,d)
        if not (p<m and i[p][2]==None): break
    return a,p<m

def p1(i):
    print(f'part1-short: {run(i)[0]}')

def p2(i):
    e,f=1,{-1:0}
    while e: a,e=run([x[:] for x in i],f)
    print(f'part2-short: {a}')

def s(fn):
    with open(fn) as f: i=[[o,int(d),None] for (o,d) in [s.strip().split() for s in f.readlines()]]
    p1([a[:] for a in i]) or p2(i)

f = s("day8.txt")

print(f)
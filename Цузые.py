w = "а р а В А а Р р а".lower().split()
print(*['%s %s' %(x, w.count(x)) for x in set(w)], sep='\n')

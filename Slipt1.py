line = 'the quick brown box jumps over the lazy dog'
words = line.split()
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
for i in stuff:
    print(i)
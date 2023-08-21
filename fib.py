import pprint
limit = 11
# this program is optimized to unroll loops and use globals for speed
# there must be a better way to do this. 
# Your hierarchical tree structure (nested dictionaries) goes here
tree = { # fibbonacci | prime | integers
} 
index = { #number -> factors
}
amax = 0  #the max numbe we saw so far

def ismax(x):
    global amax
    if x >amax:
        amax = x
        
def generate_fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        if a not in tree:
            tree[a] = {} #fib as no prime yet
        a, b = b, a + b
        #index[b] = [a,"+",b] #add to index
        ismax(b)

generate_fibonacci(limit)
## now the sieve
fibs = list(reversed(sorted(list(tree.keys()))))
#print(fibs)

number_list = range(2,limit)
for a in number_list:
    for b in number_list:
        v = a *b        
        if v not in index:
            index[v] = [a,"*",b]
            ismax(v)


# now find the primes in a sieve, and look down to find the fib
primes = {
}

def find_fibs(v):
    for x in fibs: #loop
        if x < v: #the first fib under the v        
            if v not in index: #not compound
                tree[x][v] = [] #prime under a fib
                primes[v]=x #parent
                print("Prime",x,v)
                return x
            else: #compounds lets add them
                if x in primes:
                    if x in primes:
                        fib = primes[x]
                        #print(x,tree[fib])
                        tree[fib][x].append(x)
                        return x
                    else:
                        print("DEBUG3",x,tree[fib])
                else:# are fibs
                    #print("DEBUG1",x)
                    #print(tree[fib])
                    pass

#for v in number_list:
def scan(x):
    y = x-1  #find the next prime
    if x < limit:
    while y > 1:
        if y in primes:
            #pass
            print("DEUB",y)
        else:
            y = y - 1 # start looking one down               

            if y in primes :
                fib = primes[y]
                if y in tree[fib]:
                    part = tree[fib][y]
                    part.append(x)
                    print("DEBUG",
                          primes[y],
                          tree[primes[y]][y],
                          x)
                else:
                    # primes
                    print("DEBUG2",
                          primes[y],
                          tree[primes[y]],
                          x)
                    x = find_fibs(v)
                    primes[v]=x #parent

# Now sweep up the primes and attach them to the fibs
for x in range(amax):
    if x not in index:
        index[x] = [x]        #now scan up to find the first
        if x > 0:
            scan(x)

pprint.pprint({
    "FIB":tree,
    "primes":primes,
    "index": index})

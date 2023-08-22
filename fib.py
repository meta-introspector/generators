import pprint
limit = 20
# this program is optimized to unroll loops and use globals for speed
# there must be a better way to do this. 
# Your hierarchical tree structure (nested dictionaries) goes here
tree = { # fibbonacci | prime | integers
    0: {},
    1: {},
} 
# now find the primes in a sieve, and look down to find the fib
primes = {
    2: 1,
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
        index[b] = [a,"+",b] #add to index
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

# sieve 
def scan(x):
    y = x-1  #find the next prime
    if x < limit:
        while y > 0:
            y = y - 1 # start looking one down
            if y in tree:
                #print("F",y)
                return y
    return -1
                    
# Now sieve/sweep up the primes and attach them to the fibs
for x in range(amax):
    if x not in index:
        if x < limit:
            #print("P",x)
            primes[x]=scan(x)
            index[x] = [x]
        # now scan up to find the first

pprint.pprint({
    #"FIB":tree,
#    "primes":primes,
    "index": index})

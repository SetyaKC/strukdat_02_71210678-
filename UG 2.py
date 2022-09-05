import timeit
#fungsi iteratif
def fibonacci_iteratif(n): 
    a = 1 
    b = 1 
    # print(a,end=" ")
    for i in range(1,n):
        # print(b,end=" ")
        if ((i+1) % 5 == 0):
            print(end="")
        c = b
        b = b+a
        a = c
    
for i in range(1,11):
    start = timeit.default_timer()
    fibonacci_iteratif(i)  
    end = timeit.default_timer()
    print("n=",i,"iteratif ->", end-start,"second")
print()

#fungsi rekursif
def fibonacci_rekursif(n):
    if n <= 1:
        return n
    else:
        return (fibonacci_rekursif(n-1)+fibonacci_rekursif(n-2))

for i in range(1,11):
    start = timeit.default_timer()
    fibonacci_rekursif(i)  
    end = timeit.default_timer()
    print("n=",i,"rekursif ->", end-start,"second")   



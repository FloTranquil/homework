def shell(A):
    t=int(len(A)/2)
    while t>0:
        for i in range (len(A)-t):
            while i>=0 and A[i] > A[i+t]:
                A[i], A[i+t] =  A[i+t], A[i]
                i-=1
        t = int(t/2)
A=[2, 5, 1, 4, 10, 0, 9, 6, 3]
shell(A)
print (A)

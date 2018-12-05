
def solution(A, K):

    N = len(A)

    for j in xrange(K):
        a = []
        for i in xrange(N):
            a.append(A[i])

        for i in xrange(N):
            if i == 0:
                
                A[i] = a[N-1]
                
            elif (i+1) == N:
                
                A[i] = a[i-1]
                
                break
            else:
               
                A[i] = a[i-1]


        print "A = "+str(A)

           

def main():
    A = [-1, 0, 0, 0, 0]
    K = 4
    solution(A, K)
 

if __name__=='__main__':
    main()
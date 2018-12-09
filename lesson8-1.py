def solution(A):
    n = len(A)
    leader = -1
    B = sorted(A)
    candidate = B[n // 2]
    count = 0
    
    for i in range(n):
        if (B[i] == candidate):
            count += 1
        if (count > n // 2):
            leader = candidate
    
    result = 0
    #print leader
    #print A
    for i in range(n):
        #print "i = "+str(i)
        a = A[:i+1]
        b = A[i+1:]

        #print "a.count(leader)="+str(a.count(leader))
        #print "b.count(leader)="+str(b.count(leader))
        if (a.count(leader) > len(a) // 2) and (b.count(leader) > len(b) // 2):
            result += 1

    return result    


def main():
    A = [4, 3, 4, 4, 4, 2]
    print solution(A)



if __name__ == "__main__":
    main()
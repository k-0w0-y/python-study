def prefix_sums(A):

    if A:
        n = len(A)
        P = [0]*(n+1) # [0, 0, ..., 0] 
        for k in range(1, n+1):
            P[k] = P[k-1] + A[k-1]

        return P

    else:
        return 0    

def count_total(P, x, y):
    print ("count_total = "+str(P[y + 1] - P[x]))
    return P[y + 1] - P[x]


def mushrooms(A, k, m):

    n = len(A)
    pref = prefix_sums(A)
    result = 0
    left_pos = 0
    right_pos = 0
    
    for p in range(min(m, k)+1):
        #print ("p = "+str(p))
        left_pos = k - p 
        #print ("left_pos = "+str(left_pos))
        right_pos = min(n - 1, max(k, k + m - 2 * p))
        #print ("right_pos = "+str(right_pos))
        result = max(result, count_total(pref, left_pos, right_pos))
        #print ("result = "+str(result))

    for p in range(min(m + 1, n - k)):
        #print ("p = "+str(p))
        right_pos = k + p
        #print ("right_pos = "+str(right_pos))
        left_pos = max(0, min(k, k - (m - 2 * p)))
        #print ("left_pos = "+str(left_pos))
        result = max(result, count_total(pref, left_pos, right_pos))
        #print ("result = "+str(result))
    return result


def main():
    A = [2, 3, 7, 5, 1, 3, 9]
    k = 4
    m = 6
    print mushrooms(A, k, m)



if __name__ == "__main__":
    main()
def solution(A):

    if A:

        m = max(A)
        B = range(1, m+1)
        print B
        if len(A) != len(B):
            return 0
        else:
            for item in B:
                #print ("item="+str(item))
                if item not in A:
                    return 0
            
            return 1

    else:
        return 0    




def main():
	A = [1, 3, 3]
	print solution(A)


if __name__ == "__main__":
    main()
def solution(A):
    
    flag = 0

    B = []
    for i in A:
    	B.append(i)

    C = []
    for i in A:
        for j in B:

            if i == j:
    		    flag += 1

        if flag >= 2:
    	    C.append(i)
    		#print C
        flag = 0
	
    result = list(set(A)^set(C))
    return result[0]

def main():
	A = [9, 3, 9, 3, 9, 7, 9]
	print solution(A)


if __name__ == "__main__":
    main()

def solution(A):
    count = []
    east_index = []

    for i in range(len(A)):
    
        if A[i] == 0:
            east_index.append(i)

    pairs = [0]*len(east_index)

    c = 0
    for i in range(len(east_index)): 
        a = east_index[i]
        b = A[a:]
        pairs[i] = b

    for i in range(len(east_index)):
        c = pairs[i].count(1)
        if c > 1000000000:
            return -1
        count.append(c)
        
    result = sum(count)

    if result > 1000000000:
        return -1

    return result


def main():
    A = [0, 1, 0, 1, 1]
    print solution(A)



if __name__ == "__main__":
    main()
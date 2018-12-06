def solution(A):

    N = max(A)
    n = min(A)

    l = []
    for i in range(n, N+1):
        l.append(i)


    for i in l:
        if i not in A:
            result = i
            break
    
    print result 


def main():
    A = [2, 3, 1, 5, 4, 8, 6]
    solution(A)


if __name__ == "__main__":
    main()
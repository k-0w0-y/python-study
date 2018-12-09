
def solution(A):

    n = len(A)

    a = int((n + 1 )* (n + 2) / 2)
    b = 0
    
    for i in range(0, n):
        b += A[i]

    return(a - b)

def main():
    A = [1, 3]
    print solution(A)


if __name__ == "__main__":
    main()
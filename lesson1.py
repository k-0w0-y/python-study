# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):

    binary = []

    while True:

        m = N % 2
        
        binary.append(m)
            
        n = (N-m)/2
        if n == 0:
            break

        N = n

    binary_gap = 0
    check_0 = 0
    check_1 = 1

    t = 0

    for i in binary[::-1]:
        # print i
        if i == 0: 
            check_0 = 1
            t += 1 
        else:
            if check_1 == 1 and check_0 == 1:
                if binary_gap <= t:
                    binary_gap = t
                t = 0
                check_1 = 1
                check_0 = 0

            else:
                continue
       
    return binary_gap

def main():
    print solution(328)

if __name__ == "__main__":
    main()
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
    flag = 0
    t = 0
    
    print (binary)
    for i in binary[::-1]:
        if i == 0: 
            t += 1
            flag = 1 
        else:
            if flag == 1:
                if binary_gap <= t:
                    binary_gap = t
                    t = 0
            else:
                pass
                
    return binary_gap

def main():
    print solution(74901729)

if __name__ == "__main__":
    main()
def pop_item(x, y, x_head, y_head):
    x.pop(x_head)
    y.pop(y_head)
    x_head = x_head-1
    y_head = y_head-1
    
    return x, y, x_head, y_head

def valid_head(x_item, y_item):
    if x_item == "(" and y_item == ")": 
        return 1
    elif x_item == "[" and y_item == "]": 
        return 1
    elif x_item == "{" and y_item == "}": 
        return 1
    else:
        return 0

def solution(S):
    
    x = []
 
    for c in S:
        x.append(c)

    if len(x) == 0:
        return 1
    else:
        y = []
        x_head = len(x)-1
        y_head = 0
        while True:

            if len(y) == 0:
                y.append(x[x_head])
                x.pop(x_head)
                x_head = x_head-1

            else:
                if valid_head(x[x_head], y[y_head]) == 1:
                    x, y, x_head, y_head = pop_item(x, y, x_head, y_head)
                else:
                    y_head = y_head+1
                    y.append(x[x_head])
                    x.pop(x_head)
                    x_head = x_head-1

            if len(x) == 0:
                break

        if len(y) == 0:
            result = 1
        else:
            result = 0

        return result


def main():
    S = "([)()]"
    print solution(S)



if __name__ == "__main__":
    main()
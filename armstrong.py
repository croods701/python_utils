def armstrong(num: int) -> bool:
    inp = str(num)
    n = len(inp)  # num of digits

    sum_inp = 0
    for d in inp:
        d = int(d)
        sum_inp += d ** n

    return num == sum_inp

import sys
if len(sys.argv) > 1:
    try:
        inp = int(sys.argv[1])
    except ValueError:
        print("please enetr valid number")
    else:
        print(armstrong(inp))    

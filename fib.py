def fib(num: int) -> int:
    return num * fib(num-1) if num > 0 else 1

import sys
if len(sys.argv) > 1:
    # number argument
    inp: str = sys.argv[1]
    try:
        inp = int(inp)
    except ValueError:
        print("Please pass valid number")
    else:
        result: int = fib(inp)
        print(result)

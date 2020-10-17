def fib(num: int) -> int:
    return num * fib(num-1) if num > 0 else 1

import sys
if len(sys.argv) > 1:
    print(fib(int(sys.argv[1])))

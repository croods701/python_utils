def armstrong(num: int) -> bool:
    inp = str(num)
    n = len(inp)  # num of digits

    sum_inp = 0
    for d in inp:
        d = int(d)
        sum_inp += d ** n

    return num == sum_inp

print(armstrong(133))
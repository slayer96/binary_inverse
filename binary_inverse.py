#binary inverse
#python3.4
def O(n):
    if len(n) == 1 and n[0] == 0:
        return [0]
    #n.reverse()
    dec = 0
    index = 0
    for i in n:
        tmp = i * ((-2) ** index)
        index += 1
        dec += tmp
    #print(dec)
    dec *= -1

    result = []
    while dec:
        tmp = dec % (-2)
        dec //= (-2)
        if tmp < 0:
            tmp += 2
            dec += 1
        result.append(tmp)
    #result.reverse()
    return result

if __name__ == '__main__':
    print(O([1, 0, 1, 1, 0, 1]))
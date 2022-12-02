from inputs import message

if __name__ == "__main__":
    msg = message("Message")


def hammingCall(bits):
    parityCount = 0
    while 1:
        case1 = 2 ** parityCount
        case2 = len(bits) + parityCount + 1
        if (case1 >= case2):
            break
        else:
            parityCount += 1

    parity = nonParity = 0
    array = list(range(0, len(bits) + parityCount))

    # Creating Temporary array
    for k in range(1, len(bits) + parityCount + 1):
        if (k == 2 ** parity):
            array[k - 1] = "0"
            parity += 1
        else:
            array[k - 1] = bits[nonParity]
            nonParity += 1

    # initialize
    for par in range(0, parityCount):
        let = 2 ** par
        count = 0
        s = let - 1
        while (s < len(array)):
            for a in range(s, s + let):
                if (a < len(array)):
                    if (int(array[a]) == 1): count += 1
            s += 2 ** let

        if (count % 2 != 0): array[let - 1] = "1"

    if __name__ == "__main__":
        return f"Hamming code: {' '.join(array[::-1])}"
    else:
        return ''.join(array[::-1])


if __name__ == "__main__":
    print(hammingCall(msg[::-1]))

from hammingCode import hammingCall
import pandas as p

bits = [bin(a)[2:].rjust(4, "0") for a in range(0, 16)]
number = list(range(0, 16))
hamming = []
ham_num = []

for a in bits:
    temp = hammingCall(str(a).ljust(4, "0")[::-1])
    hamming.append(str(temp))
    ham_num.append(str(int(temp, 2)))

df = p.DataFrame({"Number": number, "Binary Value": bits, "Hamming Code": hamming, "Decimal Value": ham_num})

df.to_csv("HammingCode.csv", index=False)

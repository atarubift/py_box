blocks = ""

while blocks != "0" :
    blocks = input("必要ブロック数：")
    num = int(blocks)
    print('%s Stack + %s'% (num // 64, num % 64))


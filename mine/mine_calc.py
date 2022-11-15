blocks = ""

while blocks != "0" :
    blocks = input("必要ブロック数：")
    num = int(blocks)
    stacks = num // 64
    alpha = num % 64
    if stacks >= 27:
        shulker = stacks // 27
        stacks %= 27
        print('%s Shulker + %s Stack + %s'% (shulker, stacks, alpha))
    else:
        print('%s Stack + %s'% (stacks, alpha))


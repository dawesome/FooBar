def ternary(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

def balancedTernaryFromTernary(tern):
    tern = tern[::-1]
    balanced = []
    carry = 0

    for n in tern:
        intVal = int(n) + carry
        if intVal == 0:
            balanced.append('-')
            carry = 0
        elif intVal == 1:
            balanced.append('L')
            carry = 0
        elif intVal == 2:
            balanced.append('R')
            carry = 1
        elif intVal == 3:
            balanced.append('-')
            carry = 1

    if carry == 1:
        balanced.append('L')
    return ''.join(balanced)[::-1]

def answer(x):
    return list(balancedTernaryFromTernary(ternary(x)))


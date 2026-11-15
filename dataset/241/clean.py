def apply_table(inp, table):
    res = ''
    for i in table:
        res += inp[i - 1]
    return res

def left_shift(data):
    return data[1:] + data[0]

def xor(a, b):
    res = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            res += '0'
        else:
            res += '1'
    return res

def apply_sbox(s, data):
    row = int('0b' + data[0] + data[-1], 2)
    col = int('0b' + data[1:3], 2)
    return bin(s[row][col])[2:]

def function(expansion, s0, s1, key, message):
    left = message[:4]
    right = message[4:]
    temp = apply_table(right, expansion)
    temp = xor(temp, key)
    left_bin_str = apply_sbox(s0, temp[:4])
    right_bin_str = apply_sbox(s1, temp[4:])
    left_bin_str = '0' * (2 - len(left_bin_str)) + left_bin_str
    right_bin_str = '0' * (2 - len(right_bin_str)) + right_bin_str
    temp = apply_table(left_bin_str + right_bin_str, p4_table)
    temp = xor(left, temp)
    return temp + right
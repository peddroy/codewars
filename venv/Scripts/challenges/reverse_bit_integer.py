print(f'Reverse bit integer!')

def reverse_bits(n):
    if n < 0:
        pass
    else:
        convert_to_bin = (bin(n)[2::])[::-1]
        n = int(convert_to_bin, 2)
    return n

print(reverse_bits(417))



from timeit import timeit

def get_set_bits_count_using_brian_kernighans_algorithm(number: int) -> int:
    """Count the number of set bits in a 32 bit integer"""
    if number < 0:
        raise ValueError('the value of input must not be negative')
    result = 0
    while number:
        number &= number - 1
        result += 1
    return result

def get_set_bits_count_using_modulo_operator(number: int) -> int:
    """Count the number of set bits in a 32 bit integer"""
    if number < 0:
        raise ValueError('the value of input must not be negative')
    result = 0
    while number:
        if number % 2 == 1:
            result += 1
        number >>= 1
    return result

def get_set_bits_count_using_lookup_table(number: int) -> int:
    """Count the number of set bits in a 32-bit integer using a precomputed lookup table.

    I see similar approach in GeeksforGeeks, but the implementation is different.
    Link to Code:
    https://www.geeksforgeeks.org/dsa/count-set-bits-integer-using-lookup-table/"""
    _lookup_table = [bin(i).count('1') for i in range(256)]
    if number < 0:
        raise ValueError('the value of input must not be negative')
    return _lookup_table[number & 255] + _lookup_table[number >> 8 & 255] + _lookup_table[number >> 16 & 255] + _lookup_table[number >> 24 & 255]

def benchmark() -> None:
    """
    Benchmark code for comparing 3 functions, with different length int values.
    Brian Kernighan's algorithm is consistently faster than using modulo_operator,
    and the lookup table method is often the fastest for repeated calls.
    """

    def do_benchmark(number: int) -> None:
        setup = 'import __main__ as z'
        print(f'Benchmark when number = {number!r}:')
        print(f'get_set_bits_count_using_modulo_operator(number) = {get_set_bits_count_using_modulo_operator(number)!r}')
        timing = timeit(f'z.get_set_bits_count_using_modulo_operator({number})', setup=setup)
        print(f'timeit() runs in {timing} seconds')
        print(f'get_set_bits_count_using_brian_kernighans_algorithm(number) = {get_set_bits_count_using_brian_kernighans_algorithm(number)!r}')
        timing = timeit(f'z.get_set_bits_count_using_brian_kernighans_algorithm({number})', setup=setup)
        print(f'timeit() runs in {timing} seconds')
        print(f'get_set_bits_count_using_lookup_table(number) = {get_set_bits_count_using_lookup_table(number)!r}')
        timing = timeit(f'z.get_set_bits_count_using_lookup_table({number})', setup=setup)
        print(f'timeit() runs in {timing} seconds')
    for number in (25, 37, 58, 0):
        do_benchmark(number)
        print()
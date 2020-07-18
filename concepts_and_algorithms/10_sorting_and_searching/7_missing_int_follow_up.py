missing_int = __import__("7_missing_int")
# from missing_int import makeBitArray

def find_open_number(filename: str):
    range_size = (1 << 20)   # 2 ** 20 bits
    
    blocks = get_count_per_block(filename, range_size)
    block_index = find_block_with_missing(blocks, range_size)
    if block_index < 0: return -1

    bit_vector = get_bit_vector_for_range(filename, block_index, range_size)

    for i in range(range_size):
        offset = missing_int.testBit(bit_vector, i)
        if not offset:
            offset = i
            break

    return block_index * range_size + offset

def get_count_per_block(filename: str, range_size: int):
    array_size = 2 ** 31 // range_size + 1
    blocks = [0] * array_size

    with open("missing_int.txt") as f:
        for value in f:
            blocks[int(value) // range_size] += 1
    
    return blocks

def find_block_with_missing(blocks: list, range_size: int):
    for i, block_range in enumerate(blocks):
        if block_range < range_size:
            return i
    return -1

def get_bit_vector_for_range(filename: str, block_index: int, range_size: int):
    start_range = block_index * range_size
    end_range = start_range + range_size
    bit_vector = missing_int.makeBitArray(range_size)

    with open("missing_int.txt") as f:
        for value in f:
            value = int(value)
            if start_range <= value < end_range:
                missing_int.setBit(bit_vector, value - start_range)
    return bit_vector


print(find_open_number("missing_int.txt"))

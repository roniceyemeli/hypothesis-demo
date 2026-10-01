from functools import reduce

def to_ascii_codes(input:str) -> list[int]:
    return [ord(char) for char in input]


def from_ascii_codes(input:list[int]) -> str:
    return reduce(lambda x, y: x + chr(y), input, "")
from __future__ import annotations


class BinaryNumber:
    def __init__(self, value: str):
        if not all(val in ("0", "1") for val in value):
            raise ValueError('value must contains 0 or 1 digits')
        self.value = value

    def __normalized_values(self, other: BinaryNumber) -> (str, str):
        max_length = max(len(other.value), len(self.value))
        v1 = self.value.zfill(max_length)
        v2 = other.value.zfill(max_length)
        return v1, v2

    def __and__(self, other: BinaryNumber) -> BinaryNumber:
        # Perform bitwise AND
        return BinaryNumber(
            "".join("1" if v1 == "1" and v2 == "1" else "0" for v1, v2 in zip(*self.__normalized_values(other))))

    def __or__(self, other: BinaryNumber) -> BinaryNumber:
        # Perform bitwise OR
        return BinaryNumber(
            "".join("1" if v1 == "1" or v2 == "1" else "0" for v1, v2 in zip(*self.__normalized_values(other))))

    def __xor__(self, other: BinaryNumber) -> BinaryNumber:
        # Perform bitwise XOR
        return BinaryNumber("".join("1" if v1 != v2 else "0" for v1, v2 in zip(*self.__normalized_values(other))))

    def __invert__(self) -> BinaryNumber:
        # Perform bitwise NOT
        return BinaryNumber("".join("1" if v == "0" else "0" for v in self.value))

    def __repr__(self):
        # String representation
        return f"BinaryNumber({self.value})"


a = BinaryNumber("11011000")
b = BinaryNumber("1100")

print("a:", a)
print("b:", b)

print("a AND b:", a & b)  # a AND b: BinaryNumber(00101011)
print("a OR b:", a | b)  # a OR b: BinaryNumber(11111111)
print("a XOR b:", a ^ b)  # a XOR b: BinaryNumber(11010100)
print("NOT a:", ~a)  # NOT a: BinaryNumber(00100111)

try:
    c = BinaryNumber("312")  # Error: value must contains 0 or 1 digits
    print("c:", c)
except ValueError as e:
    print("Error:", e)

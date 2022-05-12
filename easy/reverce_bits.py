class Solution:
    def reverseBits(self, n: int) -> int:
        all_ones = 0b11111111111111111111111111111111
        return all_ones - n


if __name__ == '__main__':
    all_ones = 0b11111111111111111111111111111111
    print(bin(all_ones - 0b00011111101111111111111011111110))
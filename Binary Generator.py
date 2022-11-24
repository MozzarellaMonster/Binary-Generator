# Binary generator
# Creates 32-bit binary input strings for my Binary Reader program
import random

class binary_generator:
    def __init__(self, amount=45):
        self.amount = amount

    # Coin = 0 for arithmetic operations, coin = 1 for load and store operations
    def gen_codes(self, spaces=False):
        for i in range(self.amount):
            coin=random.randint(0, 1)
            if spaces:
                print(self.gen_opcode(coin) + " " + self.gen_nums_and_dest() + " " + self.gen_nums_and_dest() + " " + self.gen_nums_and_dest() + " " + "00000" + " " + self.gen_func(coin))
            else:
                print("bin_reader.read(\"" + self.gen_opcode(coin) + self.gen_nums_and_dest() + self.gen_nums_and_dest() + self.gen_nums_and_dest() + "00000" + self.gen_func(coin) + "\")")

    def gen_opcode(self, coin):
        # Arithmetic operations
        if coin == 0:
            opcode = "000000"
        # Load and store operations
        else:
            opcode = "000011"
        return opcode

    def gen_func(self, coin):
        # Arithmetic operations
        if coin == 0:
            func = f'{random.randint(1, 4):06b}'
        # Load and store operations
        else:
            func = f'{random.randint(5, 6):06b}'
        return func

    def gen_nums_and_dest(self):
        return f'{random.randint(0, 31):05b}'

gen = binary_generator(75)
gen.gen_codes()
import re
from z3 import *


class ClassicVM:
    def __init__(self, a, b, c, inst):
        self.a, self.b, self.c, self.inst = a, b, c, inst
        self.ip = 0

    def combo(self, label): return {4: self.a, 5: self.b, 6: self.c}.get(label, label)
    def adv(self, operand): self.a = self.a >> self.combo(operand)
    def bxl(self, operand): self.b = self.b ^ operand
    def bst(self, operand): self.b = self.combo(operand) & 0x07
    def bxc(self, operand): self.b = self.b ^ self.c
    def bdv(self, operand): self.b = self.a >> self.combo(operand)
    def cdv(self, operand): self.c = self.a >> self.combo(operand)
    def jnz(self, operand): self.ip = operand - 2 if self.a else self.ip
    def out(self, operand): print(self.combo(operand) & 0x07, end=',')

    def run(self):
        while self.ip < len(self.inst):
            opcode, operand = self.inst[self.ip], self.inst[self.ip + 1]
            {
                0: self.adv, 1: self.bxl, 2: self.bst, 3: self.jnz,
                4: self.bxc, 5: self.out, 6: self.bdv, 7: self.cdv
            }[opcode](operand)
            self.ip += 2

class SymbolicVM(ClassicVM):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.osolver = Optimize()
        self.a = BitVec('a', 128)
        self.constraints_cnt = 0

    def jnz(self, operand):
        if self.constraints_cnt == len(self.inst):
            self.osolver.add(self.a == 0)
            raise StopIteration
        self.ip = operand - 2

    def out(self, operand):
        if self.constraints_cnt < len(self.inst):
            self.osolver.add(self.combo(operand) & 0x07 == self.inst[self.constraints_cnt])
            self.constraints_cnt += 1

    def run(self):
        start_a = self.a
        try:
            super().run()
        except StopIteration:
            self.osolver.minimize(start_a)
            if self.osolver.check() == sat:
                print(self.osolver.model()[start_a])


def task1(cnt):
    a, b, c, *inst = map(int, re.findall(r'-?\d+', cnt))
    vm = ClassicVM(a,b,c, inst)
    vm.run()


def task2(cnt):
    a, b, c, *inst = map(int, re.findall(r'-?\d+', cnt))
    vm = SymbolicVM(a,b,c, inst)
    vm.run()

cnt = '''Register A: 44348299
Register B: 0
Register C: 0

Program: 2,4,1,5,7,5,1,6,0,3,4,2,5,5,3,0'''
task2(cnt)
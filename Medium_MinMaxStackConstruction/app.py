# Feel free to add new properties and methods to the class.
class MinMaxStack:
    stack = []
    stackMin = []
    stackMax = []

    def peek(self):
        # Write your code here.
        value = self.stack[-1]
        print(f"peek::{value}, stack::{self.stack}, min::{self.stackMin[-1]}, max::{self.stackMax[-1]}")
        return value

    def pop(self):
        # Write your code here.
        self.editMinMax(False)
        value = self.stack.pop(-1)
        print(f"pop::{value}, stack::{self.stack}, min::{self.stackMin[-1]}, max::{self.stackMax[-1]}")
        return value

    def push(self, number):
        # Write your code here.
        if self.stack == []:
            self.stack = [number]
        else:
            self.stack.append(number)
        self.editMinMax(True)
        print(f"push::{number}, stack::{self.stack}, min::{self.stackMin[-1]}, max::{self.stackMax[-1]}")

    def getMin(self):
        # Write your code here.
        print(f"stack::{self.stack}, min::{self.stackMin[-1]}, max::{self.stackMax[-1]}")
        return self.stackMin[-1]

    def getMax(self):
        # Write your code here.
        print(f"stack::{self.stack}, min::{self.stackMin[-1]}, max::{self.stackMax[-1]}")
        return self.stackMax[-1]

    def editMinMax(self, isPushed):
        if isPushed:
            if len(self.stack) == 1:
                self.stackMin = [self.stack[-1]]
                self.stackMax = [self.stack[-1]]
            else:
                if self.stack[-1] <= self.stackMin[-1]:
                    self.stackMin.append(self.stack[-1])
                if self.stack[-1] >= self.stackMax[-1]:
                    self.stackMax.append(self.stack[-1])
        else:
            if self.stack[-1] == self.stackMin[-1]:
                self.stackMin.pop(-1)
            if self.stack[-1] == self.stackMax[-1]:
                self.stackMax.pop(-1)

a = MinMaxStack()
a.push(5)
a.getMin()
a.getMax()
a.peek()
a.push(7)
a.getMin()
a.getMax()
a.peek()
a.push(2)
a.getMin()
a.getMax()
a.peek()
a.pop()
a.pop()
a.getMin()
a.getMax()
a.peek()

"""
Input/Output:
# all methods in constant time and space
MinMaxStack(): -
push(5): -
getMin(): 5
getMax(): 5
peek(): 5
push(7): -
getMin(): 5
getMax(): 7
peek(): 7
push(2): -
getMin(): 2
getMax(): 7
peek(): 2
pop(): 2
pop(): 7
getMin(): 5
getMax(): 5
peek(): 5
"""
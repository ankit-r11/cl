class Number():
    even=0
    def check(self,num):
        if num%2==0:
            self.even=1
    def Even_Odd(self,num):
        self.check(num)
        if self.even==1:
            print(num," is even")
        else:
            print(num," is odd")

n=Number()
n.Even_Odd(21)
print(Number.even)

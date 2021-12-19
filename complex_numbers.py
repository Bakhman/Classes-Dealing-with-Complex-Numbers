class Complex(object):
    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary
        
    def __add__(self, no):
        return Complex(self.r+no.r,self.i+no.i)
        
    def __sub__(self, no):
        return Complex(self.r-no.r,self.i-no.i)
        
    def __mul__(self, no):
        return Complex(self.r*no.r - self.i*no.i, self.r*no.i + self.i*no.r)
    
    def __truediv__(self, no):
        d = no.r**2 + no.i**2
        return Complex((self.r*no.r + self.i*no.i)/d,(self.i*no.r - self.r*no.i)/d)
        
    def mod(self):
        return Complex((self.r**2+self.i**2)**.5,0)

    def __str__(self):
        return "{:.2f}{:+.2f}i".format(self.r,self.i)

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')

class Triangle:
    def __init__(self, a, b, c):
        if self.check_triangle(a, b, c):
            self.a = a
            self.b = b
            self.c = c
        else:
            print("Error input triangle not exist")

    def check_triangle(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            return False
        else:
            return True

    def perimetr(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimetr() / 2
        #print(p)
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** (1 / 2)



if __name__=='__main__':
    p1 = Triangle(4, 4, 5)
    print(f'Периметр треугольника {p1.perimetr()}')
    print(f'Площадь треугольника {p1.area()}')

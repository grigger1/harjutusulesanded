class Ruutvorrand:

    kass = "Nice."
    koer = "|||nice."




    

    def solve_x1(self):
        self.d = self.b ** 2 - 4 * self.a * self.c
        if self.d >= 0:
            self.d = self.d ** 0.5
            return -self.b - self.d / 2 * self.a

    def solve_x2(self):
        self.d = self.b ** 2 - 4 * self.a * self.c
        if self.d >= 0:
            self.d = self.d ** 0.5
            return -self.b - self.d / 2 * self.a
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        self.x1 = self.solve_x1()
        self.x2 = self.solve_x2()


if __name__ == "__main__":
    r1 = Ruutvorrand(1, 2, 3) 
    r2 = Ruutvorrand(12, 0, 12)

    print(r1.kass)
    print(r2.koer)
    print(r1.x1, r1.x2)
    print(r2.x1, r2.x2)

class FiguraGeometrica:
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass


class Triangulo(FiguraGeometrica):
    def __init__(self, base, lado1, lado2, altura):
        self.base = base
        self.lado1 = lado1
        self.lado2 = lado2
        self.altura = altura

    def calcular_area(self):
        return float((self.base*self.altura)/2)

    def calcular_perimetro(self):
        return float(self.base+self.lado1+self.lado2)


class Pentagono(FiguraGeometrica):
    def __init__(self, lado, apotema):
        self.lado = lado
        self.apotema = apotema

    def calcular_area(self):
        return float((self.lado * 5 * self.apotema) / 2)

    def calcular_perimetro(self):
        return float(self.lado * 5)


class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return float(self.base*self.altura)

    def calcular_perimetro(self):
        return float(self.base * 2+self.altura*2)


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

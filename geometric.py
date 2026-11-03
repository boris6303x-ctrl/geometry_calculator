import math
import turtle

CENTIMETER = 37.795

class Shape:
    def __init__(self, name, l, w):
        self.name = name
        self.l = l
        self.w = w

    def area(self):
        if self.validation():
            raise ValueError("input(s) must be greater than 0")
        else:
            return 0

    def validation(self):
        if self.l <= 0 or self.w <= 0:
            return True

    def perimeter(self):
        if self.validation():
            raise ValueError("input(s) must be greater than 0")
        else:
            return 0

    def info(self):
        print(f"Name: {self.name}\nLength: {self.l}\nWidth: {self.w}")

    def draw(self):
        if self.validation():
            turtle.color("red")
            turtle.write("Draw error: could not draw shape because parameter(s) must be not less than 0", align="center")
            turtle.color("black")
            return
        index = 0
        for _ in range(2):
            turtle.write(self.name[index])
            index += 1
            turtle.forward(self.l*CENTIMETER)
            turtle.write(self.name[index])
            index += 1
            turtle.right(90)
            turtle.forward(self.w*CENTIMETER)
            turtle.right(90)

class Rectangle(Shape):
    def __init__(self, l, w, name="Rectangle"):
        super().__init__(name, l, w)
    
    def area(self):
        if self.validation():
            raise ValueError("input(s) must be greater than 0")
        else:
            return self.l*self.w

    def perimeter(self):
        if self.validation():
            raise ValueError("input(s) must be greater than 0")
        else:
            return (self.l+self.w)*2

class Circle(Shape):
    def __init__(self, r, name="Circle"):
        self.name = name
        self.r = r

    def area(self):
        if self.validation():
            raise ValueError("radius must be greater than 0")
        return f"~{(math.pi*(self.r**2)):.2f}"

    def validation(self):
        if self.r <= 0:
            return True

    def perimeter(self):
        raise NameError("circles have no perimeter. Did you mean circumference()?")

    def circumference(self):
        if self.validation():
            raise ValueError("radius must be greater than 0")
        return f"~{(2*math.pi*self.r):.2f}"

    def info(self):
            print(f"Name: {self.name}\nRadius: {self.r}")

    def draw(self):
        if self.validation():
            turtle.color("red")
            turtle.write("Draw error: could not draw shape because parameter(s) must be not less than 0", align="center")
            turtle.color("black")
            return
        turtle.dot(5)
        turtle.write(f"O_{self.name}")
        turtle.penup()
        turtle.forward(self.r*CENTIMETER)
        turtle.pendown()
        turtle.write(self.name)
        turtle.left(90)
        turtle.circle(self.r*CENTIMETER)

class Square(Rectangle):
    def __init__(self, s, name="Square"):
        super().__init__(s, s, name)

# P = b + 2 × √(h² + (b/2)²)
class Triangle(Shape):
    def __init__(self, b, h=None, s1=None, s2=None, name="Triangle"):
        self.b = b
        self.h = h
        self.s1 = s1
        self.s2 = s2
        self.name = name

    def area(self):
        if self.validation():
            raise ValueError("input must be greater than 0")
        else:
            return 0.5*self.b*self.h

    def validation(self):
        if self.b <= 0 or self.h <= 0:
            return True

    def perimeter(self):
        if self.validation():
            raise ValueError("input(s) must be greater than 0")
        return self.b+self.s1+self.s2

    def root_perimeter(self):
        if self.validation():
            raise ValueError("input must be greater than 0")
        elif self.s1 != math.sqrt(self.h**2 + (self.b/2)**2):
            raise ValueError("triangle side is not equal to sqrt(h**2 + (b/2)**2)")
        return f"{self.b + 2 * math.sqrt(self.h**2 + (self.b/2)**2):.0f}"

    def info(self):
        print(f"Name: {self.name}\nBase: {self.b}\nHeight: {self.h}\nSide 1: {self.s1}\nSide 2: {self.s2}")

    def draw(self):
        turtle.color("red")
        turtle.write("Draw error: planar triangle is unknown because triangle type is not given", align="center")
        turtle.color("black")

class IsoscelesTriangle(Triangle):
    def __init__(self, b, h=None, s=None, name="Isosceles triangle"):
        super().__init__(b, h, s, s, name)

    def draw(self):
        if self.validation():
            turtle.color("red")
            turtle.write("Draw error: could not draw shape because parameter(s) must be not less than 0", align="center")
            turtle.color("black")
        elif self.s1 != math.sqrt(self.h**2 + (self.b/2)**2):
            turtle.color("red")
            turtle.write("Draw error: triangle side is not equal to sqrt(h**2 + (b/2)**2)", align="center")
            turtle.color("black")
        alpha = math.degrees(math.atan(2 * self.h / self.b))

        turtle.write(self.name[0])
        turtle.forward(self.b*CENTIMETER)
        turtle.write(self.name[2])
        turtle.left(alpha*2)
        turtle.forward(math.sqrt(self.h**2 + (self.b/2)**2)*CENTIMETER*2)
        turtle.write(self.name[1])
        turtle.home()

class RightTriangle(Triangle):
    def __init__(self, b, h=None, s=None, name="Right Triangle"):
        self.s = s
        super().__init__(b, h, h, s, name)
    
    def area(self):
        if self.validation():
            raise ValueError("input must be greater than 0")
        return f"{self.b*self.h/2:.0f}"
    

    def perimeter(self):
        if self.s != math.hypot(self.b, self.h):
            raise ValueError("side must be hypotenuse")
        return self.b+self.h+self.s

    def pyth_perimeter(self):
        if self.validation():
            raise ValueError("input must be greater than 0")
        perimeter = self.b + self.h + math.hypot(self.b, self.h)
        if perimeter == int(perimeter):
            return int(perimeter)
        return perimeter

    def validation(self):
        if self.b <= 0 or self.h <= 0:
            return True

    def info(self):
            print(f"Name: {self.name}\nOpposite: {self.b}\nAdjacent: {self.h}\nHypotenuse: {math.hypot(self.b, self.h)}")

    def heron_area(self):
        # p is the semiperimeter - the perimeter divided by 2
        if self.validation():
            raise ValueError("input must be greater than 0")
        p = self.pyth_perimeter()/2
        return f"{math.sqrt(p * (p-self.b) * (p-self.h) * (p-math.hypot(self.b, self.h))):.0f}"

    def draw(self):
        if self.validation():
            turtle.color("red")
            turtle.write("Draw error: could not draw shape because parameter(s) must be not less than 0", align="center")
            turtle.color("black")
            return
        if self.s != math.hypot(self.b, self.h):
            turtle.color("red")
            turtle.write("Draw error: could not draw shape because the sidelength must be hypotenuse", align="center")
            turtle.color("black")

        turtle.write(self.name[0])
        turtle.forward(self.b*CENTIMETER)
        turtle.write(self.name[1])
        turtle.left(90)
        turtle.forward(self.h*CENTIMETER)
        turtle.write(self.name[2])
        turtle.home()

class Rhombus(Shape):
    def __init__(self, s, h=None, name="Rhombus"):
        self.s = s
        self.h = h
        self.name = name

    def area(self):
        if self.validation():
            raise ValueError("inputs must be greater than 0")
        else:
            return self.s*self.h

    def validation(self):
        if self.s <= 0 or self.h <= 0:
            return True

    def perimeter(self):
        if self.validation():
            raise ValueError("input must be greater than 0")
        return self.s*4

    def info(self):
        print(f"Name: {self.name}\nHeight: {self.h}\nSide: {self.s}")

    def draw(self):
        if self.validation():
            turtle.color("red")
            turtle.write("Draw error: could not draw shape because parameter(s) must be not less than 0", align="center")
            turtle.color("black")
            return
        if self.h > self.s:
            turtle.color("red")
            turtle.write("Draw error: height must not be greater than the sidelength", align="center")
            turtle.color("black")
            return
        alpha = math.asin(self.h / self.s)
        dx = self.s * math.cos(alpha) * CENTIMETER

        sx, sy = -self.s*CENTIMETER/2, -self.h*CENTIMETER/2

        # sx - Start X, sy - Start Y
        points = [(sx, sy),
                (sx + self.s * CENTIMETER, sy),
                (sx + self.s * CENTIMETER + dx, sy + self.h * CENTIMETER),
                (sx + dx, sy + self.h * CENTIMETER)]

        turtle.penup()
        turtle.goto(points[0])
        turtle.pendown()

        for i in range(4):
            turtle.goto(points[i])
            turtle.write(self.name[i])
        turtle.goto(points[0])

class RegularHexagon(Shape):
    # a is the apothem - the distance between the center and the midpoint of the side
    def __init__(self, s, a=None, name="Hexagon"):
        self.s = s
        self.a = a
        self.name = name

    def area(self):
        if self.validation():
            raise ValueError("input must be greater than 0")
        elif self.a != (self.s * math.sqrt(3)) / 2:
            raise ValueError("hexagon apothem is not equal to (s * sqrt(3)) / 2")
        else:
            return f"~{(3*self.s*self.a):.2f}"

    def validation(self):
        if self.s <= 0 or self.a <= 0:
            return True

    def perimeter(self):
        if self.validation():
            raise ValueError("input(s) must be greater than 0")
        else:
            return self.s*6

    def info(self):
            print(f"Name: {self.name}\nSide: {self.s}\nApothem: {self.a}")

    def draw(self):
        if self.validation():
            turtle.color("red")
            turtle.write("Draw error: could not draw shape because parameter(s) must be not less than 0", align="center")
            turtle.color("black")
            return
        elif self.a != (self.s * math.sqrt(3)) / 2:
            turtle.color("red")
            turtle.write("Draw error: hexagon apothem must be equal to the sidelength times the square root of 3", align="center")
            turtle.color("black")
            return
        for i in range(6):
            turtle.write(self.name[i])
            turtle.forward(self.s*CENTIMETER)
            turtle.left(60)

def main():
    # rc = Rectangle(5, 3, "ABCD")
    # c = Circle(6, "c")
    # s = Square(5, "EFGH")
    # it = IsoscelesTriangle(6, 4, 5, "IJK")
    # rt = RightTriangle(3, 4, 5, "LMN")
    # rh = Rhombus(7, 6, "OPQR")
    h = RegularHexagon(3, (3*math.sqrt(3))/2, "RSTUVW")

    try:
    #     print("Shape information:")
    #     rc.info()
    #     c.info()
    #     s.info()
    #     it.info()
    #     rt.info()
    #     rh.info()
    #     h.info()
    #     print("-" * 20)
    #     print("Areas:")
    #     print(rc.area())
    #     print(c.area())
    #     print(s.area())
    #     print(it.area())
    #     print(rt.area())
    #     print(rt.heron_area())
    #     print(rh.area())
    #     print(h.area())
    #     print("-" * 20)
    #     print("Perimeters:")
    #     print(rc.perimeter())
    #     print(c.circumference())
    #     print(s.perimeter())
    #     print(it.perimeter())
    #     print(it.root_perimeter())
    #     print(rt.pyth_perimeter())
    #     print(rt.perimeter())
    #     print(rh.perimeter())
    #     print(h.perimeter())
        h.draw()
    except Exception as e:
        print(f"An error occured: {type(e).__name__}: {e}")
    
    turtle.done()

if __name__ == "__main__":
    main()
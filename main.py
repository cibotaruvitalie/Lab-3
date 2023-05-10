# Adapter pattern
class ShapeToDrawableAdapter:
    def __init__(self, shape):
        self.shape = shape

    def draw(self, canvas):
        self.shape.draw(canvas)

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, canvas):
        canvas.draw_circle(self.x, self.y, self.radius)

class Square:
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def draw(self, canvas):
        canvas.draw_square(self.x, self.y, self.side)

class Canvas:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def draw_all(self):
        for shape in self.shapes:
            shape.draw(self)

class DrawingAPI:
    def draw_circle(self, x, y, radius):
        pass

    def draw_square(self, x, y, side):
        pass

class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f'Drawing circle with API1 at ({x}, {y}) with radius {radius}')

    def draw_square(self, x, y, side):
        print(f'Drawing square with API1 at ({x}, {y}) with side {side}')

class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f'Drawing circle with API2 at ({x}, {y}) with radius {radius}')

    def draw_square(self, x, y, side):
        print(f'Drawing square with API2 at ({x}, {y}) with side {side}')

# Bridge pattern
class DrawableShape:
    def __init__(self, drawing_api):
        self.drawing_api = drawing_api

    def draw(self, canvas):
        pass

class DrawableCircle(DrawableShape):
    def __init__(self, x, y, radius, drawing_api):
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, canvas):
        self.drawing_api.draw_circle(self.x, self.y, self.radius)

class DrawableSquare(DrawableShape):
    def __init__(self, x, y, side, drawing_api):
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.side = side

    def draw(self, canvas):
        self.drawing_api.draw_square(self.x, self.y, self.side)

# Composite pattern
class CompositeShape:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def remove_shape(self, shape):
        self.shapes.remove(shape)

    def draw(self, canvas):
        for shape in self.shapes:
            shape.draw(canvas)

# Decorator pattern
class DrawableShapeDecorator(DrawableShape):
    def __init__(self, drawable_shape):
        self.drawable_shape = drawable_shape

    def draw(self, canvas):
        self.drawable_shape.draw(canvas)

class FilledShapeDecorator(DrawableShapeDecorator):
    def __init__(self, drawable_shape, color):
        super().__init__(drawable_shape)
        self.color = color

    def draw(self, canvas):
        self.drawable_shape.draw(canvas)
        print(f'Filling shape with color {self.color}')


# Create the drawing API objects
api1 = DrawingAPI1()
api2 = DrawingAPI2()

# Create the shapes using the Bridge pattern
circle1 = DrawableCircle(10, 10, 5, api1)
circle2 = DrawableCircle(20, 20, 10, api2)
square1 = DrawableSquare(30, 30, 15, api1)

# Add the shapes to a CompositeShape using the Composite pattern
composite = CompositeShape()
composite.add_shape(circle1)
composite.add_shape(circle2)
composite.add_shape(square1)

# Decorate the shapes with a color using the Decorator pattern
filled_circle = FilledShapeDecorator(circle1, 'red')
filled_square = FilledShapeDecorator(square1, 'blue')

# Create a Canvas object and add the shapes to it
canvas = Canvas()
canvas.add_shape(ShapeToDrawableAdapter(filled_circle))
canvas.add_shape(ShapeToDrawableAdapter(filled_square))
canvas.add_shape(ShapeToDrawableAdapter(composite))

# Draw all the shapes on the canvas
canvas.draw_all()
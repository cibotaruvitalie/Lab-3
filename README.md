# **Design Patterns in Python**

This project demonstrates the use of four design patterns in Python: Adapter, Bridge, Composite, and Decorator.

**Adapter Pattern**

The Adapter pattern allows two incompatible interfaces to work together. In this project, we have two classes: Shape and DrawableShape. The Shape class has a draw() method that takes a Canvas object as an argument, while the DrawableShape class has a draw() method that takes a DrawingAPI object as an argument. To make the Shape class compatible with the DrawableShape class, we create an Adapter class, ShapeToDrawableAdapter, which adapts the Shape class to the DrawableShape class.

**Bridge Pattern**

The Bridge pattern decouples an abstraction from its implementation, allowing them to vary independently. In this project, we have an abstraction, DrawableShape, and two implementations, DrawableCircle and DrawableSquare, which are subclasses of DrawableShape. We also have an implementation of the DrawingAPI interface, DrawingAPI1 and DrawingAPI2. The DrawableShape class has a draw() method that takes a DrawingAPI object as an argument, and the DrawableCircle and DrawableSquare classes pass their specific shape parameters to the DrawingAPI object's implementation of the draw\_circle() or draw\_square() method, respectively.

**Composite Pattern**

The Composite pattern allows us to treat a collection of objects in the same way as an individual object. In this project, we have a CompositeShape class, which can contain multiple DrawableShape objects. The CompositeShape class has a draw() method that calls the draw() method of each of its DrawableShape objects.

**Decorator Pattern**

The Decorator pattern allows us to add functionality to an object at runtime without affecting its behavior at compile time. In this project, we have a DrawableShapeDecorator class, which is a subclass of DrawableShape. The FilledShapeDecorator class is a subclass of DrawableShapeDecorator and adds the ability to fill a shape with a specified color.

**Running the Code**

To run the code, simply execute the main.py file in the terminal:

python main.py

The output should show the shapes being drawn with their respective drawing APIs and colors.

**Conclusion**

This project demonstrates the use of four powerful design patterns in Python. The Adapter pattern allows us to adapt incompatible interfaces, the Bridge pattern allows us to decouple abstractions from implementations, the Composite pattern allows us to treat collections of objects as a single object, and the Decorator pattern allows us to add functionality to objects at runtime. These patterns are widely used in software development to make code more flexible, maintainable, and scalable.
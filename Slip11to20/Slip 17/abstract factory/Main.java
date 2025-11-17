interface Shape
{
void draw();
}

class RoundedRectangle implements Shape
{
public void draw()
{
System.out.println(" Inside RR");
}
}
class RoundedSquare implements Shape
{
public void draw()
{
System.out.println(" Inside RS");
}
}
class Rectangle implements Shape
{
public void draw()
{
System.out.println(" Inside Simple R");
}
}
class Square implements Shape
{
public void draw()
{
System.out.println(" Inside Simple Sq");
}
}
abstract class AbstractFactory
{
abstract Shape getShape( String st);
}
class ShapeFactory extends AbstractFactory
{
public Shape getShape( String st)
{
if(st.equalsIgnoreCase("Rectangle"))
{ return new Rectangle();}
else if(st.equalsIgnoreCase("Square"))
{ return new Square();}
return null;
}
}
class RoundedShapeFactory extends AbstractFactory
{
public Shape getShape( String st)

{
if(st.equalsIgnoreCase("Rectangle"))
{ return new RoundedRectangle();}
else if(st.equalsIgnoreCase("Square"))
{ return new RoundedSquare();}
return null;
}
}
class FactoryProducer
{
public static AbstractFactory getFactory(boolean rounded)
{
if (rounded)
{ return new RoundedShapeFactory();}
else
{ return new ShapeFactory();}
}
}
public class Main
{
public static void main(String[]args)
{
AbstractFactory shapeFactory=FactoryProducer.getFactory(false);
Shape shape1=shapeFactory.getShape("Rectangle");
shape1.draw();
Shape shape2=shapeFactory.getShape("SQuare");
shape2.draw();
AbstractFactory shapeFactory1=FactoryProducer.getFactory(true);
Shape shape3=shapeFactory1.getShape("REctangle");
shape3.draw();
Shape shape4=shapeFactory1.getShape("square");
shape4.draw();
}
}

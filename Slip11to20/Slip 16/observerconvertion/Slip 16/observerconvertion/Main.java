import java.util.ArrayList;
import java.util.List;
class Subject
{
private List<Observer>observers=new ArrayList<Observer>();
private int state;
public int getState()
{
return state;
}
public void setState(int s)
{
this.state=s;
notifyAllObservers();
}
public void attach (Observer o1)
{
observers.add(o1);
}
public void notifyAllObservers()
{
for(Observer o1: observers)
{
o1.update();
}
}
}
abstract class Observer
{
protected Subject s1;
public abstract void update();
}
class BinaryObserver extends Observer
{
public BinaryObserver(Subject s)
{
this.s1=s;
this.s1.attach(this);
}
public void update()
{
System.out.println("Binary String:" +Integer.toBinaryString(s1.getState()));
}
}
class OctalObserver extends Observer
{
public OctalObserver(Subject s)
{
this.s1=s;
this.s1.attach(this);
}
public void update()
{
System.out.println("Octal String:" +Integer.toOctalString(s1.getState()));
}
}
class HexaObserver extends Observer
{
public HexaObserver(Subject s)
{
this.s1=s;
this.s1.attach(this);
}
public void update()
{
System.out.println("Heaxdeciamal String:" +Integer.toHexString(s1.getState()));
}
}
public class Main
{
public static void main(String [] args)
{
Subject s1=new Subject();
new BinaryObserver(s1);
new OctalObserver(s1);
new HexaObserver(s1);
System.out.println("First state Change:15");
s1.setState(15);
System.out.println("Second state Change:10");
s1.setState(10);
}
}

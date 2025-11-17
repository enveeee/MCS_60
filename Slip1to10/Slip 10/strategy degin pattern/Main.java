interface DuckB
{
public void oper();
}
class Fly implements DuckB
{
public void oper()
{
System.out.println("Duck Flies");
}
}
class Quack implements DuckB
{
public void oper()
{
System.out.println("Duck Sounds Quack Quack");
}
}
class Context
{
private DuckB s1;
public Context(DuckB p)
{
this.s1=p;
}
public void est()
{
s1.oper();
}
}
public class Main
{
public static void main(String[] args) {
Context c1=new Context(new Fly());
System.out.println("Duck Behaviour");
c1.est();
c1=new Context(new Quack());
System.out.println("Duck Behaviour ");
c1.est();
}
}

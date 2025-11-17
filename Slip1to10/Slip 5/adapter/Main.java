import java.util.*;
class EnumerationIterator implements Iterator {
Enumeration enumeration;
public EnumerationIterator(Enumeration enumeration) {
this.enumeration = enumeration;
}
public boolean hasNext() {
return enumeration.hasMoreElements();
}
public Object next() {
return enumeration.nextElement();
}
public void remove() {
throw new UnsupportedOperationException();
}
}
public class Main {
public static void main (String args[]) {
Vector v = new Vector(Arrays.asList(args));
Iterator iterator = new EnumerationIterator(v.elements());
while (iterator.hasNext()) {
System.out.println(iterator.next());
}
}
}

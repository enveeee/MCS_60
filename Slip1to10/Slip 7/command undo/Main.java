interface Command {
public void execute();
}
class CeilingFan {
public void on(){
System.out.println("Ceiling Fan is on");
}
public void off()
{
System.out.println("Ceiling Fan is off");
}
}
class CeilingFanOnCommand implements Command {
CeilingFan c;
public CeilingFanOnCommand(CeilingFan l) {
this.c = l;
}
public void execute() {
c.on();
}
}
class CeilingFanOffCommand implements Command {
CeilingFan c;
public CeilingFanOffCommand(CeilingFan l) {
this.c = l;
}
public void execute() {
c.off();
}
}
class SimpleRemoteControl {
Command slot;
public SimpleRemoteControl() {}
public void setCommand(Command command) {
slot = command;
}
public void buttonWasPressed() {
slot.execute();
}
}
public class Main {
public static void main(String[] args) {
SimpleRemoteControl remote = new SimpleRemoteControl();
CeilingFan ceilingFan=new CeilingFan();
CeilingFanOnCommand ceilingFanOn =new CeilingFanOnCommand(ceilingFan);
remote.setCommand(ceilingFanOn);
remote.buttonWasPressed();
CeilingFanOffCommand ceilingFanOff =new CeilingFanOffCommand(ceilingFan);
remote.setCommand(ceilingFanOff);
remote.buttonWasPressed();
}
}

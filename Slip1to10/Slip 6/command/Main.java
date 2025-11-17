interface Command {
public void execute();
}
class Light {
public void on(){
System.out.println("Light is on");
}
public void off()
{
System.out.println("Light is off");
}
}
class LightOnCommand implements Command {
Light l1;
public LightOnCommand(Light a) {
this.l1 = a;
}
public void execute() {
l1.on();
}
}
class LightOffCommand implements Command {
Light l1;
public LightOffCommand(Light a) {
this.l1 = a;
}
public void execute() {
l1.off();
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
SimpleRemoteControl r1 = new SimpleRemoteControl();
Light l1 = new Light();
LightOnCommand lo = new LightOnCommand(l1);
r1.setCommand(lo);
r1.buttonWasPressed();
LightOffCommand lO = new LightOffCommand(l1);
r1.setCommand(lO);
r1.buttonWasPressed();
}
}

interface Command {
public void execute();
}

class Stereo {
public void On(){
System.out.println("Stereo is on");
}
}
class GarageDoor {
public void Up(){
System.out.println("Garage Door is Up");
}
}
class GarageDoorUpCommand implements Command {
GarageDoor c;
public GarageDoorUpCommand(GarageDoor l) {
this.c = l;
}
public void execute() {
c.Up();
}
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
Light light;
public LightOnCommand(Light light) {
this.light = light;
}
public void execute() {
light.on();
}
}
class LightOffCommand implements Command {
Light light;
public LightOffCommand(Light light) {
this.light = light;
}
public void execute() {
light.off();

}
}
class StereoOn implements Command {
Stereo s;
public StereoOn(Stereo l) {
this.s = l;
}
public void execute() {
s.On();
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
Light light = new Light();
LightOnCommand lightOn = new LightOnCommand(light);
remote.setCommand(lightOn);
remote.buttonWasPressed();
LightOffCommand lightOff = new LightOffCommand(light);
remote.setCommand(lightOff);
remote.buttonWasPressed();
GarageDoor garageDoor = new GarageDoor();
GarageDoorUpCommand garageDoorUp = new GarageDoorUpCommand(garageDoor);
remote.setCommand(garageDoorUp);
remote.buttonWasPressed();
Stereo s1=new Stereo();
StereoOn s2 =new StereoOn(s1);
remote.setCommand(s2);
remote.buttonWasPressed();
}
}

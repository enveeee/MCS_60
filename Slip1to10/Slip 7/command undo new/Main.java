
interface Command {
    void execute();
    void undo();

class CeilingFan {
    public void on() {
        System.out.println("Ceiling Fan is ON");
    }
    public void off() {
        System.out.println("Ceiling Fan is OFF");
    }
}

class CeilingFanOnCommand implements Command {
    CeilingFan fan;

    public CeilingFanOnCommand(CeilingFan fan) {
        this.fan = fan;
    }

    public void execute() {
        fan.on();
    }

    public void undo() {
        fan.off();
    }
}

class CeilingFanOffCommand implements Command {
    CeilingFan fan;

    public CeilingFanOffCommand(CeilingFan fan) {
        this.fan = fan;
    }

    public void execute() {
        fan.off();
    }

    public void undo() {
        fan.on();
    }
}

class SimpleRemoteControl {
    Command slot;

    public void setCommand(Command command) {
        slot = command;
    }

    public void buttonWasPressed() {
        slot.execute();
    }

    public void undoButtonWasPressed() {
        slot.undo();
    }
}

public class Main {
    public static void main(String[] args) {
        SimpleRemoteControl remote = new SimpleRemoteControl();
        CeilingFan ceilingFan = new CeilingFan();

       
        CeilingFanOnCommand fanOn = new CeilingFanOnCommand(ceilingFan);
        remote.setCommand(fanOn);
        remote.buttonWasPressed();     
        remote.undoButtonWasPressed(); 

       
        CeilingFanOffCommand fanOff = new CeilingFanOffCommand(ceilingFan);
        remote.setCommand(fanOff);
        remote.buttonWasPressed();   
        remote.undoButtonWasPressed(); 
    }
}


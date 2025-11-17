import java.util.*;

// --- MODEL INTERFACE ---
interface BeatModelInterface {
    void initialize();
    void on();
    void off();
    void setBPM(int bpm);
    int getBPM();
    void registerObserver(BeatObserver o);
    void removeObserver(BeatObserver o);
    void registerObserver(BPMObserver o);
    void removeObserver(BPMObserver o);
}

// --- OBSERVER INTERFACES ---
interface BeatObserver {
    void updateBeat();
}

interface BPMObserver {
    void updateBPM();
}

// --- MODEL CLASS ---
class BeatModel implements BeatModelInterface {
    private int bpm = 90;
    private List<BeatObserver> beatObservers = new ArrayList<>();
    private List<BPMObserver> bpmObservers = new ArrayList<>();

    public void initialize() {
        System.out.println("Model initialized.");
    }

    public void on() {
        System.out.println("Music started.");
        setBPM(90);
    }

    public void off() {
        System.out.println("Music stopped.");
        setBPM(0);
    }

    public void setBPM(int bpm) {
        this.bpm = bpm;
        notifyBPMObservers();
    }

    public int getBPM() {
        return bpm;
    }

    public void registerObserver(BeatObserver o) {
        beatObservers.add(o);
    }

    public void removeObserver(BeatObserver o) {
        beatObservers.remove(o);
    }

    public void registerObserver(BPMObserver o) {
        bpmObservers.add(o);
    }

    public void removeObserver(BPMObserver o) {
        bpmObservers.remove(o);
    }

    private void notifyBeatObservers() {
        for (BeatObserver o : beatObservers) o.updateBeat();
    }

    private void notifyBPMObservers() {
        for (BPMObserver o : bpmObservers) o.updateBPM();
    }

    public void beatEvent() {
        notifyBeatObservers();
    }
}

// --- VIEW CLASS ---
class DJView implements BeatObserver, BPMObserver {
    private BeatModelInterface model;

    public DJView(BeatModelInterface model) {
        this.model = model;
       model.registerObserver((BeatObserver) this); // Explicit cast
       model.registerObserver((BPMObserver) this);  
    }

    public void updateBPM() {
        int bpm = model.getBPM();
        if (bpm == 0) {
            System.out.println("DJ View: Offline");
        } else {
            System.out.println("DJ View: Current BPM = " + bpm);
        }
    }

    public void updateBeat() {
        System.out.println("DJ View: Beat occurred!");
    }
}

// --- CONTROLLER INTERFACE ---
interface ControllerInterface {
    void start();
    void stop();
    void increaseBPM();
    void decreaseBPM();
    void setBPM(int bpm);
}

// --- CONTROLLER CLASS ---
class BeatController implements ControllerInterface {
    private BeatModelInterface model;

    public BeatController(BeatModelInterface model) {
        this.model = model;
        new DJView(model); // View is created and linked with model
        model.initialize();
    }

    public void start() {
        model.on();
    }

    public void stop() {
        model.off();
    }

    public void increaseBPM() {
        model.setBPM(model.getBPM() + 1);
    }

    public void decreaseBPM() {
        model.setBPM(model.getBPM() - 1);
    }

    public void setBPM(int bpm) {
        model.setBPM(bpm);
    }
}

// --- MAIN CLASS ---
public class Main {
    public static void main(String[] args) {
        BeatModelInterface model = new BeatModel();
        ControllerInterface controller = new BeatController(model);

        controller.start();
        controller.increaseBPM();
        controller.setBPM(120);
        controller.decreaseBPM();
        controller.stop();
    }
}


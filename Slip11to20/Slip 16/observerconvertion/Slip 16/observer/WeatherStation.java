import java.util.Observable;
import java.util.Observer;

// Subject (Observable)
class WeatherData extends Observable {
    private float temperature, humidity, pressure;

    public void setMeasurements(float temp, float hum, float pres) {
        this.temperature = temp;
        this.humidity = hum;
        this.pressure = pres;
        setChanged();
        notifyObservers();
    }

    public float getTemperature() { return temperature; }
    public float getHumidity() { return humidity; }
    public float getPressure() { return pressure; }
}

// Observer interface
interface DisplayElement {
    void display();
}

// Current Conditions Display
class CurrentConditionsDisplay implements Observer, DisplayElement {
    private float temperature, humidity;

    public CurrentConditionsDisplay(Observable observable) {
        observable.addObserver(this);
    }

    public void update(Observable o, Object arg) {
        WeatherData data = (WeatherData) o;
        temperature = data.getTemperature();
        humidity = data.getHumidity();
        display();
    }

    public void display() {
        System.out.println("Current: " + temperature + "F, " + humidity + "% humidity");
    }
}

// Forecast Display
class ForecastDisplay implements Observer, DisplayElement {
    private float lastPressure = 29.92f, currentPressure;

    public ForecastDisplay(Observable o) {
        o.addObserver(this);
    }

    public void update(Observable o, Object arg) {
        WeatherData data = (WeatherData) o;
        lastPressure = currentPressure;
        currentPressure = data.getPressure();
        display();
    }

    public void display() {
        System.out.print("Forecast: ");
        if (currentPressure > lastPressure) System.out.println("Improving weather!");
        else if (currentPressure == lastPressure) System.out.println("No change");
        else System.out.println("Watch out for cooler, rainy weather");
    }
}

// Main App
public class WeatherStation {
    public static void main(String[] args) {
        WeatherData weatherData = new WeatherData();

        new CurrentConditionsDisplay(weatherData);
        new ForecastDisplay(weatherData);

        weatherData.setMeasurements(80, 65, 30.4f);
        weatherData.setMeasurements(82, 70, 29.2f);
        weatherData.setMeasurements(78, 90, 29.2f);
    }
}

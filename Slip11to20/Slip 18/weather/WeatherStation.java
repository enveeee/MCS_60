import java.util.Observable;
import java.util.Observer;

// WeatherData class extends Observable
class WeatherData extends Observable {
    private float temperature;
    private float humidity;
    private float pressure;

    public void setMeasurements(float temperature, float humidity, float pressure) {
        this.temperature = temperature;
        this.humidity = humidity;
        this.pressure = pressure;
        measurementsChanged();
    }

    public void measurementsChanged() {
        setChanged(); // mark the observable as changed
        notifyObservers(); // notify all observers
    }

    public float getTemperature() {
        return temperature;
    }

    public float getHumidity() {
        return humidity;
    }

    public float getPressure() {
        return pressure;
    }
}

// Display class implements Observer
class CurrentConditionsDisplay implements Observer {
    private float temperature;
    private float humidity;

    public void update(Observable obs, Object arg) {
        if (obs instanceof WeatherData) {
            WeatherData weatherData = (WeatherData) obs;
            this.temperature = weatherData.getTemperature();
            this.humidity = weatherData.getHumidity();
            display();
        }
    }

    public void display() {
        System.out.println("Current conditions: " + temperature + "°C and " + humidity + "% humidity");
    }
}

// Main class
public class WeatherStation {
    public static void main(String[] args) {
        WeatherData weatherData = new WeatherData();
        CurrentConditionsDisplay display = new CurrentConditionsDisplay();

        // Register observer
        weatherData.addObserver(display);

        // Simulate new weather readings
        weatherData.setMeasurements(30.0f, 65.0f, 1013.1f);
        weatherData.setMeasurements(28.5f, 70.0f, 1012.5f);
    }
}


function getWeather() {
    let city = document.getElementById("city").value;
    let country = document.getElementById("country").value;

    if (!city) {
        alert("Please enter a city name");
        return;
    }

    let url = `http://127.0.0.1:5000/weather?city=${city}&country=${country}`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert("Error: " + data.error);
                return;
            }

            document.getElementById("weather-location").innerText = `${data.city}, ${data.country}`;
            document.getElementById("weather-description").innerText = data.description;
            document.getElementById("temperature").innerText = data.temperature;
            document.getElementById("feels_like").innerText = data.feels_like;
            document.getElementById("humidity").innerText = data.humidity;
            document.getElementById("wind_speed").innerText = data.wind_speed;
            document.getElementById("pressure").innerText = data.pressure;
        })
        .catch(error => {
            alert("Failed to fetch weather data. Please try again.");
            console.error("Error:", error);
        });
}

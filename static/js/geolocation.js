if (!navigator.geolocation) {
    console.log("location not available");
} else {
    navigator.geolocation.getCurrentPosition(getPosition);
}

function getPosition(position) {
    var lat = position.coords.latitude;
    var long = position.coords.longitude;

    document.querySelector('input[name="latitude"]').value = lat;
    document.querySelector('input[name="longitude"]').value = long;
}

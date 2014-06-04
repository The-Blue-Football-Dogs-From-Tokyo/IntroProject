// When the page loads, we will set the form's submit function to searchAPI.
// Returning false prevents page refresh
$(document).ready(function() {
    $("form").submit(function (e) {
        e.preventDefault();
        searchAPI();
    });
})

function searchAPI() {
    var productName = document.getElementById("productName").value;
    var requestURL = "https://api.sgt.io/products/?api_key=14a5eb7c31cdf6e9a9758ba7f32224c20fcc1137&q=" + productName + "&format=jsonp";
    // Cross-domain issues came up, so we're using this niftier ajax request
    $.ajax({
        url: requestURL,
        type: "GET",
        crossDomain: true,
        dataType: "jsonp",
        jsonpCallback: "display",
        timeout: 1000
    });
}

function searchError() {
    // Probably should do an error log here
    document.getElementById("textBox").innerHTML = "Failed";
    return false;
}

// array is an array of Objects that represent the returned json objects from the api
function display(array) {
    document.getElementById("textBox").innerHTML = "Success";
    return false;
}

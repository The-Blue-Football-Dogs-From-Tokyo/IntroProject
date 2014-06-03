function search() {
    var script = document.createElement('script');
    script.src = 'http://code.jquery.com/jquery-1.11.0.min.js';
    script.type = 'text/javascript';
    document.getElementsByTagName('head')[0].appendChild(script);
    var productName = $("#productName").value;
    var requestURL = "https://api.sgt.io/products/?api_key=4c4ec8961617eee94e2469b1fea9f5587d64b6d3&q=" + productName;
    $.ajax({
        url: requestURL,
        type: 'GET',
        success: display,
        error: searchError
    });
}

function searchError() {
    // Probably should do an error log here
}

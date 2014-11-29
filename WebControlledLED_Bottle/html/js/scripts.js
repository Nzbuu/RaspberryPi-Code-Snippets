var main = function() {
// insert code here
$(".OnButton").click(function() {
    
    // Create Json object
    data  = {"LedStatus":true};

    var json_on = JSON.stringify(data);



    try{
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "http://192.168.0.14:8080/SetStatus", false);

        //Send the proper header information along with the request
        xhr.setRequestHeader("Content-type", "application/json");
        xhr.send(json_on);
    }
    catch(err){alert("Turn On: Server on Pi unavailable!")}
    
    // Get state of LED from server
    xhr.open("GET", "http://192.168.0.14:8080/GetStatus", false);
    xhr.send();    

    var response = JSON.parse(xhr.responseText);

    var isTrue = (response.LedStatus === 'True' || response.LedStatus === '1');
    // Only turn on the LED image on the website if the server turned on the real one
    if (isTrue){
    $(".circle").removeClass("off");
    $(".circle").addClass("on");
    $("#belowLED").append("<p>On</p>")
    // TODO: limit the history
    }
   

});
$(".OffButton").click(function() {
    // Create Json object
    data  = {"LedStatus":false};

    var json_off = JSON.stringify(data);

        // Update HTML file
    try{
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "http://192.168.0.14:8080/SetStatus", false);

        //Send the proper header information along with the request
        xhr.setRequestHeader("Content-type", "application/json");
        xhr.send(json_off);
    }
   
    catch(err){alert("Turn Off: Server on Pi unavailable!")}

    // Get state of LED from server
    xhr.open("GET", "http://192.168.0.14:8080/GetStatus", false);
    xhr.send();  

    var response = JSON.parse(xhr.responseText);

    var isFalse = (response.LedStatus === 'False' || response.LedStatus === '0' );
    // Only turn off the LED image on the website if the server turned off the real one
    if (isFalse){
    $(".circle").removeClass("on");
    $(".circle").addClass("off");
    $("#belowLED").append("<p>Off</p>")
     // TODO: limit the history
  }

});
};

$(document).ready(main);



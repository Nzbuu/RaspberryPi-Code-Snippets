function init()  {

//Create On Button
var button = webiopi().createButton(
    "button_on", // id
    "On", // Label
    led_on); // press , /'release (optional)
    $(".OnButton").append(button);

// Create Off Button
var button = webiopi().createButton(
    "button_off", // id
    "Off", // Label
    led_off); // press , /'release (optional)
    $(".OffButton").append(button);
}

function led_on() {
  webiopi().callMacro("led_on");
}

function led_off() {
  webiopi().callMacro("led_off");
}

webiopi().ready(init);

var main = function(){

    // remove the last child of the header if it is webiopi style sheet
    var head   = document.getElementsByTagName('head')[0];
    
    var lastHeadChild = head.lastChild;

    var name = lastHeadChild.getAttribute('href');
    if (name.search("webiopi") > 0){
        head.removeChild(lastHeadChild)
    }


    $(".OnButton").click(function() {
    $(".circle").removeClass("off");
    $(".circle").addClass("on");
    $("#belowLED").append("<p>On</p>")
    // TODO: limit the history
    });

    $(".OffButton").click(function() {
    $(".circle").removeClass("on");
    $(".circle").addClass("off");
    $("#belowLED").append("<p>Off</p>")
     // TODO: limit the history
});
}

$(document).ready(main);






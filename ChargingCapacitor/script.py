def main():
    # Create global variable for pinslse
    pin_in = 17
    pin_out  = 13
    Capacitance = 10e-6; # Capacitance [F]

    Thermometer = ThermistorThermometer(pin_in, pin_out, Capacitance)
    
    T_deg = Thermometer.readTemperature();

    print "Temperature = " + str(round(T_deg,1)) + " degC"

    print "wait for capacitor discharge"
    time.sleep(5 * Thermometer.tau);
    
    print "goodbye"

try:
    main()
finally:
	del Thermometer;
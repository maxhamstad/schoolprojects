package src;

public class Storm {
	/**
     * rain
     */
	private String percip;
	/**
     * inches of rain 
     */
    private double inches;
    /**
     * duration in hours of rain
     */
    private int hours;
  

    /**
     * Constructor to initialize a new movie.
     * 
     * @param percip     type of percepitation
     * @param inches       inches of rain
     * @param hours  duration of the rain
     */
    public Storm(String percip, double inches, int hours){
    this.percip = percip;
    this.inches = inches;
    this.hours = hours;
    }
	/**
     * returns the type of percipitation
     * 
     * @return rain
     */
    public String getPrecipType() {
        return this.percip;
    }
    /**
     * Sets the type of precipitation.
     * 
     * @param percip Type of precipitation
     */
    public void setPrecipType(String percip) {
        this.percip = percip;
    }

    /**
     * Gets the inches of percipiation.
     * 
     * @return inches of percipitation
     */
    public double getPrecipInches() {
        return this.inches;
    }

    /**
     * Sets the inches of the percipitation.
     * 
     * @param percipitation of the rain in inches
     */
    public void setPrecipInches(double inches) {
        this.inches = inches;
    }
    
    /**
     * Gets the hours of percipiation.
     * 
     * @return hours of percipitation
     */
    public int getStormLength() {
        return this.hours;
    }

    /**
     * Sets the hours of the hours.
     * 
     * @param percipitation of the rain in hours
     */
    public void setStormLength(int hours) {
        this.hours = hours;
    }
    /**
     * Calculates the precipitation rate per hour.
     * 
     * @return Inches per hour
     */
    public double getPrecipPerHour() 
    {
    	if (this.hours == 0) {
    		return 0; 
    	}
    	return this.inches / this.hours;
    }

    /**
     * Returns a string representation of the Storm object.
     * 
     * @return Storm details
     */
    @Override
    public String toString() {
        return "This Storm dropped " + inches + " inches of " + percip + " over the course of " + hours + " hours." + "averging " 
    + getPrecipPerHour() + " inches per hour";
    }
}

package src;

public class StormDriver {

	// DO NOT alter this main method
		public static void main(String[] args) {

			//Create a Storm object
			Storm gentleRain = new Storm("rain", 1.5, 3);

			//This will trigger an automatic call to Storm.toString()
			System.out.println(gentleRain);

			//Try to change a value using the setter method
			gentleRain.setPrecipInches(2.5);

			//Make sure it changed
			System.out.println(gentleRain);

			System.out.println("Testing a few getter methods:");
			System.out.println(gentleRain.getPrecipType() + " " 
					+ gentleRain.getPrecipInches() + " "
					+ gentleRain.getStormLength());
			System.out.println(gentleRain.getPrecipPerHour());

			//Create and print out a snow storm of the century
			//48 inches of snow over the course of 36 hours
			Storm stormOfCentury = new Storm("snow", 48, 36);
			System.out.println(stormOfCentury);

		}
}

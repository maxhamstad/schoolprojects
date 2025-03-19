package src;

public class RomanticComedy extends Movie {
protected String bestFriend;
	
	//Constructor
	public RomanticComedy(String title, String director, String bestFriend) {
		super(title, director); // Calls the parent class (Movie) constructor
		setBestFriend(bestFriend);
	}

	public String getBestFriend() {
		return bestFriend;
	}
	
	public void setBestFriend(String bestFriend) {
		this.bestFriend = bestFriend;
	}
	@Override 
	public String toString() {
		return super.toString() + " It is a Romantic Comedy. " + bestFriend + "is the main characters best friend who was right in front of them the whole time but they didn't realize they were in love.";
				
}
}

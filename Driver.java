package src;

public class Driver {

		public static void main(String[] args) {
			//This chunk of code should work once you've completed part 1
			Movie m1 = new Movie("Star Wars", "George Lucas");
			System.out.println(m1);//calls Movie.toString()
			System.out.println(); //blank line
			
			
			RomanticComedy rc1 = new RomanticComedy("You've Got Mail", "Nora Ephron", "Joe Fox");
			System.out.println(rc1);//calls RomanticComedy.toString()
			System.out.println(); //blank line
			

			//This chunk of code will need to wait until you've completed part 3
			ActionFilm af1 = new ActionFilm("Transformers", "Michael Bay", 5213);
			System.out.println(af1); //calls ActionFilm.toString()
			System.out.println(); //blank line
			
			//TODO Complete part 4 here
			Movie m2 = af1;
			//ActionFilm af2 = m1;
			//can convert a action film to a movie 
			//but cannot convert a movie into a action film 
			System.out.println(m2);
			System.out.println("M2 title is: " + m2.getTitle());
			//System.out.println("M2 number of explosions is: " + m2.getNumExplosions());
			//movie does not have numExplosions
			
			//Leave this commented out until you do part 5
			//TODO create your array of Movie objects here
			
			Movie[] myMovies = new Movie[5];
			myMovies[0] = new Movie("Inception", "Christopher Nolan");
			myMovies[1] = new RomanticComedy("You've Got Mail", "Nora Ephron", "Joe Fox");
			myMovies[2] = new ActionFilm("Mad Max: Fury Road", "George Miller", 215);
			myMovies[3] = new Movie("The Godfather", "Francis Ford Coppola");
			myMovies[4] = new ActionFilm("Die Hard", "John McTiernan", 30);

			System.out.println("My list of movies is: ");
			for(int i = 0; i < myMovies.length; i++){
				System.out.println(myMovies[i]);
				System.out.println();//blank line
			}

		}
	}
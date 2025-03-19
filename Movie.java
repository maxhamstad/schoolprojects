package src;

public class Movie {
	protected String title; 
	protected String director;
	
	public Movie(String title, String director) {
		setTitle(title);
		setDirector(director);
	}

	public String getTitle() {
		return title;
	}
	
	public void setTitle(String title) {
		this.title = title;
	}
	public String getDirector() {
		return director;
	}
	
	public void setDirector(String director) {
		this.director = director;
	}
	@Override
	public String toString() {
		return "this movie is \"" + title + "\", directed by " + director  + ".";
	}
}

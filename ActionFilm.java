package src;

public class ActionFilm extends Movie {
    private int numExplosions;

    public ActionFilm(String title, String director, int numExplosions) {
        super(title, director); 
        setNumExplosions(numExplosions);
    }

    public int getNumExplosions() {
        return numExplosions;
    }

    public void setNumExplosions(int numExplosions) {
        this.numExplosions = numExplosions;
    }

    @Override
    public String toString() {
        return super.toString() + " It is an Action Film, and has " + numExplosions + " explosions.";
    }
}
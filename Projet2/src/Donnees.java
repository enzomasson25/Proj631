package stockageDonnee;

public class Donnees {
	
	
	private int IDdonnee;
	private int taille;
	
	
	//Getters/Setters
		public int getIDdonnee() {
			return IDdonnee;
		}
		
		public int getTaille() {
			return taille;
		}
	
	//Constructor
	public Donnees(int iDdonnee, int taille) {
		IDdonnee = iDdonnee;
		this.taille = taille;
	}

	//toString
	@Override
	public String toString() {
		return "Donnees [IDdonnee=" + IDdonnee + ", taille=" + taille + "]";
	}
	
}

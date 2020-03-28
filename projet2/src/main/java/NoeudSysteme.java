
import java.util.ArrayList;

public class NoeudSysteme {
	
	private int idNoeudSyst;
	private int capacite;
	private ArrayList<Integer> listeDonneesStockees = new ArrayList<Integer>();
	private ArrayList<NoeudSysteme> noeudAccessibles = new ArrayList<NoeudSysteme>();
	
	//Getters/Setters
	public int getIdNoeud() {
		return this.idNoeudSyst;
	}
	
	public ArrayList<Integer> getListeDonneesStockees() {
		return listeDonneesStockees;
	}
	public void setListeDonneesStockees(ArrayList<Integer> listeDonneesStockees) {
		this.listeDonneesStockees = listeDonneesStockees;
	}
	
	public int getCapacite() {
		return this.capacite;
	}
	public void setCapacite(int capacite) {
		this.capacite = capacite;
	}
	
	public ArrayList<NoeudSysteme> getNoeudAccessibles() {
		return noeudAccessibles;
	}
	public void setNoeudAccessibles(ArrayList<NoeudSysteme> noeudAccessibles) {
		this.noeudAccessibles = noeudAccessibles;
	}

	//Constructor
	public NoeudSysteme(int idNoeudSyst, int capacite) {
		this.idNoeudSyst = idNoeudSyst;
		this.capacite = capacite;
	}
	
	//toString
	@Override
	public String toString() {
		return "NoeudSysteme [idNoeudSyst=" + idNoeudSyst + ", capacite=" + capacite + ", listeDonneesStockees="
				+ listeDonneesStockees + ", noeudAccessibles=" + noeudAccessibles + "]";
	}

	//Methods
	public void ajouterDonnee(Donnees donnee) {
		this.listeDonneesStockees.add(donnee.getIDdonnee());
		this.capacite = this.capacite - donnee.getTaille() ;
	}
	
	public void ajouterNoeudAccessible(NoeudSysteme noeud) {
		this.noeudAccessibles.add(noeud);
	}

}

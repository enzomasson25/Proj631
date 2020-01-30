import java.util.List;

public class utilisateur {

	private int id;
	private List<Integer> liste_donnee_interet;
	private int id_noeud;
	
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public List<Integer> getListe_donnee_interet() {
		return liste_donnee_interet;
	}
	public void setListe_donnee_interet(List<Integer> liste_donnee_interet) {
		this.liste_donnee_interet = liste_donnee_interet;
	}
	public int getId_noeud() {
		return id_noeud;
	}
	public void setId_noeud(int id_noeud) {
		this.id_noeud = id_noeud;
	}
	
	public utilisateur(int id, List<Integer> liste_donnee_interet, int id_noeud) {
		super();
		this.id = id;
		this.liste_donnee_interet = liste_donnee_interet;
		this.id_noeud = id_noeud;
	}
	
}

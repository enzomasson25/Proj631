import java.util.List;

public class noeud {
	
	private int id;
	private int capacite;
	private List<Integer> donnee_sto_lcl;
	private List<Integer> noeuds_accessibles;
	
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public int getCapacite() {
		return capacite;
	}
	public void setCapacite(int capacite) {
		this.capacite = capacite;
	}
	public List<Integer> getDonnee_sto_lcl() {
		return donnee_sto_lcl;
	}
	public void setDonnee_sto_lcl(List<Integer> donnee_sto_lcl) {
		this.donnee_sto_lcl = donnee_sto_lcl;
	}
	public List<Integer> getNoeuds_accessibles() {
		return noeuds_accessibles;
	}
	public void setNoeuds_accessibles(List<Integer> noeuds_accessibles) {
		this.noeuds_accessibles = noeuds_accessibles;
	}
	
	public noeud(int id, int capacite, List<Integer> donnee_sto_lcl, List<Integer> noeuds_accessibles) {
		super();
		this.id = id;
		this.capacite = capacite;
		this.donnee_sto_lcl = donnee_sto_lcl;
		this.noeuds_accessibles = noeuds_accessibles;
	}

	 
}

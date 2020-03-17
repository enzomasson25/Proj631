package stockageDonnee;
import org.jgrapht.graph.DefaultWeightedEdge;
import org.jgrapht.graph.SimpleWeightedGraph;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

import org.jgrapht.GraphPath;
import org.jgrapht.alg.*;

public class Graphe<Noeud,Edge> extends SimpleWeightedGraph {
	
	
	private ArrayList<Utilisateurs> listeUtil = new ArrayList<Utilisateurs>();
	private ArrayList<Donnees> listeDonneesAPlacer = new ArrayList<Donnees>();
	private ArrayList<Donnees> listeDonneesPlacees = new ArrayList<Donnees>();
	private ArrayList<NoeudSysteme> listeNoeud = new ArrayList<NoeudSysteme>();

	
	public Graphe(Class arg0) {
		super(arg0);
	}
	
	
	public List cheminLePlusCourt(NoeudSysteme n1,NoeudSysteme n2) {
		DijkstraShortestPath<NoeudSysteme,Edge> dij = new DijkstraShortestPath<NoeudSysteme,Edge> (this, n1, n2);
		return dij.findPathBetween(this, n1, n2);
	}
	
	
	public void ajouterUtils(ArrayList<Utilisateurs> utils) {
		for(int i = 0;i<utils.size();i++) {
			this.addVertex(utils);
		}
	}
	
	public void ajouterUnUtil(Utilisateurs util) {
		this.listeUtil.add(util);
	}
	
	
	public void ajouterNoeud(ArrayList<NoeudSysteme> noeud) {
		for(int i = 0;i<noeud.size();i++) {
			this.addVertex(noeud);
			this.listeNoeud.add(noeud.get(i));
		}
	}
	
	
	public void ajouterDonneesAPlacer(ArrayList<Donnees> don) {
		for(int i = 0;i<don.size();i++) {
			this.listeDonneesAPlacer.add(don.get(i));
		}
	}
	
	
	public void donneesAEtePlace(Donnees don) {
		this.listeDonneesAPlacer.remove(don);
		this.listeDonneesPlacees.add(don);
	}
	
	
	public Donnees getDonneeById(Integer id) {
		for(int i = 0;i<this.listeDonneesAPlacer.size();i++) {
			if(this.listeDonneesAPlacer.get(i).getIDdonnee() == id) {
				return this.listeDonneesAPlacer.get(i);
			}
		}
		return null;
	}
	
	
	public ArrayList<Donnees> getDonneesAPlacerParUtil(Utilisateurs util){
		ArrayList<Donnees> arr = new ArrayList<Donnees>();
		for(int i = 0;i<util.getListeIdDonnees().size();i++) {
			if(util.getListeIdDonnees().get(i) == this.listeDonneesAPlacer.get(i).getIDdonnee()) {
				arr.add(this.listeDonneesAPlacer.get(i));
			}
		}
		return arr;
	}
	
	
	public void ajouterNoeudGraphe(NoeudSysteme noeud) {
		this.listeNoeud.add(noeud);
	}
	
	
	
	public void ajouterPlusieursNoeud(ArrayList<NoeudSysteme> noeuds) {
		for(int i = 0;i<noeuds.size();i++) {
			this.listeNoeud.add(noeuds.get(i));
		}
	}
	
	
	public NoeudSysteme getNoeudById(int idNoeud) {
		for(int i = 0;i<this.listeNoeud.size();i++) {
			if (this.listeNoeud.get(i).getIdNoeud() == idNoeud){
				return this.listeNoeud.get(i);
			}
		}
		System.out.println("Le noeud cherche n'est pas dans le graphe");
		return null;
	}
	
	
	public ArrayList<Donnees> getListeIntermed(ArrayList<Donnees> don){
		ArrayList<Donnees> intermed = new ArrayList<Donnees>();
		for(Donnees donnee : don) {
			intermed.add(donnee);
		}
		return intermed;
	}
	

	
	
	
	public void affichageNoeudGraphe() {
		for(NoeudSysteme n : this.listeNoeud) {
			System.out.println("Noeud : " + n.getIdNoeud() + " capacite : "+n.getCapacite() + " donnees placees : "+n.getListeDonneesStockees());
		}
	}
	

}

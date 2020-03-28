
import org.jgrapht.graph.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;



public class Graphe<Noeud,Edge> extends SimpleWeightedGraph {
	
	
	private ArrayList<Utilisateurs> listeUtil = new ArrayList<Utilisateurs>();
	private ArrayList<Donnees> listeDonneesAPlacer = new ArrayList<Donnees>();
	private ArrayList<Donnees> listeDonneesPlacees = new ArrayList<Donnees>();
	private ArrayList<NoeudSysteme> listeNoeud = new ArrayList<NoeudSysteme>();

	//constructor
	public Graphe(Class arg0) {
		super(arg0);
	}
	
	//methods
	public void ajouterUnUtil(Utilisateurs util) {
		this.listeUtil.add(util);
	}
	

	public void ajouterDonneesAPlacer(ArrayList<Donnees> don) {
		for(int i = 0;i<don.size();i++) {
			this.listeDonneesAPlacer.add(don.get(i));
		}
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
	
	public NoeudSysteme getNoeudById(int idNoeud) {
		for(int i = 0;i<this.listeNoeud.size();i++) {
			if (this.listeNoeud.get(i).getIdNoeud() == idNoeud){
				return this.listeNoeud.get(i);
			}
		}
		System.out.println("Le noeud "+idNoeud +" n'est pas dans le graphe");
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
			System.out.println("Noeud : " + n.getIdNoeud() + "\n	capacite : "+n.getCapacite() + "\n	donnees placees : "+n.getListeDonneesStockees());
		}
	}
	
	
	public void placerDonneeDansGraphe(Utilisateurs util) {
		ArrayList<Donnees> aPlacer = new ArrayList<Donnees>();
		ArrayList<Donnees> intermed = new ArrayList<Donnees>();
			aPlacer = this.getDonneesAPlacerParUtil(util);
			intermed = this.getListeIntermed(aPlacer);
			NoeudSysteme nUtil = this.getNoeudById(util.getNoeudAccessible());
			for (int j = 0;j<aPlacer.size();j++) {
				if (aPlacer.get(j).getTaille() <= nUtil.getCapacite()) {
					nUtil.ajouterDonnee(aPlacer.get(j));
					intermed.remove(aPlacer.get(j));
				}else {
					ArrayList<NoeudSysteme> nAccessibles = nUtil.getNoeudAccessibles();
					double min = 1000;
					NoeudSysteme nSuivant = null;
					for(NoeudSysteme n : nAccessibles) {
						if (this.getEdgeWeight(this.getEdge(nUtil,n))< min & n.getCapacite()>= aPlacer.get(j).getTaille()) {
							min = this.getEdgeWeight(this.getEdge(nUtil,n));
							nSuivant = n;
						}
					}
					if(nSuivant != null) {
						nSuivant.ajouterDonnee(aPlacer.get(j));
						intermed.remove(aPlacer.get(j));	
					}else {
						this.placerDonneesDescendant(nUtil, aPlacer.get(j));
						intermed.remove(aPlacer.get(j));
					}
				}
		}if(intermed.size() > 0 ) {
			System.out.println(intermed);
			System.out.println("Pas assez de place pour ces données ! :(");
		}else {
			System.out.println("Les donnees "+this.getDonneesAPlacerParUtil(util)+" de l'utilisateur "+util.getIdUtil()+" ont bien été placés");
		}
	}
	
	public void placerDonneesDescendant(NoeudSysteme n,Donnees don) {
		ArrayList<NoeudSysteme> arrNoeud = this.getNoeudAccessibleDescendant(n);
		for(NoeudSysteme noeud : arrNoeud) { 
			if(noeud.getCapacite() >= don.getTaille()) {
				noeud.ajouterDonnee(don);
			}
		}
	}
	
	public ArrayList<NoeudSysteme> getNoeudAccessibleDescendant(NoeudSysteme n) {
		ArrayList<NoeudSysteme> noeuds = new ArrayList<NoeudSysteme>();
		for (NoeudSysteme noeud : n.getNoeudAccessibles()) {
			NoeudSysteme noeud2 = noeud;
			for(NoeudSysteme noeudIntermed : noeud2.getNoeudAccessibles()) {
				noeuds.add(noeudIntermed);
			}
		}
		return noeuds;
	}
	
	

}


import java.util.ArrayList;

import org.jgrapht.graph.*;
import org.jgrapht.graph.SimpleWeightedGraph;



public class Main {

	public static void main(String[] args) {
		
		//Question 2 
		Graphe<NoeudSysteme, Edge> graphe = new Graphe <>(Edge.class);
		
		Donnees donnee0 = new Donnees(0,40);
		Donnees donnee1 = new Donnees(1,25);
		Donnees donnee2 = new Donnees(2,25);
	    
		ArrayList<Donnees> listeDonnee = new ArrayList<Donnees>();
		listeDonnee.add(donnee0);
		listeDonnee.add(donnee1);
		listeDonnee.add(donnee2);
		graphe.ajouterDonneesAPlacer(listeDonnee);
		
		NoeudSysteme noeud0 = new NoeudSysteme(0, 50);
		NoeudSysteme noeud1 = new NoeudSysteme(1, 40);
		NoeudSysteme noeud2 = new NoeudSysteme(2, 40);
		
		noeud0.ajouterNoeudAccessible(noeud1);
		noeud1.ajouterNoeudAccessible(noeud2);
		
		graphe.ajouterNoeudGraphe(noeud0);
		graphe.ajouterNoeudGraphe(noeud1);
		graphe.ajouterNoeudGraphe(noeud2);
		
		ArrayList<Integer> noeudUtil1 = new ArrayList<Integer>();
		noeudUtil1.add(noeud0.getIdNoeud());
		noeudUtil1.add(noeud1.getIdNoeud());
		noeudUtil1.add(noeud2.getIdNoeud());
		Utilisateurs util1 = new Utilisateurs(0,noeudUtil1,0);
		
		
		graphe.ajouterUnUtil(util1);
		
		graphe.addVertex(noeud0);
		graphe.addVertex(noeud1);
		graphe.addVertex(noeud2);
		
		DefaultWeightedEdge edge1 = (DefaultWeightedEdge)graphe.addEdge(noeud0, noeud1);
		DefaultWeightedEdge edge2 = (DefaultWeightedEdge)graphe.addEdge(noeud1, noeud2);
		
		graphe.setEdgeWeight(edge1, 1);
		graphe.setEdgeWeight(edge2, 1);
		
		graphe.placerDonneeDansGraphe(util1);
		
		graphe.affichageNoeudGraphe();
		
	}

}

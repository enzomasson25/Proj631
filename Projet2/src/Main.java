package stockageDonnee;

public class Main {

	public static void main(String[] args) {
		
		//Question 2 
		Donnees donnee0 = new Donnees(0,40);
		Donnees donnee1 = new Donnees(1,25);
		Donnees donnee2 = new Donnees(2,25);
	    
		NoeudSysteme noeud0 = new NoeudSysteme(0, 50);
		NoeudSysteme noeud1 = new NoeudSysteme(1, 40);
		NoeudSysteme noeud2 = new NoeudSysteme(2, 40);
		
		noeud0.ajouterNoeudAccessible(noeud1);
		noeud1.ajouterNoeudAccessible(noeud2);
		
		
	}

}

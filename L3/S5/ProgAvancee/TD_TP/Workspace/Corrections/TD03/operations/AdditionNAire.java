package up.mi.jgm.td03.operations;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * Represente une addition generalisee avec arite quelconque
 * @author Jean-Guy Mailly
 *
 */
public class AdditionNAire extends Operateur {
	/**
	 * Les operandes de l'addition
	 */
	private List<Operateur> operandes;

	/**
	 * Construit une addition "vide"
	 */
	public AdditionNAire() {
		super(0);
		operandes = new ArrayList<Operateur>();
	}
	
	/**
	 * Construit une addition a partir de la liste de ses operandes
	 * @param operandes la liste d'operandes
	 */
	public AdditionNAire(List<Operateur> operandes) {
		this();
		this.operandes.addAll(operandes);
		for(int i = 0 ; i < operandes.size();i++)
			incrementeArite();
	}
	
	/**
	 * Ajoute un operande a l'addition
	 * @param op
	 */
	public void ajouteOperande(Operateur op) {
		operandes.add(op);
		incrementeArite();
	}

	@Override
	public double evaluer() {
		double somme = 0;
		for (Operateur op : operandes)
			somme += op.evaluer();
		return somme;
	}

	@Override
	public String toString() {
		if(getArite() == 0) {
			return "0" ;
		}
		StringBuilder build = new StringBuilder();
		Iterator<Operateur> it = operandes.iterator();
		
		Operateur op = it.next();
		if(op instanceof Valeur) {
			build.append(op.toString());
		}else {
			build.append("(");
			build.append(op.toString());
			build.append(")");
		}
		
		while(it.hasNext()) {
			build.append("+");
			op = it.next();
			if(op instanceof Valeur) {
				build.append(op.toString());
			}else {
				build.append("(");
				build.append(op.toString());
				build.append(")");
			}
		}
		
		return build.toString();
	}
}

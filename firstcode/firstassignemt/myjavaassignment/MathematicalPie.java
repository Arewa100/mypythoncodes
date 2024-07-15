public class MathematicalPie {
	public static void main(String[] args) {
		System.out.println("Welcome to my math pie calculator");
	
	int number = 4;
	int pi = 0;
	int terms = 1;
	int odd = 1;
	
	for(int counter = 1; counter <= 301; counter++) {
		if(counter % 2 == 1) {
			terms = number/odd;
		}
		else if (counter % 2 == 0) {
			terms = -(number/odd);
}
		pi = pi + terms;
		odd = odd + 1;
	System.out.println(pi);
}	 
}
}
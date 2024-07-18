public class NumberFinder {
	public static void main(String[] args) {
		System.out.println("Welcome to the number finder");
		
	int number = 770;
			
	while(number <= 4200) {
		int conditionOne = number % 7;
		if(conditionOne == 0) {
			int conditionTwo = number;
			if(conditionTwo % 5 != 0) {
				System.out.print(conditionTwo + "  ,");
			}
		}
	   number = number + 1;		
	}

}
}
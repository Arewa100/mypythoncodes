import java.util.Scanner;

public class BankApp {
	public static void main(String[] args) {	
		System.out.println("Welome friend: what is your name? ")
	
	Scanner input = new Scanner();

		String name;
		int balance = 0
		String sentinel = "E";
	
	System.out.println("What is your name?");
		name = input.nextLine();
		
		while(!sentinel.equal("E")) {
			System.out.println("Enter 'D'deposit, 'W' to withdraw OR 'E' to show balance");

		switch(sentinel) {
			case 'D':
				int deposit;
				System.out.println("Enter amount to deposit");
					deposit = input.nextInt();
					balance = (sbalance + deposit);
				break;
			case 'W':
				System.out.println("Enter amount to withdraw');
					withdraw = input.nextInt();

				balance = (balance - withdraw);
					
				break; 
}
		
}
	
}
}
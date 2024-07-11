import java.util.Scanner;

public class BankApp {
	public static void main(String[] args) {	
		System.out.println("Welome friend: what is your name? ");
	
	Scanner input = new Scanner(System.in);

		String name;
		int balance = 0;
		String sentinel = new String();
	
	System.out.println("What is your name?");
		name = input.nextLine();
		
		while(!sentinel.equals("E")) {
			System.out.println("Enter 'D'deposit, 'W' to withdraw OR 'E' to show balance");
				sentinel = input.next();

		switch(sentinel) {
			case "D":
				int deposit;
				System.out.println("Enter amount to deposit");
					deposit = input.nextInt();
					balance = (balance + deposit);
				break;
			case "W":
				int withdraw;
				System.out.println("Enter amount to withdraw");
					withdraw = input.nextInt();
				if(balance == 0 || withdraw > balance) {
					System.out.println("you cannot withdraw");
}				else {
				balance = (balance - withdraw);
}	
				break; 
}
		
}
			if(balance == 0) {
				System.out.println("your balance is Zero");
}			else {
				System.out.printf("your current balance is %d%n", balance);
}
}
}
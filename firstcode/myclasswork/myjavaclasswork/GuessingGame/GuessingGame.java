import java.security.SecureRandom;
import java.util.Scanner;

public class GuessingGame {
	public static void main(String[] args) {
		System.out.println("WELCOME TO GUESS THE NUMBER GAME\n");

	Scanner input = new Scanner(System.in);
	
	SecureRandom secureRequest = new SecureRandom();
		int computer = 1 + secureRequest.nextInt(1000);

		String name;
	
		System.out.print("what is your name:  ");
			name = input.nextLine();
		System.out.printf("Welcome %s%n", name);
		
		
		String flag = new String(" ");
		Guess request = new Guess();
		
		int numberOfAttempt = 0;

		while(!flag.equals("no")) {
			int player = 0;
			while(player != computer) {

				System.out.print("Guess number between 1 and 1000 with the fewest guesses:  ");
						player = input.nextInt();
					String feedback = request.game(player, computer);

				System.out.println(feedback);

				if(player != computer) {
					numberOfAttempt = numberOfAttempt + 1;
				}
			
					
			}
		String feedback = request.getattempt(numberOfAttempt);
		System.out.println(feedback);
		
		System.out.printf("%s will you like to continue? : press yes or no %n", name);
			flag = input.next();
		}
			
}
}
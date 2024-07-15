import java.util.Scanner;
public class ExamResult {
	public static void main(String[] args) {
		System.out.println("welcome: lets check the results");
	
	Scanner input = new Scanner(System.in);
		
	int passes = 0;
	int failures = 0;
	
	int userInput = 0;
	
	while(userInput != -1) {
	
	System.out.println("enter result (1 for pass:  2 for failure: ");
		userInput = input.nextInt();
		if(userInput == 1) {
		passes = passes + 1;
		} else if(userInput == 2 ) {
		failures = failures + 1;
		}
}
		
	System.out.printf("the number of passes is %d and the number of failure is %d%n", passes, failures);	
}
}
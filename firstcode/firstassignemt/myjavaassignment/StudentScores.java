import java.util.Scanner;

public class StudentScores {
	public static void main(String[] args) {
		System.out.println("Welcome to student scores evaluator");
	
	Scanner input = new Scanner(System.in);
	
	int scores = 0;
	int counter = 1;
	int pass = 0;
	int fail = 0;

	while(counter <= 15) {
		System.out.print("Enter a score:  ");
			scores = input.nextInt();
		if(scores >= 45) {
			pass = pass + 1;
		} else if(scores < 45) {
			fail = fail + 1;
		}
	   counter =  counter + 1;	
	}
	System.out.printf("%d student passed the exam and %d students failed the exam %n", pass, fail);
}
}
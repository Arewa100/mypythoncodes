import java.util.Scanner;

public class MultiplicationTable {
	public static void main(String[] args) {
		System.out.println("welcome to the multiplication table");
	
	Scanner input = new Scanner(System.in);

	int number;
	System.out.print("Enter a number to display its multiplication table:  ");
		number = input.nextInt();
	
	for(int counter = 1; counter <= 10; counter++) {
		int result = number * counter;
		System.out.printf("%d  x  %d = %d %n", number, counter , result);
	}
}
}
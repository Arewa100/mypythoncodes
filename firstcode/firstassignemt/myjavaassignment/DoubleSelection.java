import java.util.Scanner;

public class DoubleSelection {
	public static void main(String[] args) {
		System.out.println("Welcome friend.");
	
	Scanner input = new Scanner(System.in);
	
	System.out.println("Enter your age");
		int age = input.nextInt();
	if(age >= 20) {
		System.out.println("you are eligible to apply");
	} else {
		System.out.println("you are not eligible to apply");
}
}
}

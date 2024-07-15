import java.util.Scanner;

public class Palindrome {
	public static void main(String[] args) {
		System.out.println("Welcome to the Palindrome guy");
	
	Scanner input = new Scanner(System.in);

	int number = 0;
	for(int counter = 1; counter <= 10; counter++) {
		System.out.print("Enter a number to check if it is palindrome:  ");
			number = input.nextInt();

		boolean result = palindrome(number);
		if(result == true) {
			System.out.println("the number is palindrome");	
		} else {
			System.out.println("the number is not palindrome");
		}

}
}	
public static boolean palindrome(int number) {
	int firstDivision;
	int secondDivision;
	int thirdDivision;
	int fourthDivision;
	int firstNumber;
	int secondNumber;
	int thirdNumber;
	int fourthNumber;
	int fifthNumber;
	
	
	firstDivision = (number / 10);

	fifthNumber = (number % 10);

	fourthNumber = (firstDivision % 10); 

	secondDivision = (firstDivision / 10);
	thirdNumber = (secondDivision % 10);

	thirdDivision = (secondDivision / 10);
	secondNumber = (thirdDivision % 10);

	fourthDivision = (thirdDivision / 10);
	firstNumber = (fourthDivision);
	
	return (firstNumber == fifthNumber && secondNumber == fourthNumber ? true : false);
}
}
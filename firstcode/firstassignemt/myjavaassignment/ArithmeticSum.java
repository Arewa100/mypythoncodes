import java.util.Scanner;
public class ArithmeticSum {
	public static void main(String[] args) {
		System.out.println("Welcome friend, this a program to print arithmetic sum ,average, product, smallest, largest of three inputs");

	Scanner input = new Scanner(System.in);
	

	int firstNumber;
	int secondNumber;
	int thirdNumber;
	int fourthNumber;
	
	System.out.println("Enter the first number");
		firstNumber = input.nextInt();
	System.out.println("Enter the second number");
		secondNumber = input.nextInt();
	System.out.println("Enter the third number");
		thirdNumber = input.nextInt();
	System.out.println("Enter the fourth number");
		fourthNumber = input.nextInt();
	
	int[] arithmetic = calculator(firstNumber, secondNumber, thirdNumber, fourthNumber);
	
	System.out.printf("the sum is %d%n", arithmetic[0]);
	System.out.printf("the average is %d%n", arithmetic[1]);
	System.out.printf("the product is %d%n", arithmetic[2]);
	System.out.printf("the smallest is %d%n", arithmetic[3]);
	System.out.printf("the largest is %d%n", arithmetic[4]);
}



public static int[] calculator(int numberone, int numbertwo, int numberthree, int numberfour) {

	int sum = (numberone + numbertwo + numberthree + numberfour);
	int average = (sum / 3);
	int product = (numberone * numbertwo * numberthree * numberfour);
	int smallest = Math.min(numberone, Math.min(numbertwo, Math.min(numberthree, numberfour)));
	int largest = Math.max(numberone, Math.max(numbertwo, Math.max(numberthree, numberfour)));
	
	int[] resultList = {sum, average, product, smallest, largest};	
	return  resultList;
} 
}
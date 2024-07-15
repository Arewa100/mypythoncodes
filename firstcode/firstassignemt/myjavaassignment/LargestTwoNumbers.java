import java.util.Scanner;
public class LargestTwoNumbers {
	public static void main(String[] args) {
		System.out.println("Welcome friend");
	
	Scanner input =  new Scanner(System.in);
	int firstLargest = 0;
	int secondLargest = 0;
	int number = 0;
	int counter = 1;
	
	while(counter <= 10) {
		System.out.print("enter a number");
			number = input.nextInt();
		if(firstLargest < number) {
			firstLargest = number;
		}		
		else if(firstLargest > secondNumber) {
			secondLargest = number;
		}
	counter = counter + 1;
}
	System.out.println(firstLargest);
	System.out.println(secondLargest);
}
}
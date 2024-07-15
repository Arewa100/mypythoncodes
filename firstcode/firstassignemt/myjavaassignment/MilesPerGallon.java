import java.util.Scanner;

public class MilesPerGallon {
	public static void main(String[] args) {
		System.out.println("Welcome friend, today is goin to be a very good day");
	
	Scanner input = new Scanner(System.in);
		
	int gallon = 0;
	int miles = 0;
	double total =0;
	int counter = 0;
	double result= 0;

	
	while(gallon != -1) {
		System.out.print("Enter the number of gallon used: ");
		gallon = input.nextInt();
		System.out.print("Enter the number of miles: ");
			miles = input.nextInt();
		if(gallon != -1) {
		result = (miles/ gallon);
		total = total + result;
		counter = counter + 1;
		
		System.out.printf("the miles/gallon for this tank was %f%n", result);

}
		
}
	double average;
	average = (total / counter);
	System.out.printf("The overall average miles/gallon was %f", average);
	
}
}
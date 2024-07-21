import java.util.Scanner;

public class DivideOrSquare {
	public static void main(String[] args) {
		System.out.println("Welcome friend, it is a good day");
		
	Scanner input = new Scanner(System.in);
		
	System.out.print("Enter a number:  ");
	double number = input.nextDouble();
	
	CommonTools tools = new CommonTools();
	
	double result = tools. divideorsquare(number)
	
	System.out.printf("&f ", result);

}
}
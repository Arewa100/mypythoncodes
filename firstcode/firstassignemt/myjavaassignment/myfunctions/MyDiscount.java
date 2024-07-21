import java.util.Scanner;

public class MyDiscount {
	public static void main(String[] args) {	
		System.out.println("Welcome friend, today is just so beautiful\n");
	
	Scanner input =  new Scanner(System.in);
		int price;
		int percentageDiscounts;
	System.out.println("HILLARY SUPERSTORE & Co.\n");
	System.out.print("Enter the price: ");
		price = input.nextInt();
	System.out.print("Enter the percentage discount: ");
		percentageDiscounts = input.nextInt();

	CommonTools tools = new CommonTools();

	double discount = tools.mydiscount(price, percentageDiscounts);
		
	System.out.printf("Your discount price is %.2f%n", discount);
		
		
}
}
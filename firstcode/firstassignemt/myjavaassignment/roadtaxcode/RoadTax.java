import java.util.Scanner;
	
public class RoadTax {
	public static void main(String[] args) {
		System.out.println("Welcome friend, today must be a very good day\n");
	
	Scanner input = new Scanner(System.in);
	
	
	String flag = new String(" ");
	
	while(!flag.equals("no")) {

		String carname;
		System.out.print("What is you car name:  ");
			carname = input.next();


		TaxCalculator tax = new TaxCalculator();
		double carcost;

		System.out.println("Enter the cost of your car\n");
			carcost = input.nextDouble();

		double AmountPaidOnRoadTax = tax.roadtax(carcost);
		
		System.out.printf("the road tax to be paid based on your %s car price is %.2f %n", carname, AmountPaidOnRoadTax);
	
		System.out.println("press yes to continue or no to end");
			flag = input.next();
	}
}
}
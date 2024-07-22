import java.util.Scanner;

public class PersonalIncomeTax {
	public static void main(String[] args) {
		System.out.println("Welcome Friend: how can i help you?");
		
	Scanner input = new Scanner(System.in);
		
	String name;
	System.out.println("What is your name");
	name = input.nextLine();
	
	System.out.println("welcome " + name);
	
	String flag = new String();
	
	while(!flag.equals("no")) {
		double taxableincome;
		double feedback;
		IncomeTax tax = new IncomeTax();
		String message = """
			1: press 0 to calculate tax for single filer
			2: press 1 for married filing jointly
			3: prees 2 for married filling seperately
			4: press 3 for head of house
			""";
		System.out.println(message);
		System.out.print("Select category:  ");
		int category = input.nextInt();
	
	switch(category) {
		case 0:
			System.out.println("welcome to taxable income calculator for single filers\n");
			
			System.out.print("Enter a taxable income:  ");
			taxableincome = input.nextDouble();
			feedback = tax.singlefiler(taxableincome);
			System.out.printf("Your tax is %.2f%n", feedback);

			break;
		case 1:
			System.out.println("welcome to taxable income calculator for single filers\n");
			
			System.out.print("Enter a taxable income:  ");
			taxableincome = input.nextDouble();
			feedback = tax.marriedfillingjointly(taxableincome);
			System.out.printf("Your tax is %.2f%n", feedback);
			break;
		case 2: 
			System.out.println("welcome to taxable income calculator for single filers\n");
			
			System.out.print("Enter a taxable income:  ");
			taxableincome = input.nextDouble();
			feedback = tax.marriedfillingseperately(taxableincome);
			System.out.printf("Your tax is %.2f%n", feedback);
			break;
		case 3: 
			System.out.println("welcome to taxable income calculator for single filers\n");
			
			System.out.print("Enter a taxable income:  ");
			taxableincome = input.nextDouble();
			feedback = tax.headofhousehold(taxableincome);
			System.out.printf("Your tax is %.2f%n", feedback);
			break;
		default:
			System.out.println("invalid entry....");
	}


	System.out.println("press 'yes' to continue or 'no' to end");
		flag = input.next();
	}

}
}
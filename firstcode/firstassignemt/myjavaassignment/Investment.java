import java.util.Scanner;
public class Investment {
	public static void main(String[] args) {
	
	Scanner input = new Scanner(System.in);

	int amount;

	System.out.println("Enter the amount on investment");
		amount = input.nextInt();

	for(int counter = 1; counter <= 31; counter++) {
		double result = investment(amount, counter);
		System.out.printf("the amount on investment is %.2f after %d year %n", result, counter);
	}
}

public static double investment(int amount, int years) {
	int annualrate = 7;
	int rate_sum = (1 + annualrate);
	double rate_exponent_to_years = Math.pow(rate_sum, years);
	
	double amount_on_deposit_each_year = (amount * rate_exponent_to_years);
	
	return amount_on_deposit_each_year;
}
}
public class IncomeTax {

	public double singlefiler(double taxableincome) {
		double rate;
		double first_rate;
		double tax_on_first_rate;
		double tax;
		double feedback;
		double result;

		if (taxableincome <= 8350) {
		rate = (10.0/100);
		tax = (taxableincome * rate);
		
		return tax;

	} else if (taxableincome >= 8351 && taxableincome <= 33950) {
		rate = (15.0/100);
		first_rate = (10.0/100);
		tax_on_first_rate = (8350 *first_rate);
		result = (taxableincome - 8350);
		feedback = (result * rate);
		tax = (tax_on_first_rate + feedback);
		
		return tax;

	} else if (taxableincome >= 33951 && taxableincome <= 82250) {
		rate = (25.0/100);
		first_rate = (10.0/100);
		tax_on_first_rate = (8350 *first_rate);
		result = (taxableincome - 8350);
		feedback = (result * rate);
		tax = (tax_on_first_rate + feedback);
		
		return tax;

	} else if (taxableincome >= 82251 && taxableincome <= 171550) {
		rate = (28.0/100);
		first_rate = (10.0/100);
		tax_on_first_rate = (8350 *first_rate);
		result = (taxableincome - 8350);
		feedback = (result * rate);
		tax = (tax_on_first_rate + feedback);
		
		return tax;

	} else  if (taxableincome >= 171551 && taxableincome <= 372950) {
		rate = (33.0/100);
		first_rate = (10.0/100);
		tax_on_first_rate = (8350 *first_rate);
		result = (taxableincome - 8350);
		feedback = (result * rate);
		tax = (tax_on_first_rate + feedback);
		
		return tax;
	
	} else {
		rate = (35.0/100);
		first_rate = (10/100);
		tax_on_first_rate = (8350 *first_rate);
		result = (taxableincome - 8350);
		feedback = (result * rate);
		tax = (tax_on_first_rate + feedback);
		
		return tax;
	}
}
	public double marriedfillingjointly(double taxableincome) {
		double rate;
		double first_rate;
		double tax_on_first_rate;
		double tax;
		double feedback;
		double result;

		if (taxableincome <= 16700) {
		rate = (10.0/100);
		tax = (taxableincome * rate);
		
		return tax;

	} else if (taxableincome >= 16701 && taxableincome <= 67900) {
		rate = (15.0/100);
		first_rate = (10.0/100);
		tax_on_first_rate = (8350 *first_rate);
		result = (taxableincome - 8350);
		feedback = (result * rate);
		tax = (tax_on_first_rate + feedback);
		
		return tax;

	} else if (taxableincome >= 67901 && taxableincome <= 137050) {
		rate = (25.0/100);
		first_rate = (10.0/100);
		tax_on_first_rate = (8350 *first_rate);
		result = (taxableincome - 8350);
		feedback = (result * rate);
		tax = (tax_on_first_rate + feedback);
		
		return tax;

	} else if (taxableincome >= 137051 && taxableincome <= 208850) {
		rate = (28.0/100);
		first_rate = (10.0/100);
		tax_on_first_rate = (8350 * first_rate);
		result = (taxableincome - 8350);
		feedback = (result * rate);
		tax = (tax_on_first_rate + feedback);
		
		return tax;

	} else if (taxableincome >= 208851 && taxableincome <= 372950) {
		rate = (33.0/100);
		first_rate = (10.0/100);
		tax_on_first_rate = (8350 *first_rate);
		result = (taxableincome - 8350);
		feedback = (result * rate);
		tax = (tax_on_first_rate + feedback);
		
		return tax;
	
	} else {
		rate = (35.0/100);
		first_rate = (10.0/100);
		tax_on_first_rate = (8350 *first_rate);
		result = (taxableincome - 8350);
		feedback = (result * rate);
		tax = (tax_on_first_rate + feedback);
		
		return tax;
	}
}

}
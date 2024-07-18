public class TaxCalculator {
	
	public double gettax(double amount, double percentage) {
		double percentageCost = (percentage/100);
		double calculatedRoadTax = (amount * percentageCost);
		
		return calculatedRoadTax;
}
	public double roadtax(double carcost) {
		TaxCalculator tax = new TaxCalculator();
		double carRoadTax;
		if(carcost < 1000000) {
			carRoadTax = tax.gettax(carcost, 10);
			
			return carRoadTax;
		}else if(carcost < 3000000) {
			carRoadTax = tax.gettax(carcost, 15);
			
			return carRoadTax;

		}else if(carcost < 5000000) {
			carRoadTax = tax.gettax(carcost, 20);
			
			return carRoadTax;

		}else {
			carRoadTax = tax.gettax(carcost, 25);
			
			return carRoadTax;

		}
}
}
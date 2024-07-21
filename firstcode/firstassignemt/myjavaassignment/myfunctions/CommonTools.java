public class CommonTools {

	public double divideorsquare(double number) {
		
		if(number % 5 == 0) {
		return Math.sqrt(number);
		}
		else {
		return (number % 5);
		}

}
	public double mydiscount(double price, double discount) {
		double percentage = (discount / 100);
		double percentageOfPrice = (price * percentage);
		
		double discountPrice = (price - percentageOfPrice);
		
		return discountPrice;
}
	public boolean equalstring(String firstString, String SecondString) {
		
		return (firstString == SecondString) ? true : false;
}
}
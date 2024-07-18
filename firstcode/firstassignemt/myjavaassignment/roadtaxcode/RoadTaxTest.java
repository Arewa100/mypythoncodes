import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class RoadTaxTest {
	
	@Test
	public void testingIfTaxCalculatorWorksFine() {
		TaxCalculator tax = new TaxCalculator();
		
		double result = tax.gettax(1000000, 10);
		
		assertEquals(100000, result);
}
	@Test
	public void testingIfTaxCalculatorCanTestForRoadTaxLesserThanAMillion() {
		TaxCalculator cartax = new TaxCalculator();
		
		double result = cartax.roadtax(100000);
		
		assertEquals(10000, result);
}	@Test
	public void testingIfTaxCalculatorCanTestForRoadTaxLesserThanthreeMillion() {
		TaxCalculator cartax = new TaxCalculator();
		
		double result = cartax.roadtax(2000000);
		
		assertEquals(300000, result);
}
	@Test
	public void testingIfTaxCalculatorCanTestForRoadTaxLesserFiveAMillion() {
		TaxCalculator cartax = new TaxCalculator();
		
		double result = cartax.roadtax(4000000);
		
		assertEquals(800000, result);
}
	@Test
	public void testingIfTaxCalculatorCanTestForRoadTaxGreaterThanFiveMillion() {
		TaxCalculator cartax = new TaxCalculator();
		
		double result = cartax.roadtax(6000000);
		
		assertEquals(1_500000, result);
}

}
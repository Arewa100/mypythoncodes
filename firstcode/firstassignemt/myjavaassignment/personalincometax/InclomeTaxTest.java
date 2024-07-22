import org.junit.jupiter.api.Test;
import stattic org.junit.jupiter.api.Assertions.assertEquals;

public class IncomeTaxTest {
	
	@Test
	public void testingIfSingleFilerFunctionIsWorkingProperlyForIncomesLessThanTheFirstInstance() {
		IncomeTax tax = new IncomeTax();
		
		double result = tax.singlefiler(8350);
		
		assertEquals(1082.50, result);
}	
}
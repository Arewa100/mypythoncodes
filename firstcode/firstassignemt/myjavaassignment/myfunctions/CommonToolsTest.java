import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class CommonToolsTest {
	
	@Test 
	public void testingIfDivideORSquareFunctionWorksProperlyForNumberThatIsDIvisibleByFive() {
		CommonTools tools = new CommonTools();

		double result = tools.divideorsquare(10);
			
		assertEquals(3.1622776601683795, result);
}
	@Test
	public void testingIfDivideORSquareFunctionWorksProperlyForNumberThatIsNotDIvisibleByFive() {
		CommonTools tools = new CommonTools();

		double result = tools.divideorsquare(12);
			
		assertEquals(2.0, result);
}
	@Test
	public void testingIfMyDiscountFunctionIsAbleToCalculateDiscountProperly() {
		CommonTools tools = new CommonTools();
	
		double result = tools.mydiscount(150, 15);
		
		assertEquals(127.5, result);
}
	@Test
	public void testingIfFunctionEqualsStringReturnsTrueIfItsStringArgumentAreEqual() {
		CommonTools tools = new CommonTools();
		
		Boolean result = tools.equalstring("shola", "shola");
		
		assertEquals(true, result);
}
}
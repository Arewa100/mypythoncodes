import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class IncomeTaxTest {
	
	@Test
	public void testingIfSingleFilerFunctionIsWorkingProperlyForIncomesLessThanTheFirstInstance() {
		IncomeTax tax = new IncomeTax();
		
		double result = tax.singlefiler(8350);
		
		assertEquals(835.0, result);
}	
		@Test
	public void testingIfSingleFilerFunctionIsWorkingProperlyForIncomesForTheSecondInstance() {
		IncomeTax tax = new IncomeTax();
		
		double result = tax.singlefiler(10000);
		
		assertEquals(1082.5, result);
}
			@Test
	public void testingIfSingleFilerFunctionIsWorkingProperlyForIncomesForTheThirdInstance() {
		IncomeTax tax = new IncomeTax();
		
		double result = tax.singlefiler(33951);
		
		assertEquals(7235.25, result);
}
			@Test
	public void testingIfSingleFilerFunctionIsWorkingProperlyForIncomesForTheFourthInstance() {
		IncomeTax tax = new IncomeTax();
		
		double result = tax.singlefiler(82251);
		
		assertEquals(21527.280000000002, result);
}
			@Test
	public void testingIfSingleFilerFunctionIsWorkingProperlyForIncomesForTheFifthInstance() {
		IncomeTax tax = new IncomeTax();
		
		double result = tax.singlefiler(171551);
		
		assertEquals(54691.33, result);
}
			@Test
	public void testingIfSingleFilerFunctionIsWorkingProperlyForIncomesForTheSixthInstance() {
		IncomeTax tax = new IncomeTax();
		
		double result = tax.singlefiler(400000);
		
		assertEquals(137077.5, result);
}



	@Test
	public void testingIfmarriedfillingjointlyFunctionIsWorkingProperlyForIncomesLessThanTheFirstInstance() {
		IncomeTax tax = new IncomeTax();
		
		double result = tax.marriedfillingjointly(8350);
		
		assertEquals(835.0, result);
}	
	@Test
	public void testingIfmarriedfillingjointlyIsWorkingProperlyForIncomesForTheSecondInstance() {
		IncomeTax tax = new IncomeTax();
		
		double result = tax.marriedfillingjointly(16701);
		
		assertEquals(2087.6499999999996, result);
}
	@Test
	public void testingIfmarriedfillingjointlyIsWorkingProperlyForIncomesForTheThirdInstance() {
		IncomeTax tax = new IncomeTax();
		
		double result = tax.marriedfillingjointly(67901);
		
		assertEquals(15722.75, result);
}
	@Test
	public void testingIfmarriedfillingjointlyProperlyForIncomesForTheFourthInstance() {
		IncomeTax tax = new IncomeTax();
		
		double result = tax.marriedfillingjointly(137051);
		
		assertEquals(36871.280000000006, result);
}
	@Test
	public void testingIfmarriedfillingjointlyIsWorkingProperlyForIncomesForTheFifthInstance() {
		IncomeTax tax = new IncomeTax();
		
		double result = tax.marriedfillingjointly(208851);
		
		assertEquals(67000.33, result);
}
	@Test
	public void testingIfmarriedfillingjointlyIsWorkingProperlyForIncomesForTheSixthInstance() {
		IncomeTax tax = new IncomeTax();
		
		double result = tax.marriedfillingjointly(400000);
		
		assertEquals(137912.5, result);
}

	

	@Test
	public void testingIfmarriedfillingseperatelyFunctionIsWorkingProperlyForIncomesLessThanTheFirstInstance() {
		IncomeTax tax = new IncomeTax();
		
		double result = tax.marriedfillingseperately(8350);
		
		assertEquals(835.0, result);
}	
	@Test
	public void testingIfmarriedfillingseperatelyIsWorkingProperlyForIncomesForTheSecondInstance() {
		IncomeTax tax = new IncomeTax();
		
		double result = tax.marriedfillingseperately(8351);
		
		assertEquals(835.15, result);
}
	@Test
	public void testingIfmarriedfillingseperatelyIsWorkingProperlyForIncomesForTheThirdInstance() {
		IncomeTax tax = new IncomeTax();
		
		double result = tax.marriedfillingseperately(33951);
		
		assertEquals(7235.25, result);
}
	@Test
	public void testingIfmarriedfillingseperatelyProperlyForIncomesForTheFourthInstance() {
		IncomeTax tax = new IncomeTax();
		
		double result = tax.marriedfillingseperately(68525);
		
		assertEquals(15878.75, result);
}
	@Test
	public void testingIfmarriedfillingseperatelyIsWorkingProperlyForIncomesForTheFifthInstance() {
		IncomeTax tax = new IncomeTax();
		
		double result = tax.marriedfillingseperately(104426);
		
		assertEquals(32540.08, result);
}
	@Test
	public void testingIfmarriedfillingseperatelyIsWorkingProperlyForIncomesForTheSixthInstance() {
		IncomeTax tax = new IncomeTax();
		
		double result = tax.marriedfillingseperately(400000);
		
		assertEquals(137912.5, result);
}


	@Test
	public void testingIfheadofhouseholdFunctionIsWorkingProperlyForIncomesLessThanTheFirstInstance() {
		IncomeTax tax = new IncomeTax();
		
		double result = tax.headofhousehold(11950);
		
		assertEquals(1195.0, result);
}	
	@Test
	public void testingIfheadofhouseholdFunctionIsWorkingProperlyForIncomesForTheSecondInstance() {
		IncomeTax tax = new IncomeTax();
		
		double result = tax.headofhousehold(11951);
		
		assertEquals(1375.15, result);
}
	@Test
	public void testingIfheadofhouseholdFunctionIsWorkingProperlyForIncomesForTheThirdInstance() {
		IncomeTax tax = new IncomeTax();
		
		double result = tax.headofhousehold(45501);
		
		assertEquals(10122.75, result);
}
	@Test
	public void testingIfheadofhouseholdFunctionIsProperlyForIncomesForTheFourthInstance() {
		IncomeTax tax = new IncomeTax();
		
		double result = tax.headofhousehold(117451);
		
		assertEquals(31383.280000000002, result);
}
	@Test
	public void testingIfheadofhouseholdFunctionIsWorkingProperlyForIncomesForTheFifthInstance() {
		IncomeTax tax = new IncomeTax();
		
		double result = tax.headofhousehold(190201);
		
		assertEquals(60845.83, result);
}
	@Test
	public void testingIfheadofhouseholdFunctionIsIsWorkingProperlyForIncomesForTheSixthInstance() {
		IncomeTax tax = new IncomeTax();
		
		double result = tax.headofhousehold(400000);
		
		assertEquals(137912.5, result);
}

}
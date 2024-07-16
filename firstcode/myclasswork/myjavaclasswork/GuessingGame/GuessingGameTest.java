import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class GuessingGameTest {
	
	@Test
	public void testingIfGameWorksWellForConditionWhenPlayerValueIsGreaterThanComputer() {
		Guess request = new Guess();
		
		String result = request.game(100, 20);
		
		assertEquals("too high, try again", result);
}
	@Test
	public void testingIfGameWorksWellForConditionWhenPlayerValueIsLesserThanComputer() {
		Guess request = new Guess();
		
		String result = request.game(20, 100);
		
		assertEquals("too low, try again", result);
}
	@Test
	public void testingIfGameWorksWellForConditionWhenPlayerValueIsEqualToComputer() {
		Guess request = new Guess();
		
		String result = request.game(20, 20);
		
		assertEquals("Congratulation", result);
}
	@Test 
	public void testingIfTheNumberOfAttemptIsLowerThanTen() {
		Guess request = new Guess();

		String result = request.getattempt(5);
		
		assertEquals("you are good", result);
}
	@Test 
	public void testingIfTheNumberOfAttemptIsGreaterThanTen() {
		Guess request = new Guess();

		String result = request.getattempt(12);
		
		assertEquals("you can be better", result);
}

}
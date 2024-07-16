import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class GuessingGameTest {
	
	@Test
	public testingIfGameWorksWellForConditionWhenPlayerValueIsGreaterThanComputer() {
		Guess request = new Guess();
		
		String result = request.game(100, 20);
		
		assertEquals("too high, try again", result);
}
	
}
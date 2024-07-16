public class Guess {
	
	public String game(int player, int computer) {

		if(player > computer) {
			String message = "too high, try again";
			return message;

		} else if(player == computer) {
			String message = "Congratulation";
			return message;
		} else  {
			String message = "too low, try again";
			return message;
		}
	
}
	public String getattempt(int attempt) {
		if(attempt < 10) {
			String message = "you are good";
		return message;
		} else {
			String message = "you can be better";
		return message;
		}
}
	
}
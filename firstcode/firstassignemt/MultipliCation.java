public class MultipliCation { 
		
	public int multiply(int firstNumber, int secondNumber) {
		int product1 = 0;
		int product2 = 0;
		
		if(firstNumber < secondNumber) {
			int counter = 1;
			while(counter < secondNumber) {
				product1 = product1 + firstNumber;	
			
				counter = counter + 1;
}
		return product1;
		
}	else  {
		int counter = 1;
		
		while(counter < firstNumber) {
			product2 = product2 + secondNumber;
}
		return product2;
}
	
}
}
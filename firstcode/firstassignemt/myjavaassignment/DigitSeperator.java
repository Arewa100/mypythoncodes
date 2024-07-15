import java.util.Scanner;
	
public class DigitSeperator {
	public static void main(String[] miracle) {
		System.out.println("welcome to my digit seperator");
	
	Scanner input = new Scanner(System.in);
		int number;
	System.out.println("Enter a number");
		number = input.nextInt();
		
	int[] result = digitseperator(number);
	System.out.println(result[0]);
	System.out.println(result[1]);
	System.out.println(result[2]);
	System.out.println(result[3]);
	System.out.println(result[4]);
	
	
		
	
	
}
	public static int[] digitseperator(int number) {
		
		int firstIndex;
		int secondIndex;
		int thirdIndex;
		int fourthIndex;
		int firstDivision;
		int secondDivision;
		int thirdDivision;
		int fourthDivision;
		int fifthIndex;

		firstDivision = (number / 10);  
		firstIndex = (number % 10); 

		secondDivision = (firstDivision / 10); 
		secondIndex = (firstDivision % 10);  

		thirdDivision = (secondDivision / 10); 
		thirdIndex = (secondDivision % 10); 

		fourthDivision = (thirdDivision / 10); 
		fourthIndex = (thirdDivision % 10); 
		
		fifthIndex = fourthDivision;
	
	int[] result = {fifthIndex, fourthIndex, thirdIndex, secondIndex, firstIndex};
	
		return result;
		
}
}
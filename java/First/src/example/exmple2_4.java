package example;
import java.util.Scanner;
public class exmple2_4 {

	public static void main(String[] args) {
		// 
		Scanner read = new Scanner(System.in);
				
		System.out.println("숫자를 입력하세요");
		float number = read.nextInt();
		
		if (number > 0.0) {
			System.out.println("이 숫자는 양수 입니다.");
		}else if(number < 0.0) {
			System.out.println("이 숫자는 음수 입니다.");
		}else {
			System.out.println("이 숫자는 0입니다");
		}
		
		System.out.println("3****************");
		
		
		char Eng = 'a';
		
	
		if( ( Eng >= 'a' && Eng <= 'z') || (Eng >= 'A' && Eng <= 'Z')){
			System.out.println( Eng + "\n이 글자는 알파벳입니다.");
		}else {
			System.out.println( Eng + "\n이 글자는 알파벳이 아닙니다");
		}
		
		System.out.println("4******************");
		System.out.println("숫자를 입력하세요");
		int num = read.nextInt();
		int sum = 0;
		
		
		
		
		for (int i = 1; i <= num; ++i) {
			sum += i ;
		}
		System.out.println("1부터 " + num + "까지의 합은" + sum + "입니다");
		}
	}



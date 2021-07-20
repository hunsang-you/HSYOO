package example;
import java.util.Scanner;
public class example8 {

	public static void main(String[] args) {
		// for, if를 이용한 최대공약수
		Scanner read = new Scanner(System.in);
		System.out.println("최대공약수를 구할 두 수를 입력하세요");
		
		int num1 = read.nextInt();
		int num2 = read.nextInt();
		
		int gcd = 1;
		
		for (int i = 1 ; i <= num1 && i <= num2 ; ++i) {
			if (num1 % i == 0 && num2 % i ==0) {
				gcd = i;
				
			}
			
		}
		System.out.println(num1 + ", " + num2 + "의 최대공약수는" + gcd + "입니다.");
		
		System.out.println("8-2*************");
		//while, if를 이용한 최대공약수
		System.out.println("최대공약수를 구할 두 수를 입력하세요");
		int n1 = read.nextInt();
		int n2 = read.nextInt();
		
		int GCD = 1;
		
		while(n1 != n2) {
			if (n1 >n2) {
				n1 -= n2;
			}
			else {
				n2 -= n1;
				}
		}
		System.out.println("최대공약수 : " + n1);
		
		
	}

}

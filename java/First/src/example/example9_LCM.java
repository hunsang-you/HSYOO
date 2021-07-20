package example;
import java.util.Scanner;
public class example9_LCM {

	public static void main(String[] args) {
		//최소공배수 구하기
		Scanner read = new Scanner(System.in);
		
		System.out.println("최소공배수를 구할 숫자 두개를 입력하세요");
		
		//숫자 두개를 입력하는 변수
		int n1 = read.nextInt();
		int n2 = read.nextInt();
		
		//두 수중 더 큰 숫자를 저장하는 변수
		int mul = (n1 > n2) ? n1 : n2;
		
		// 항상 True 일때
		
		while(true) {
			if( mul % n1 == 0 && mul % n2 ==0) {
				System.out.printf("두 숫자의 최소공배수는 " + mul + " 입니다");
				break;
			}
			++mul;
		}
	System.out.println();	
	System.out.println("9-1***********");
	System.out.println();	

	//최대공약수를 이용한 최소공배수 계산
	
	System.out.println("숫자 두개를입력하세요");
	int m1 = read.nextInt();
	int m2 = read.nextInt();
	int gcd = 1;
	for (int i = 1; i <= m1 && i <= m2; ++i) {
		if (n1 % i ==0 && n2 % i ==0)
			gcd = i;
		}
	int lcm = (m1 * m2) / gcd;
	System.out.printf("최소 공배수는 %d", lcm);
	
	
	
	}//out of main

}//out of Class

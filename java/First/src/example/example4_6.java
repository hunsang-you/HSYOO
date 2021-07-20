package example;
import java.util.Scanner;
public class example4_6 {

	public static void main(String[] args) {
		//while을 이용한 sum 구하기 
		System.out.println("숫자를 입력하세요");
		
		Scanner read = new Scanner(System.in);
		
		int i = 1;
		int sum = 0;
		int num = read.nextInt();
		
		while (i <= num) {
			sum+=i;
			i++;
		}
		System.out.println("1부터 " + num + " 까지의 합은 " + sum + "입니다.");
		
		System.out.println("5*************");
		//입력한 수까지의 팩토리얼값 구하기
		long factorial = 1;
		System.out.println("숫자를 입력하세요");
		int A = read.nextInt();
		for (int j =1 ; j <= A; ++j) {
			factorial = factorial * j;
		}
		System.out.println("입력한 " + A + "의 팩토리얼 값은 " + factorial + " 입니다.");
		
		
		System.out.println("6*************");
		//구구단(B * 10까지)
		
		System.out.println("숫자를 입력");
		
		int B = read.nextInt();
		
		for(int k = 1; k <= 10; ++k) {
			System.out.printf("%d * %d = %d \n", B, k, B * k);
		}
		
		System.out.println("6-2 ********");
		//입력한 수(C * C)까지의 구구단
		System.out.println("숫자를 입력하세요");
		int C = read.nextInt();
		
		for(int m = 1; m <= C ; ++m) {
			System.out.printf("%d * %d = %d \n", C, m, C*m);
		}
		
	}

}

package example;
import java.util.Scanner;
public class example7 {

	public static void main(String[] args) {
		// 피보나치 수열
		
		int first = 0;
		int second = 1;
		int n = 10;
		System.out.println(first + "부터 시작하는 피보나치 수열은");
		for (int i = 1; i <= n ; ++i) {
			System.out.print(first + ".");
			int next = first + second;
			first = second;
			second = next;
		}
		System.out.print("......\n");
		
		System.out.println("7-2************");
		//for 구문을 이용한 피보나치 수열
		
		System.out.println("숫자를 입력하세요");
		Scanner read = new Scanner(System.in);
		
		int firstterm = read.nextInt();
		int secondterm = read.nextInt();
		int m = 10;
		System.out.println(firstterm + ", " + secondterm + "으로 시작하는 피보나치 수열은");
		
		for(int ii = 1; ii<=m; ++ii) {
			System.out.print(firstterm + ".");
			int nextterm = firstterm + secondterm;
			firstterm = secondterm;
			secondterm = nextterm;
		}
		System.out.println(".......");
		
		System.out.println("7-3************");
		//while을 이용한 피보나치 수열
		System.out.println("숫자 두개를 입력하세요");
		int l = 10;
		int iii = 1;
		int uno = read.nextInt();
		int dos = read.nextInt();
		
		System.out.println(uno + ", " + dos + "으로 시작하는 피보나치 수열은");
		
	
		while (iii <= l){
			
			System.out.print(uno + ".");
			
			int nextint = uno + dos;
			uno = dos;
			dos = nextint;
			
			iii++;
		}System.out.println(".....");
		
		
	}

}

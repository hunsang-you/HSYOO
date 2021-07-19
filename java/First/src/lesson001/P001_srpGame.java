package lesson001;
import java.util.Scanner;
public class P001_srpGame {
	
	public static void main(String[] args) {
		// Scissor = 1, Rock = 2 , Paper = 3;
		System.out.println("가위(1), 바위(2), 보(3) 중에 숫자를 입력하세요");
		
		Scanner input = new Scanner(System.in);
		int num = input.nextInt();
		
		int Com = (int) (Math.random() * 10 % 3 + 1);
		
		
		//Com이 가위(1)일때
		if(Com == 1 & num ==1) {
			System.out.println("무승부.");
		}else if (Com == 1 & num == 2) {
			System.out.println("당신이 이겼습니다.");
		}else if (Com == 1 & num == 3){
			System.out.println("당신이 졌습니다");
		}
		
		
		//Com이 바위(2)일때
		if(Com == 2 & num == 1) {
			System.out.println("당신이 졌습니다.");
		}else if (Com == 2 & num == 2) {
			System.out.println("무승부.");
		}else if (Com == 2 & num == 3){
			System.out.println("당신이 이겼습니다");
		}
		
		//Com이 보(3)일때
		if(Com == 3 & num == 1) {
			System.out.println("당신이 이겼습니다..");
		}else if (Com == 3 & num == 2) {
			System.out.println("당신이 졌습니다..");
		}else if (Com == 3 & num == 3){
			System.out.println("무승부");
		}
		if( num ==0 || 4<= num) {
			System.out.println("1,2,3 중에 하나를 입력해주세요");
		}
	System.out.println("컴퓨터는 " + Com + "을 냈습니다");	
		
		
	}
}

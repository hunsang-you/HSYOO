package lesson003;

public class SysteminText2 {

	public static void main(String[] args) {
		System.out.println("단어를 입력하고 엔터를 치세요. \nCtrl + Z = 종료");
		int i;
		try {
			while((i=System.in.read()) != -1) {
				System.out.print((char)i);
			}	
		} catch (Exception e) {
			System.out.println("입력처리에서 오류발생");
			e.printStackTrace();
		}
		System.out.println("프로그램 종료");
		
	}

}

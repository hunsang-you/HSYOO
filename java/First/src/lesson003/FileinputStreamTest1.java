package lesson003;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

public class FileinputStreamTest1 {

	public static void main(String[] args) {
		try {
			FileInputStream fis = new FileInputStream("C:/Users/user16/Desktop/input.txt");
			int i;
			while((i = fis.read()) != -1) {
				System.out.print((char)i);
			}
			System.out.println("읽기 완료");
		
		}catch(FileNotFoundException fe) {
			System.out.println("지정된 파일을 찾을 수 없습니다.");
			fe.printStackTrace();
		} catch (Exception e) {
			// TODO: handle exception
			System.out.println("파일 입출력 처리 오류");
			e.printStackTrace();
		}
		
		System.out.println("프로그램 정상종료..");

	}

}

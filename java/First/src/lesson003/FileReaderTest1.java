package lesson003;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class FileReaderTest1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {FileReader fr = new FileReader("C:/Users/user16/Desktop/input2.txt");
			int i;
			while((i = fr.read()) != -1) {
				System.out.print((char)i);
			
			}
			System.out.println("\n읽기완료");
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

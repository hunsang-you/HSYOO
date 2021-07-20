package lesson001;

public class E015_Array2D {

	public static void main(String[] args) {
		// declare array 배열 선언
		int [] array1d;
		int [][] array2d;
		
		array1d = new int[] {1,2,3}; // 선언된 배열에 값 초기화
		array2d = new int[][] {
								{1,2,3},
							   {4,5,6},
							   {7,8,9}
							   };
		
		// 개별 요소에의 접근은 index 사용
		System.out.println("1차원 배열 array1d의 값");
		for(int i = 0; i < array1d.length ; i++) {
			System.out.printf("%3d   ", array1d[i]);
		}
		System.out.println(); //줄바꿈용
		
		
		//2차원 배열 요소에 대한 접근
		// nested for loop 사용
		System.out.println("2차원 배열 array2d의 값");
		for(int row = 0; row < array2d.length; row++) {
			for(int col = 0; col < array2d[row].length ; col++) {
				//array2d[row][col]
				System.out.printf("%3d ", array2d[row][col]);
			}
			System.out.println();
		}//end of outer for loop
		
	}

}

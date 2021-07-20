package lesson001;

import java.util.Arrays;

public class E016_ArrayCopy {

	public static void main(String[] args) {
		 // 방법 1. shallow (얕은복사)
        int [] numbers = {1, 2, 3, 4, 5, 6};
        int [] positiveNumbers = numbers;    // copying arrays

        for (int number: positiveNumbers) {
            System.out.print(number + ", ");
        }
        	System.out.println();
            System.out.println("numbers : " + numbers);
            System.out.println("positiveNumbers : " + positiveNumbers);
            System.out.println();
            
            
            
         // 방법 2. deep copy : 깊은 복사
         int [] source = {1, 2, 3, 4, 5, 6};
         int [] destination = new int[6];

         // iterate and copy elements from source to destination
         for (int i = 0; i < source.length; ++i) {
             destination[i] = source[i];
         }
          
         System.out.println("source....(1)");
         System.out.println(source);
         System.out.println(Arrays.toString(source));
         System.out.println();
         System.out.println("destination...(1)");
         System.out.println(destination);
         System.out.println(Arrays.toString(destination));
         
         System.out.println();
         
         destination[0] = 1000;
         System.out.println("변경후 두 배열값비교");
         System.out.println("source....(2)");
         System.out.println(Arrays.toString(source));
         System.out.println();
         System.out.println("destination...(2)");

         System.out.println(Arrays.toString(destination));
         System.out.println();
         
         // 방법 3.  arraycopy() 사용
         int[] n1 = {2, 3, 12, 4, 12, -2}; //6
         int[] n3 = new int[5];			   //5

         // Creating n2 array of having length of n1 array
         int[] n2 = new int[n1.length];	   //6
       
         // copying entire n1 array to n2
         System.arraycopy(n1, 0, n2, 0, n1.length);
         				//n1의 0번을 , n2의 0번으로
         System.out.println("n2 = " + Arrays.toString(n2));  
       
         // copying elements from index 2 on n1 array
         // copying element to index 1 of n3 array
         // 2 elements will be copied
         System.arraycopy(n1, 2, n3, 1, 2);
         				//n1의 2번을, n3의 1번으로 2칸
         System.out.println("n3 = " + Arrays.toString(n3));
         
	}// end of main

}// end of class

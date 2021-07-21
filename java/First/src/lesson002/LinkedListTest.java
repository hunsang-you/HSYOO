package lesson002;

import java.util.LinkedList;

public class LinkedListTest {

	public static void main(String[] args) {
		// LinkedList의 이해와 활용
		LinkedList<String> myList = new LinkedList<String>();
		
		myList.add("A");
		myList.add("B");
		myList.add("C");
		
		System.out.println("==A,B,C 출력==");
		System.out.println(myList);
		
		System.out.println("==D 추가==");
		myList.add(1, "D");
		System.out.println(myList);;
		
		System.out.println("==0추가==");
		myList.addFirst("0");
		System.out.println(myList);
		
		System.out.println("==삭제==");
		System.out.println(myList.removeLast());
		System.out.println(myList);
		
	}

}

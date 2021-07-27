package example;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;

public class PSet {

	public static void main(String[] args) {
		Set<Integer> set1 = new HashSet<>();
		
		set1.add(2);
		set1.add(3);
		set1.add(4);
		set1.add(5);
		System.out.println("Set1 : " + set1);
		
		Set<Integer> set2 = new HashSet<>();
		
		set2.add(1);
		set2.add(4);
		set2.add(7);
		set2.add(8);
		System.out.println("Set2 : " + set2);
		
		set2.addAll(set1);
		System.out.println("Union is : " + set2);
		
		System.out.println("===========================");
		
		Set<Integer> number1 = new TreeSet<>();
		
		number1.add(2);
		number1.add(3);
		number1.add(1);
		number1.add(5);
		number1.add(-2);
		System.out.println("Set using TreeSet : " + number1);
		
		System.out.println("Accessing elements using iterator(): ");
		Iterator<Integer> iterate1 = number1.iterator();
		while(iterate1.hasNext()) {
			System.out.print(iterate1.next());
			System.out.print(", ");
		}
		
		System.out.println();
		System.out.println();
		System.out.println("Words TreeSet");
	
		
		Set<String> words = new TreeSet<>();
		
		words.add("C");
		words.add("D");
		words.add("A");
		words.add("B");
		System.out.println("Set Using TreeSet : " + words);
		System.out.println("Accessing elements using iterator(): ");
		Iterator<String> iterate2 = words.iterator();
		while(iterate2.hasNext()) {
			System.out.print(iterate2.next());
			System.out.print(". ");
		}
	System.out.println();
	System.out.println("===================");
	// insert Elements to HashSet
	
	HashSet<Integer> evenNumber = new HashSet<>();
	
	evenNumber.add(2);
	evenNumber.add(4);
	evenNumber.add(6);
	System.out.println("(even)HashSet : " + evenNumber);
	
	HashSet<Integer> num = new HashSet<>();
	num.addAll(evenNumber);
	num.add(10);
	num.add(8);
	System.out.println("New (even) HashSet : " + num);
	System.out.println();
	System.out.println();
//	boolean value1 = num.remove(8);
//	System.out.println("Is 8 removed? " + value1);
//	System.out.println(num);
//	
//	boolean value2 = num.removeAll(num);
//	System.out.println("Are all elements removed?" + value2);
//	System.out.println(num);
	
	System.out.println("추가 제거");
	Scanner read = new Scanner(System.in);
	System.out.println("추가할 숫자를 입력하세요");
	int A = read.nextInt();
	num.add(A);
	System.out.println("현재 " + A + "가 추가된 정렬은");
	System.out.println(num);
	System.out.println();

	
	
	System.out.println("삭제할 숫자를 입력하세요");
	int B = read.nextInt();
	num.remove(B);
	System.out.println("현재 " + B + "가 삭제된 정렬은");
	System.out.println(num);
	
	}
	
}

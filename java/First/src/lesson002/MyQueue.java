package lesson002;

import java.util.ArrayList;

class MyQueue {

	private ArrayList<String> arrayQueue = new ArrayList<String>();
	
	public String deQueue() {
		int len = arrayQueue.size();
		if(len == 0) {
			System.out.println("큐가 비었습니다");
			return null;
		}
		
		return(arrayQueue.remove(0));
	}
	
}

public class QueueTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		MyQueue queue = new MyQueue();
		
		queue.enQueue("A");
		queue.enQueue("B");
		queue.enQueue("C");
		
		System.out.println(queue.deQueue());
		System.out.println(queue.deQueue());
		System.out.println(queue.deQueue());
		

	}

}


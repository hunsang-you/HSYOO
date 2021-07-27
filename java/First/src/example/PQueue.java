package example;

import java.util.Queue;
import java.util.LinkedList;
import java.util.PriorityQueue;
class PQueue {

    public static void main(String[] args) {
        // Creating Queue using the LinkedList class
        Queue<Integer> numbers = new LinkedList<>();

        // offer elements to the Queue
        numbers.offer(1);
        numbers.offer(4);
        numbers.offer(2);
        numbers.offer(3);
        numbers.offer(5);
        System.out.println("Queue: " + numbers);

        // Access elements of the Queue
        int accessedNumber = numbers.peek();
        System.out.println("Accessed Element: " + accessedNumber);

       
        // Remove elements from the Queue
        int removedNumber = numbers.poll();
        System.out.println("Removed Element: " + removedNumber);

        System.out.println("Updated Queue: " + numbers);
        
        System.out.println("====");
        
        // Creating a priority queue
       
        PriorityQueue<Integer> numbers1 = new PriorityQueue<>();

        // Using the add() method
        numbers1.add(5);
        numbers1.add(3);
        numbers1.add(4);
        numbers1.add(6);
        numbers1.add(7);
        
        
        System.out.println("PriorityQueue: " + numbers1);

        // Using the offer() method
        numbers1.offer(1);
        System.out.println("Updated PriorityQueue: " + numbers1);
            }
        
        
        
    }

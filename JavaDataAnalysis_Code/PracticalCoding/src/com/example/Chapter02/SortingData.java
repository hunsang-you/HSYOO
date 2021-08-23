package com.example.Chapter02;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.TreeMap;

public class SortingData {
    public static void main(String[] args) {
        File file = new File("data/Countries2.dat");
        TreeMap<Integer,String> dataset = new TreeMap();
        try {
            Scanner input = new Scanner(file);
            while (input.hasNext()) {
                String x = input.next();
                int y = input.nextInt();
                dataset.put(y, x);
            }
            input.close();
        } catch (FileNotFoundException e) {
            System.out.println(e);
        }
        print(dataset); // 인구수는 오름차순
    }
    
    public static void print(TreeMap<Integer,String> map) {
        for (Integer key : map.keySet()) {
            System.out.printf("%,12d  %-16s%n", key, map.get(key));
        }
    }
}

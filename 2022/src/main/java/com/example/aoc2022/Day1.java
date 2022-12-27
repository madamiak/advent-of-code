package com.example.aoc2022;

import com.example.AocBase;

import java.util.Collections;
import java.util.List;
import java.util.PriorityQueue;

public class Day1 extends AocBase {

    public static void main(String[] args) {
        List<String> input = readInput(Day1.class);
        System.out.println(task1(input));
        System.out.println(task2(input));
    }

    private static int task1(List<String> input) {
        int max = 0;
        int currentSum = 0;
        for (String line : input) {
            if (line.equals("")) {
                currentSum = 0;
                continue;
            }
            int number = _int(line);
            currentSum += number;
            if (currentSum > max) {
                max = currentSum;
            }
        }
        return max;
    }

    private static int task2(List<String> input) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        int currentSum = 0;
        for (String line : input) {
            if (line.equals("")) {
                pq.add(currentSum);
                currentSum = 0;
                continue;
            }
            int number = _int(line);
            currentSum += number;
        }
        return pq.poll() + pq.poll() + pq.poll();
    }

}

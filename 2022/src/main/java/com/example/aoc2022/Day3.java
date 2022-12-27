package com.example.aoc2022;

import com.example.AocBase;

import java.util.*;

import static java.util.stream.Collectors.toSet;

public class Day3 extends AocBase {

    public static void main(String[] args) {
        List<String> input = readInput(Day3.class);
        System.out.println(task1(input));
        System.out.println(task2(input));
    }

    private static int task2(List<String> input) {
        int priorities = 0;
        for (int i = 0; i < input.size(); i += 3) {
            Set<Integer> line1 = input.get(i).chars().boxed().collect(toSet());
            Set<Integer> line2 = input.get(i + 1).chars().boxed().collect(toSet());
            Set<Integer> line3 = input.get(i + 2).chars().boxed().collect(toSet());
            Map<Integer, Integer> occs = new HashMap<>();
            line1.forEach(e -> occs.put(e, occs.getOrDefault(e, -1) + 1));
            line2.forEach(e -> occs.put(e, occs.getOrDefault(e, -1) + 1));
            line3.forEach(e -> occs.put(e, occs.getOrDefault(e, -1) + 1));
            int priority = occs.entrySet()
                    .stream()
                    .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
                    .map(Map.Entry::getKey)
                    .findFirst()
                    .orElse(0);
            priorities += priority - constant(priority);
        }
        return priorities;
    }

    private static int task1(List<String> input) {
        int priorities = 0;
        for (String line : input) {
            CharSequence seq1 = line.subSequence(0, line.length() / 2);
            CharSequence seq2 = line.subSequence(line.length() / 2, line.length());

            seq:
            for (int i = 0; i < seq1.length(); i++) {
                for (int j = 0; j < seq2.length(); j++) {
                    if (seq1.charAt(i) == seq2.charAt(j)) {
                        priorities += seq1.charAt(i) - constant(seq1.charAt(i));
                        break seq;
                    }
                }
            }
        }
        return priorities;
    }

    private static int constant(int item) {
        return item > 96 ? 96 : (64 - 26);
    }
}

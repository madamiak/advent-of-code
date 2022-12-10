package com.example.aoc2022;

import com.example.AocBase;

import java.util.*;
import java.util.stream.Collectors;

public class Day5 extends AocBase {
    public static void main(String[] args) {
        System.out.println(task1(readFirst(Day5.class)));
        System.out.println(task2(readFirst(Day5.class)));
    }

    public static String task1(List<String> input) {
        List<Deque<Character>> stacks = readStacks(input);
        List<Operation> operations = readOperations(input);
        for (Operation operation : operations) {
            for (int i = 0; i < operation.amount; i++) {
                stacks.get(operation.to).push(stacks.get(operation.from).pop());
            }
        }
        return stacks.stream()
                .map(Deque::peek)
                .filter(Objects::nonNull)
                .map(Object::toString)
                .collect(Collectors.joining());
    }

    public static String task2(List<String> input) {
        List<Deque<Character>> stacks = readStacks(input);
        List<Operation> operations = readOperations(input);
        for (Operation operation : operations) {
            Stack<Character> temp = new Stack<>();
            for (int i = 0; i < operation.amount; i++) {
                Character pop = stacks.get(operation.from).pop();
                temp.add(pop);
            }
            while (!temp.isEmpty()) {
                Character push = temp.pop();
                stacks.get(operation.to).push(push);
            }
        }
        return stacks.stream()
                .map(Deque::peek)
                .filter(Objects::nonNull)
                .map(Object::toString)
                .collect(Collectors.joining());
    }

    private static List<Operation> readOperations(List<String> input) {
        return input.stream()
                .filter(e -> e.contains("move"))
                .map(Day5::toOperation)
                .toList();
    }

    private static Operation toOperation(String line) {
        String[] tokens = line.split(" ");
        return new Operation(_int(tokens[1]), _int(tokens[3]) - 1, _int(tokens[5]) - 1);
    }

    private static List<Deque<Character>> readStacks(List<String> input) {
        List<Deque<Character>> stacks = new ArrayList<>();
        Iterator<String> iterator = input.iterator();
        while (iterator.hasNext()) {
            String line = iterator.next();
            if (line.contains("1")) break;
            char[] chars = line.toCharArray();
            for (int i = 1; i < chars.length; i += 4) {
                int j = i / 4;
                if (stacks.size() <= j) {
                    stacks.add(new ArrayDeque<>());
                }
                if (chars[i] != ' ') {
                    stacks.get(j).add(chars[i]);
                }
            }
        }
        return stacks;
    }

    private record Operation(int amount, int from, int to) {
    }
}

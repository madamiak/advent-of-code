package com.example.aoc2022;

import com.example.AocBase;

import java.util.Collections;
import java.util.List;
import java.util.Stack;

public class Day10 extends AocBase {

    public static void main(String[] args) {
        List<String> input = readInput(Day10.class);
        System.out.println(task1(input));
        System.out.println(task2(input));
    }

    private static int task1(List<String> input) {
        int sum = 0;
        int registerX = 1;
        int cycle = 1;
        Stack<String> cmds = new Stack<>();
        Collections.reverse(input);
        cmds.addAll(input);
        List<Integer> elements = List.of(20, 60, 100, 140, 180, 220);
        while (!cmds.isEmpty()) {
            cycle++;
            String line = cmds.pop();
            String[] args = line.split(" ");
            switch (args[0]) {
                case "noop" -> {
                }
                case "addx" -> cmds.push("addx2 " + args[1]);
                case "addx2" -> registerX += _int(args[1]);
            }
            if (elements.contains(cycle)) {
                sum += registerX * cycle;
            }
        }
        return sum;
    }

    private static int task2(List<String> input) {
        Position spritePos = new Position(1, 3);
        int renderPos = 1;
        int cycle = 1;
        Stack<String> cmds = new Stack<>();
        cmds.addAll(input);
        while (!cmds.isEmpty()) {
            String line = cmds.pop();
            String[] args = line.split(" ");

            boolean shouldRender = spritePos.shouldRender(renderPos);
            System.out.print(shouldRender ? "#" : ".");
            if (cycle % 40 == 0) {
                System.out.println();
            }

            switch (args[0]) {
                case "noop" -> {}
                case "addx" -> cmds.push("addx2 " + args[1]);
                case "addx2" -> spritePos = spritePos.move(_int(args[1]));
            }

            cycle++;
            renderPos = (renderPos + 1) % 40;
        }
        return -1;
    }

    private record Position(int s, int e) {
        public Position move(int d) {
            return new Position(s + d, e + d);
        }

        public boolean shouldRender(int renderPos) {
            return renderPos >= s && renderPos <= e;
        }
    }

}

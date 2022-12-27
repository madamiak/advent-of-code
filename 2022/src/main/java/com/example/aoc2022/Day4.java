package com.example.aoc2022;

import com.example.AocBase;

import java.util.List;

public class Day4 extends AocBase {
    public static void main(String[] args) {
        System.out.println(task1(readInput(Day4.class)));
        System.out.println(task2(readInput(Day4.class)));
    }

    public static int task1(List<String> input) {
        int occs = 0;
        for (String line : input) {
            String[] args = line.split(",");
            String[] left = args[0].split("-");
            String[] right = args[1].split("-");
            if ((_int(left[0]) <= _int(right[0]) && _int(left[1]) >= _int(right[1]))
                    || (_int(left[0]) >= _int(right[0]) && _int(left[1]) <= _int(right[1]))) {
                occs++;
            }
        }
        return occs;
    }

    public static int task2(List<String> input) {
        int occs = 0;
        for (String line : input) {
            String[] args = line.split(",");
            String[] left = args[0].split("-");
            String[] right = args[1].split("-");
            if (!((_int(left[1]) < _int(right[0]))
                    || (_int(right[1]) < _int(left[0])))) {
                occs++;
            }
        }
        return occs;
    }
}

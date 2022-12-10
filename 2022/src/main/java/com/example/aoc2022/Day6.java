package com.example.aoc2022;

import com.example.AocBase;

import java.util.ArrayList;
import java.util.List;

public class Day6 extends AocBase {

    public static void main(String[] args) {
        List<String> input = readFirst(Day6.class);
        System.out.println(task1(input));
        System.out.println(task2(input));
    }

    private static int task1(List<String> input) {
        String line = input.get(0);
        String[] split = line.split("");
        List<String> occs = new ArrayList<>();
        for (int i = 0; i < split.length; i++) {
            String s = split[i];
            if (occs.size() > 4) {
                occs = occs.subList(1, occs.size());
            }
            if (occs.contains(s)) {
                occs = occs.subList(occs.indexOf(s) + 1, occs.size());
            }
            occs.add(s);
            if (occs.size() == 4) {
                return i + 1;
            }
        }
        return -1;
    }

    private static int task2(List<String> input) {
        String line = input.get(0);
        String[] split = line.split("");
        List<String> occs = new ArrayList<>();
        for (int i = 0; i < split.length; i++) {
            String s = split[i];
            if (occs.size() > 14) {
                occs = occs.subList(1, occs.size());
            }
            if (occs.contains(s)) {
                occs = occs.subList(occs.indexOf(s) + 1, occs.size());
            }
            occs.add(s);
            if (occs.size() == 14) {
                return i + 1;
            }
        }
        return -1;
    }
}

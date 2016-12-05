package com.github.madamiak.aoc.day4;

public class Puzzle4_2 {

    public static final String LETTERS = "abcdefghijklmnopqrstuvwxyz";

    public static int solve(String input, String phrase) {
        for (String row : input.split("\n")) {
            String[] s = row.split("[\\[|\\]]");
            String txt = s[0].substring(0, s[0].lastIndexOf("-")).replaceAll("-", " ");
            int number = Integer.parseInt(s[0].substring(s[0].lastIndexOf("-") + 1));

            StringBuilder sb = new StringBuilder();
            for (char c : txt.toCharArray()) {
                if(c != ' ')
                    sb.append(LETTERS.charAt((LETTERS.indexOf(c) + number) % LETTERS.length()));
                else
                    sb.append(c);
            }
            if(sb.toString().contains(phrase)) {
                return number;
            }
        }
        return -1;
    }

}

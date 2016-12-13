package com.github.madamiak.aoc.day5;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Puzzle5_2 {

    public static String solve(String input) throws NoSuchAlgorithmException {
        char[] pwd = new char[]{'-', '-', '-', '-', '-', '-', '-', '-'};
        for (int index = 0; incomplete(pwd); index++) {
            String s = input + index;
            byte[] md5 = MessageDigest.getInstance("MD5").digest(s.getBytes());
            String hex = String.format("%02x", md5[0]) + String.format("%02x", md5[1]) + String.format("%02x", md5[2]);
            if (hex.startsWith("00000")) {
                System.out.println(s);
                int position = Character.getNumericValue(hex.charAt(5));
                if(position < 8 && pwd[position] == '-') {
                    pwd[position] = String.format("%02x", md5[3]).charAt(0);
                }
            }
        }

        return new String(pwd);
    }

    private static boolean incomplete(char[] pwd) {
        boolean incomplete = false;
        for (char c : pwd) {
            if(c == '-') {
                incomplete = true;
                break;
            }
        }
        return incomplete;
    }
}

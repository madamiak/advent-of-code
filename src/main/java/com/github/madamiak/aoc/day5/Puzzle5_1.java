package com.github.madamiak.aoc.day5;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Puzzle5_1 {

    public static String solve(String input) throws NoSuchAlgorithmException {
        StringBuilder sb = new StringBuilder();
        for (int index = 0; sb.toString().length() < 8; index++) {
            String s = input + index;
            byte[] md5 = MessageDigest.getInstance("MD5").digest(s.getBytes());
            String hex = String.format("%02x", md5[0]) + String.format("%02x", md5[1]) + String.format("%02x", md5[2]);
            if (hex.startsWith("00000")) {
                System.out.println(s);
                sb.append(hex.charAt(5));
            }
        }

        return sb.toString();
    }
}

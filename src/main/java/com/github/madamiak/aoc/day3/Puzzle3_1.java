package com.github.madamiak.aoc.day3;

import java.util.Arrays;

public class Puzzle3_1 {

	public static int solve(String input) {
		int result = 0;
		for (String s : input.split("\n")) {
			int[] e = Arrays.stream(s.split("\t")).mapToInt(Integer::parseInt).toArray();
			if (e[0] + e[1] > e[2] && e[0] + e[2] > e[1] && e[2] + e[1] > e[0])
				result++;
		}
		return result;
	}

}

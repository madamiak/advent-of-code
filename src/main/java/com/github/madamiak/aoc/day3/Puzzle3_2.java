package com.github.madamiak.aoc.day3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Puzzle3_2 {

	public static int solve(String input) {
		int result = 0;
		List<Integer> f1 = new ArrayList<>();
		List<Integer> f2 = new ArrayList<>();
		List<Integer> f3 = new ArrayList<>();
		for (String s : input.split("\n")) {
			int[] e = Arrays.stream(s.split("\t")).mapToInt(Integer::parseInt).toArray();
			f1.add(e[0]);
			f2.add(e[1]);
			f3.add(e[2]);
		}
		List<Integer> all = new ArrayList<>();
		all.addAll(f1);
		all.addAll(f2);
		all.addAll(f3);
		System.out.println(all);
		for (int i = 0; i < all.size(); i = i + 3) {
			if (all.get(i) + all.get(i+1) > all.get(i+2) && all.get(i) + all.get(i+2) > all.get(i+1) && all.get(i+2) + all.get(i+1) > all.get(i))
				result++;
		}
		return result;
	}
}

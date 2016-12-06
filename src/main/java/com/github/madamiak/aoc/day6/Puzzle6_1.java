package com.github.madamiak.aoc.day6;

import java.util.*;

public class Puzzle6_1 {

	public static String solve(String input) {
		Map<Integer, Map<Character, Integer>> m = new HashMap<>();
		for (int i = 0; i < input.substring(0, input.indexOf("\n")).length(); i++) {
			m.put(i, new HashMap<>());
		}

		for (String s : input.split("\n")) {
			char[] chars = s.toCharArray();
			for (int i = 0; i < chars.length; i++) {
				Map<Character, Integer> map = m.get(i);
				if(map.containsKey(chars[i])) {
					map.put(chars[i], map.get(chars[i]) + 1);
				} else {
					map.put(chars[i], 1);
				}
			}
		}

		StringBuilder sb = new StringBuilder();
		for (Integer integer : m.keySet()) {
			Set<Character> keySet = m.get(integer).keySet();
			Character max = Collections.max(keySet, (o1, o2) -> {
				if (m.get(integer).get(o1) > m.get(integer).get(o2)) {
					return 1;
				} else if (m.get(integer).get(o2) > m.get(integer).get(o1)) {
					return -1;
				} else {
					return o1.compareTo(o2);
				}
			});
			sb.append(max);
		}

		return sb.toString();
	}
}

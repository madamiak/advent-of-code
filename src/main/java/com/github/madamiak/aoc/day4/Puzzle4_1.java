package com.github.madamiak.aoc.day4;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Puzzle4_1 {
	public static int solve(String input) {
		int result = 0;
		Map<Character, Integer> m = new HashMap<>();
		String[] s = input.split("[\\[|\\]]");
		String txt = s[0].substring(s[0].lastIndexOf("-") - 1).replaceAll("-", "");
		int number = Integer.parseInt(s[0].substring(s[0].lastIndexOf("-") + 1));
		String hash = s[1];

		for (char c : txt.toCharArray()) {
			if(m.containsKey(c)) {
				m.put(c, m.get(c) + 1);
			} else {
				m.put(c, 1);
			}
		}

		Character[] keySet = m.keySet().toArray(new Character[]{});
		Arrays.sort(keySet);

		boolean ok = true;
		char[] chars = hash.toCharArray();
		for (int i = 0; i < chars.length; i++) {
			if(!Character.valueOf(chars[i]).equals(keySet[i])) {
				ok = false;
			}
		}

		if(ok) {
			result ++;
		}

		return result;
	}
}

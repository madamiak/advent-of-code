package com.github.madamiak.aoc.day1;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Puzzle1_1 {

	private static final String CARDINAL_DIRECTIONS = "NESWNESW";
	private final Map<Character, Integer> moves = new HashMap<>();

	public Puzzle1_1() {
		moves.put('N', 0);
		moves.put('E', 0);
		moves.put('S', 0);
		moves.put('W', 0);
	}

	public int solve(String input) {
		char cardinalDirection = 'N';
		List<String> instructions = Arrays.asList(input.split(", "));
		for (String instruction : instructions) {
			char turnDirection = instruction.charAt(0);
			cardinalDirection = getCardinalDirection(cardinalDirection, turnDirection);
			moves.put(cardinalDirection, moves.get(cardinalDirection) + Integer.parseInt(instruction.substring(1, instruction.length())));
		}
		return Math.abs(moves.get('N') - moves.get('S')) + Math.abs(moves.get('E') - moves.get('W'));
	}

	private char getCardinalDirection(char cardinalDirection, char turnDirection) {
		int diff = turnDirection == 'R' ? 1 : 3;
		return CARDINAL_DIRECTIONS.charAt(CARDINAL_DIRECTIONS.indexOf(cardinalDirection) + diff);
	}
}

package com.github.madamiak.aoc.day1;

import java.util.Arrays;

public class Puzzle1_1 {

	public static int solve(String input) {
		Human human = new Human();
		String[] instructions = input.split(", ");
		Arrays.stream(instructions).forEach(instruction -> move(human, instruction));
		return human.getBlocksAwayFromStart();
	}

	private static void move(Human human, String instruction) {
		human.move(instruction.charAt(0), Integer.parseInt(instruction.substring(1, instruction.length())));
	}

	private static class Human {
		private static final String CARDINAL_DIRECTIONS = "01230123";
		private static final int[] MOVES = new int[4];

		private int lastDir = 0;

		void move(char turnDirection, int blocks) {
			lastDir = getDirectionAfterTurning(turnDirection);
			MOVES[lastDir] += blocks;
		}

		private int getDirectionAfterTurning(char turnDirection) {
			int diff = turnDirection == 'R' ? 1 : 3;
			return Character.getNumericValue(CARDINAL_DIRECTIONS.charAt(lastDir + diff));
		}

		int getBlocksAwayFromStart() {
			return Math.abs(MOVES[0] - MOVES[2]) + Math.abs(MOVES[1] - MOVES[3]);
		}
	}
}

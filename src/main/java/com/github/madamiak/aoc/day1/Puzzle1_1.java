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
		char turnDirection = instruction.charAt(0);
		int blocks = Integer.parseInt(instruction.substring(1, instruction.length()));
		human.move(turnDirection, blocks);
	}

	private static class Human {
		private static final String CARDINAL_DIRECTIONS = "01230123";
		private static final int[] MOVES = new int[4];

		private int facingDirection = 0;

		void move(char turnDirection, int blocks) {
			facingDirection = getDirectionAfterTurning(turnDirection);
			MOVES[facingDirection] += blocks;
		}

		private int getDirectionAfterTurning(char turnDirection) {
			int diff = turnDirection == 'R' ? 1 : 3;
			return Character.getNumericValue(CARDINAL_DIRECTIONS.charAt(facingDirection + diff));
		}

		int getBlocksAwayFromStart() {
			return Math.abs(MOVES[0] - MOVES[2]) + Math.abs(MOVES[1] - MOVES[3]);
		}
	}
}

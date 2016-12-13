package com.github.madamiak.aoc.day1;

import java.awt.*;
import java.util.*;
import java.util.List;

public class Puzzle1_2 {

	private static final String CARDINAL_DIRECTIONS = "NESWNESW";
	private static final List<Point> points = new ArrayList<>();

	public static int solve(String input) {
		char cardinalDirection = 'N';
		points.add(new Point(0, 0));
		Human human = new Human(null);
		List<String> instructions = Arrays.asList(input.split(", "));
		for (String instruction : instructions) {
			human.move(instruction.charAt(0), Integer.parseInt(instruction.substring(1, instruction.length())));
			char turnDirection = instruction.charAt(0);
			cardinalDirection = getCardinalDirection(cardinalDirection, turnDirection);
			for (Integer i = 0; i < Integer.valueOf(instruction.substring(1, instruction.length())); i++) {
				Point lastPoint = points.get(points.size() - 1);
				switch (cardinalDirection) {
				case 'N':
					Point e = new Point(lastPoint.x, lastPoint.y + 1);
					if (points.contains(e)) {
						return Math.abs(e.x) + Math.abs(e.y);
					} else {
						points.add(e);
					}
					break;
				case 'E':
					Point e1 = new Point(lastPoint.x + 1, lastPoint.y);
					if (points.contains(e1)) {
						return Math.abs(e1.x) + Math.abs(e1.y);
					} else {
						points.add(e1);
					}
					break;
				case 'S':
					Point e2 = new Point(lastPoint.x, lastPoint.y - 1);
					if (points.contains(e2)) {
						return Math.abs(e2.x) + Math.abs(e2.y);
					} else {
						points.add(e2);
					}
					break;
				case 'W':
					Point e3 = new Point(lastPoint.x - 1, lastPoint.y);
					if (points.contains(e3)) {
						return Math.abs(e3.x) + Math.abs(e3.y);
					} else {
						points.add(e3);
					}
					break;
				}

			}
			if(!human.getDoubleVisitedBlocks().isEmpty()){
				return human.getDoubleVisitedBlocks().get(0).getBlocksAwayFrom(0,0);
			}
		}
		return 0;
	}

	private static char getCardinalDirection(char cardinalDirection, char turnDirection) {
		int diff = turnDirection == 'R' ? 1 : 3;
		return CARDINAL_DIRECTIONS.charAt(CARDINAL_DIRECTIONS.indexOf(cardinalDirection) + diff);
	}

	private static class Human {
		private static final String CARDINAL_DIRECTIONS = "01230123";
		// N - 0	x,y -> x+0, y+1			0=> 0, 0=> 1
		// E - 1	x,y -> x+1, y+0			1=> 1, 1=> 0
		// S - 2	x,y -> x+0, y-1			2=> 0, 2=>-1
		// W - 3	x,y -> x-1, y+0			3=>-1, 3=>-0

		private int facingDirection = 0;
		private Stack<Block> visitedBlocks = new Stack<>();

		Human(Block startingBlock) {
			visitedBlocks.push(startingBlock);
		}

		void move(char turnDirection, int blocks) {
			facingDirection = getDirectionAfterTurning(turnDirection);
			visitedBlocks.addAll(Block.createMany(visitedBlocks.peek(), facingDirection, blocks));
		}

		List<Block> getDoubleVisitedBlocks() {
			return null;
		}

		private int getDirectionAfterTurning(char turnDirection) {
			int diff = turnDirection == 'R' ? 1 : 3;
			return Character.getNumericValue(CARDINAL_DIRECTIONS.charAt(facingDirection + diff));
		}
	}

	private static class Block {
		final int x;
		final int y;

		public static Block create(int x, int y) {
			return new Block(x, y);
		}

		static List<Block> createMany(Block starting, int direction, int amount) {
			List<Block> blocks = new ArrayList<>();
			for (int i = 0; i < amount; i++) {
//				blocks.add(new Block(starting.x + dx, starting.y + dy));
			}
			return null;
		}

		private Block(int x, int y) {
			this.x = x;
			this.y = y;
		}

		int getBlocksAwayFrom(int x, int y) {
			return 0;
		}
	}
}

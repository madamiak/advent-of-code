package com.github.madamiak.aoc.day1;

import java.awt.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Puzzle1_2 {

	private static final String CARDINAL_DIRECTIONS = "NESWNESW";
	private static final List<Point> points = new ArrayList<>();

	public static int solve(String input) {
		char cardinalDirection = 'N';
		points.add(new Point(0, 0));
		List<String> instructions = Arrays.asList(input.split(", "));
		for (String instruction : instructions) {
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
		}
		return 0;
	}

	private static char getCardinalDirection(char cardinalDirection, char turnDirection) {
		int diff = turnDirection == 'R' ? 1 : 3;
		return CARDINAL_DIRECTIONS.charAt(CARDINAL_DIRECTIONS.indexOf(cardinalDirection) + diff);
	}
}

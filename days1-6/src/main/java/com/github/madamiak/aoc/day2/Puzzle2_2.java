package com.github.madamiak.aoc.day2;

import java.awt.*;
import java.util.HashMap;
import java.util.Map;

public class Puzzle2_2 {

	private static final String[][] BOARD = {
			{" ", " ", " ", " ", " ", " ", " "},
			{" ", " ", " ", "1", " ", " ", " "},
			{" ", " ", "2", "3", "4", " ", " "},
			{" ", "5", "6", "7", "8", "9", " "},
			{" ", " ", "A", "B", "C", " ", " "},
			{" ", " ", " ", "D", " ", " ", " "},
			{" ", " ", " ", " ", " ", " ", " "}
	};

	public static String solve(String input) {
		Map<Character, Point> move = new HashMap<>();
		move.put('U', new Point(0, -1));
		move.put('R', new Point(1, 0));
		move.put('D', new Point(0, 1));
		move.put('L', new Point(-1, 0));
		StringBuilder result = new StringBuilder();
		Point previousPosition = new Point(1, 3);
		for (String s : input.split("\n")) {
			for (char c : s.toCharArray()) {
				Point m = move.get(c);
				int nx = previousPosition.x + m.x;
				int ny = previousPosition.y + m.y;
				if (nx > 0 && nx < 6 && ny > 0 && ny < 6 && !BOARD[ny][nx].equals(" ")) {
					previousPosition.move(nx, ny);
				}
			}
			result.append(BOARD[previousPosition.y][previousPosition.x]);
		}
		return result.toString();
	}

}

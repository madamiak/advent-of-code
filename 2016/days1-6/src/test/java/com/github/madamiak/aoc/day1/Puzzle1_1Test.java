package com.github.madamiak.aoc.day1;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.Test;

import com.github.madamiak.aoc.InputReader;

public class Puzzle1_1Test {

	@Test
	public void shouldReturn5WhenR2_L3() {
		int result = Puzzle1_1.solve("R2, R3");

		assertThat(result).isEqualTo(5);
	}

	@Test
	public void shouldReturn2WhenR2_R2_R2() {
		int result = Puzzle1_1.solve("R2, R2, R2");

		assertThat(result).isEqualTo(2);
	}

	@Test
	public void shouldReturn12WhenR5_L5_R5_R3() {
		int result = Puzzle1_1.solve("R5, L5, R5, R3");

		assertThat(result).isEqualTo(12);
	}

	@Test
	public void answer() {
		System.out.println(Puzzle1_1.solve(InputReader.read(Puzzle1_1.class)));
	}

}
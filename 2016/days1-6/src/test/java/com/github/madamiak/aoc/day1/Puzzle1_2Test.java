package com.github.madamiak.aoc.day1;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.Test;

import com.github.madamiak.aoc.InputReader;

public class Puzzle1_2Test {

	@Test
	public void should() {
		assertThat(Puzzle1_2.solve("R8, R4, R4, R8")).isEqualTo(4);
	}

	@Test
	public void answer() {
		assertThat(Puzzle1_2.solve(InputReader.read(Puzzle1_2.class))).isEqualTo(141);
	}

}
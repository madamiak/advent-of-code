package com.github.madamiak.aoc.day1;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.Test;

public class Puzzle1_2Test {

	@Test
	public void should() {
		assertThat(Puzzle1_2.solve("R8, R4, R4, R8")).isEqualTo(4);
	}

	@Test
	public void answer() {
		System.out.println(Puzzle1_2.solve(
				"R2, L5, L4, L5, R4, R1, L4, R5, R3, R1, L1, L1, R4, L4, L1, R4, L4, R4, L3, R5, R4, R1, R3, L1, L1, " +
						"R1, L2, R5, L4, L3, R1, L2, L2, R192, L3, R5, R48, R5, L2, R76, R4, R2, R1, L1, L5, L1, R185," +
						" L5, L1, R5, L4, R1, R3, L4, L3, R1, L5, R4, L4, R4, R5, L3, L1, L2, L4, L3, L4, R2, R2, L3, " +
						"L5, R2, R5, L1, R1, L3, L5, L3, R4, L4, R3, L1, R5, L3, R2, R4, R2, L1, R3, L1, L3, L5, R4, " +
						"R5, R2, R2, L5, L3, L1, L1, L5, L2, L3, R3, R3, L3, L4, L5, R2, L1, R1, R3, R4, L2, R1, L1, " +
						"R3, R3, L4, L2, R5, R5, L1, R4, L5, L5, R1, L5, R4, R2, L1, L4, R1, L1, L1, L5, R3, R4, L2, " +
						"R1, R2, R1, R1, R3, L5, R1, R4"));
	}

}
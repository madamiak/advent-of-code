package com.github.madamiak.aoc.day4;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.Test;

public class Puzzle4_1Test {

	@Test
	public void shouldReturn1() {
		assertThat(Puzzle4_1.solve("aaaaa-bbb-z-y-x-123[abxyz]")).isEqualTo(1);
	}
}
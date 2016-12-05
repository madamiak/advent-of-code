package com.github.madamiak.aoc.day5;

import org.junit.Test;

import java.security.NoSuchAlgorithmException;

import static org.assertj.core.api.Assertions.assertThat;

public class Puzzle5_1Test {

    @Test
    public void should() throws NoSuchAlgorithmException {
        assertThat(Puzzle5_1.solve("abc")).isEqualTo("18f47a30");
    }

    @Test
    public void answer() throws NoSuchAlgorithmException {
        System.out.println(Puzzle5_1.solve("wtnhxymk"));
    }

}
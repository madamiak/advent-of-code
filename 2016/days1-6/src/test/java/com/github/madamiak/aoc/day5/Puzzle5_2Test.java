package com.github.madamiak.aoc.day5;

import org.junit.Test;

import java.security.NoSuchAlgorithmException;

import static org.assertj.core.api.StrictAssertions.assertThat;

public class Puzzle5_2Test {

    @Test
    public void should() throws NoSuchAlgorithmException {
        assertThat(Puzzle5_2.solve("abc")).isEqualTo("05ace8e3");
    }

    @Test
    public void answer() throws NoSuchAlgorithmException {
        System.out.println(Puzzle5_2.solve("wtnhxymk"));
    }

}
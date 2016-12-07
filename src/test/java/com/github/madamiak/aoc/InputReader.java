package com.github.madamiak.aoc;

import static java.lang.ClassLoader.getSystemResource;
import static java.nio.file.Files.lines;
import static java.nio.file.Paths.get;
import static java.util.stream.Collectors.joining;

import java.io.IOException;
import java.net.URISyntaxException;

public class InputReader {

	public static String read(Class puzzleClass) {
		try {
			return lines(get(getSystemResource(puzzleClass.getSimpleName() + ".txt").toURI()))
					.collect(joining("\n"));
		} catch (IOException | URISyntaxException e) {
			throw new RuntimeException(e);
		}
	}

}

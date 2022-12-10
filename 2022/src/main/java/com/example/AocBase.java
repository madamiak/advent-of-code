package com.example;

import lombok.SneakyThrows;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

import static java.util.Locale.ENGLISH;

public abstract class AocBase {

    @SneakyThrows
    protected static <T extends AocBase> List<String> readFirst(Class<T> tClass) {
        return read(tClass, 1);
    }

    @SneakyThrows
    protected static <T extends AocBase> List<String> readSecond(Class<T> tClass) {
        return read(tClass, 2);
    }

    @SneakyThrows
    protected static <T extends AocBase> List<String> read(Class<T> tClass, int taskNumber) {
        return Files.readAllLines(Paths.get("./2022/src/main/resources/" + tClass.getSimpleName().toLowerCase(ENGLISH) + "_" + taskNumber + ".txt"));
    }

    protected static int _int(String s) {
        return Integer.parseInt(s);
    }
}

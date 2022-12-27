package com.example;

import lombok.SneakyThrows;

import java.math.BigInteger;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

import static java.util.Locale.ENGLISH;

public abstract class AocBase {

    @SneakyThrows
    protected static <T extends AocBase> List<String> readInput(Class<T> tClass) {
        return read(tClass);
    }

    @SneakyThrows
    protected static <T extends AocBase> List<String> read(Class<T> tClass) {
        return Files.readAllLines(Paths.get("./2022/src/main/resources/" + tClass.getSimpleName().toLowerCase(ENGLISH) + ".txt"));
    }

    protected static int _int(String s) {
        return Integer.parseInt(s);
    }

    protected static BigInteger _bint(int i) {
        return BigInteger.valueOf(i);
    }

    protected static int[][] _arri(List<String> l) {
        int[][] arr = new int[l.size()][];
        for (int i = 0; i < l.size(); i++) {
            arr[i] = new int[l.get(i).length()];
            for (int j = 0; j < l.get(i).length(); j++) {
                arr[i][j] = _int(l.get(i).split("")[j]);
            }
        }
        return arr;
    }

    protected static String[][] _arrs(List<String> l) {
        String[][] arr = new String[l.size()][];
        for (int i = 0; i < l.size(); i++) {
            arr[i] = new String[l.get(i).length()];
            for (int j = 0; j < l.get(i).length(); j++) {
                arr[i][j] = l.get(i).split("")[j];
            }
        }
        return arr;
    }
}

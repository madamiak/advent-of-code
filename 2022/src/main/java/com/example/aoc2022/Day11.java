package com.example.aoc2022;

import com.example.AocBase;

import java.math.BigInteger;
import java.util.*;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static java.math.BigInteger.ONE;

public class Day11 extends AocBase {

    private static Map<Integer, Monkey> monkeys = new HashMap<>();
    private static Map<Integer, BigMonkey> bigMonkeys = new HashMap<>();

    public static void main(String[] args) {
//        System.out.println(task1());
        System.out.println(task2());
    }

    private static int task1() {
        var m0 = new Monkey(List.of(96, 60, 68, 91, 83, 57, 85), x -> x * 2, x -> x % 17 == 0, x -> throwItemTo(x, 2), x -> throwItemTo(x, 5));
        var m1 = new Monkey(List.of(75, 78, 68, 81, 73, 99), x -> x + 3, x -> x % 13 == 0, x -> throwItemTo(x, 7), x -> throwItemTo(x, 4));
        var m2 = new Monkey(List.of(69, 86, 67, 55, 96, 69, 94, 85), x -> x + 6, x -> x % 19 == 0, x -> throwItemTo(x, 6), x -> throwItemTo(x, 5));
        var m3 = new Monkey(List.of(88, 75, 74, 98, 80), x -> x + 5, x -> x % 7 == 0, x -> throwItemTo(x, 7), x -> throwItemTo(x, 1));
        var m4 = new Monkey(List.of(82), x -> x + 8, x -> x % 11 == 0, x -> throwItemTo(x, 0), x -> throwItemTo(x, 2));
        var m5 = new Monkey(List.of(72, 92, 92), x -> x * 5, x -> x % 3 == 0, x -> throwItemTo(x, 6), x -> throwItemTo(x, 3));
        var m6 = new Monkey(List.of(74, 61), x -> x * x, x -> x % 2 == 0, x -> throwItemTo(x, 3), x -> throwItemTo(x, 1));
        var m7 = new Monkey(List.of(76, 86, 83, 55), x -> x + 4, x -> x % 5 == 0, x -> throwItemTo(x, 4), x -> throwItemTo(x, 0));
        monkeys.put(0, m0);
        monkeys.put(1, m1);
        monkeys.put(2, m2);
        monkeys.put(3, m3);
        monkeys.put(4, m4);
        monkeys.put(5, m5);
        monkeys.put(6, m6);
        monkeys.put(7, m7);
        for (int i = 0; i < 20; i++) {
            for (int j = 0; j < monkeys.size(); j++) {
                Monkey monkey = monkeys.get(j);
                monkey.inspectAll();
            }
        }
        return monkeys.values().stream().map(e -> e.inspectedCount).sorted(Comparator.reverseOrder()).limit(2).reduce(1, (x, y) -> x * y);
    }

    private static BigInteger task2() { // 145356120 too low
        var m0 = new BigMonkey(List.of(96, 60, 68, 91, 83, 57, 85),     x -> x.multiply(_bint(2)),  x -> x.mod(_bint(17)).equals(BigInteger.ZERO), x -> throwItemTo(x, 2), x -> throwItemTo(x, 5));
        var m1 = new BigMonkey(List.of(75, 78, 68, 81, 73, 99),         x -> x.add(_bint(3)),       x -> x.mod(_bint(13)).equals(BigInteger.ZERO), x -> throwItemTo(x, 7), x -> throwItemTo(x, 4));
        var m2 = new BigMonkey(List.of(69, 86, 67, 55, 96, 69, 94, 85), x -> x.add(_bint(6)),       x -> x.mod(_bint(19)).equals(BigInteger.ZERO), x -> throwItemTo(x, 6), x -> throwItemTo(x, 5));
        var m3 = new BigMonkey(List.of(88, 75, 74, 98, 80),             x -> x.add(_bint(5)),       x -> x.mod(_bint(7)).equals(BigInteger.ZERO),  x -> throwItemTo(x, 7), x -> throwItemTo(x, 1));
        var m4 = new BigMonkey(List.of(82),                             x -> x.add(_bint(8)),       x -> x.mod(_bint(11)).equals(BigInteger.ZERO), x -> throwItemTo(x, 0), x -> throwItemTo(x, 2));
        var m5 = new BigMonkey(List.of(72, 92, 92),                     x -> x.multiply(_bint(5)),  x -> x.mod(_bint(3)).equals(BigInteger.ZERO),  x -> throwItemTo(x, 6), x -> throwItemTo(x, 3));
        var m6 = new BigMonkey(List.of(74, 61),                         x -> x.pow(2),                 x -> x.mod(_bint(2)).equals(BigInteger.ZERO),  x -> throwItemTo(x, 3), x -> throwItemTo(x, 1));
        var m7 = new BigMonkey(List.of(76, 86, 83, 55),                 x -> x.add(_bint(4)),       x -> x.mod(_bint(5)).equals(BigInteger.ZERO),  x -> throwItemTo(x, 4), x -> throwItemTo(x, 0));
        bigMonkeys.put(0, m0);
        bigMonkeys.put(1, m1);
        bigMonkeys.put(2, m2);
        bigMonkeys.put(3, m3);
        bigMonkeys.put(4, m4);
        bigMonkeys.put(5, m5);
        bigMonkeys.put(6, m6);
        bigMonkeys.put(7, m7);
        for (int i = 1; i < 10001; i++) {
            for (int j = 0; j < bigMonkeys.size(); j++) {
                BigMonkey monkey = bigMonkeys.get(j);
                monkey.inspectAll();
            }
        }
        return bigMonkeys.values().stream().map(e -> e.inspectedCount).sorted(Comparator.reverseOrder()).limit(2).map(AocBase::_bint).reduce(ONE, BigInteger::multiply);
    }

    private static void throwItemTo(Integer item, int monkeyId) {
        monkeys.get(monkeyId).obtain(item);
    }

    private static void throwItemTo(BigInteger item, int monkeyId) {
        bigMonkeys.get(monkeyId).obtain(item);
    }

    private static class Monkey {
        private final Queue<Integer> items;
        private final Function<Integer, Integer> operation;
        private final Function<Integer, Boolean> test;
        private final Consumer<Integer> ifTrue;
        private final Consumer<Integer> ifFalse;
        private int worryLevel;
        private int inspectedCount = 0;

        private Monkey(List<Integer> startingItems, Function<Integer, Integer> operation, Function<Integer, Boolean> test, Consumer<Integer> ifTrue, Consumer<Integer> ifFalse) {
            this.items = new ArrayDeque<>(startingItems);
            this.operation = operation;
            this.test = test;
            this.ifTrue = ifTrue;
            this.ifFalse = ifFalse;
        }

        public void obtain(Integer item) {
            items.add(item);
        }

        public void inspectAll() {
            while (!items.isEmpty()) {
                var item = items.poll();
                inspectedCount++;
                worryLevel = operation.apply(item);
                worryLevel /= 3;
                if (test.apply(worryLevel)) {
                    ifTrue.accept(worryLevel);
                } else {
                    ifFalse.accept(worryLevel);
                }
            }
        }
    }

    private static class BigMonkey {
        private static final BigInteger leastCommonMultiple = Stream.of(17, 13, 19, 7, 11, 3, 2, 5)  // monkeys' tests divisors
                .map(AocBase::_bint)
                .reduce(ONE, BigInteger::multiply);
        private final Queue<BigInteger> items;
        private final Function<BigInteger, BigInteger> operation;
        private final Function<BigInteger, Boolean> test;
        private final Consumer<BigInteger> ifTrue;
        private final Consumer<BigInteger> ifFalse;
        private BigInteger worryLevel;
        private int inspectedCount = 0;

        private BigMonkey(List<Integer> startingItems, Function<BigInteger, BigInteger> operation, Function<BigInteger, Boolean> test, Consumer<BigInteger> ifTrue, Consumer<BigInteger> ifFalse) {
            this.items = startingItems.stream().map(AocBase::_bint).collect(Collectors.toCollection(ArrayDeque::new));
            this.operation = operation;
            this.test = test;
            this.ifTrue = ifTrue;
            this.ifFalse = ifFalse;
        }

        public void obtain(BigInteger item) {
            items.add(item);
        }

        public void inspectAll() {
            while (!items.isEmpty()) {
                var item = items.poll();
                inspectedCount++;
                worryLevel = operation.apply(item);
                worryLevel = worryLevel.mod(leastCommonMultiple);
                if (test.apply(worryLevel)) {
                    ifTrue.accept(worryLevel);
                } else {
                    ifFalse.accept(worryLevel);
                }
            }
        }
    }

}

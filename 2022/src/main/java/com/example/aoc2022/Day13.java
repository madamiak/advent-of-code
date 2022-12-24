package com.example.aoc2022;

import com.example.AocBase;

import java.util.*;

public class Day13 extends AocBase {

    public static void main(String[] args) {
        List<String> input = readFirst(Day13.class);
        System.out.println(task1(input));
        System.out.println(task2(input));
    }

    private static int task1(List<String> input) {
        List<Pair> pairs = pairs(input);
        int sum = 0;
        for (int i = 0; i < pairs.size(); i++) {
            System.out.printf("=== Pair %d ===%n", i + 1);
            Pair pair = pairs.get(i);
            if (pair.isInOrder()) {
                System.out.println("Add to result " + (i + 1));
                sum += i + 1;
            }
        }
        return sum;
    }

    private static int task2(List<String> input) {
        List<Pair> pairs = pairs(input);
        String div1 = "[[2]]";
        String div2 = "[[6]]";
        pairs.add(Pair.of(div1, div2));
        List<Packet> packets = pairs.stream()
                .map(e -> List.of(e.left, e.right))
                .flatMap(Collection::stream)
                .sorted()
                .toList();
        int result = 1;
        for (int i = 0; i < packets.size(); i++) {
            Packet packet = packets.get(i);
            if(packet.toString().equals(div1) || packet.toString().equals(div2)) {
                result *= (i+1);
            }
        }
        return result;
    }

    private static List<Pair> pairs(List<String> input) {
        List<Pair> pairs = new ArrayList<>();
        for (int i = 0; i < input.size(); i += 3) {
            pairs.add(Pair.of(input.get(i), input.get(i + 1)));
        }
        return pairs;
    }

    private record Pair(Packet left, Packet right) {
        static Pair of(String left, String right) {
            Packet p1 = Packet.of(left);
            Packet p2 = Packet.of(right);
            return new Pair(p1, p2);
        }

        public boolean isInOrder() {
            return left.compareTo(right) < 0;
        }

    }

    @SuppressWarnings({"ConstantConditions", "unchecked"})
    private static class Packet implements Comparable<Packet> {
        private final List<Object> packet;

        private Packet(List<Object> packet) {
            this.packet = packet;
        }

        static Packet of(String packet) {
            List<Object> packets = new LinkedList<>();
            Stack<List<Object>> stack = new Stack<>();
            Scanner scanner = new Scanner(packet);
            scanner.useDelimiter(",");
            while (scanner.hasNext()) {
                String next = scanner.next();
                String[] tokens = next.split("");
                StringBuilder p = new StringBuilder();
                for (String token : tokens) {
                    if (token.equals("[")) {
                        if (!p.isEmpty()) {
                            stack.peek().add(_int(p.toString()));
                            p = new StringBuilder();
                        }
                        stack.push(new ArrayList<>());
                    } else if (token.equals("]")) {
                        if (!p.isEmpty()) {
                            stack.peek().add(_int(p.toString()));
                            p = new StringBuilder();
                        }
                        List<Object> tmp = stack.pop();
                        if (stack.isEmpty()) {
                            packets.add(tmp);
                        } else {
                            stack.peek().add(tmp);
                        }
                    } else {
                        p.append(token);
                    }
                }
                if (!p.isEmpty()) {
                    stack.peek().add(_int(p.toString()));
                }
            }
            return new Packet(packets);
        }

        @Override
        public int compareTo(Packet o) {
            return compareLists(this.packet, o.packet);
        }

        private int compareLists(Object o1, Object o2) {
            System.out.printf("Compare %s vs %s%n", o1, o2);
            List<Object> l1 = fix(o1, o2);
            List<Object> l2 = fix(o2, o1);
            int cmp = 0;
            int i;
            for (i = 0; i < l1.size(); i++) {
                if (i == l2.size()) {
                    System.out.println("Right side ran out of items, so inputs are not in the right order");
                    return 1;
                }
                Object n1 = l1.get(i);
                Object n2 = l2.get(i);
                if (n1 instanceof List || n2 instanceof List) {
                    cmp = compareLists(n1, n2);
                    if (cmp > 0) {
                        return 1;
                    }
                    if (cmp < 0) {
                        return -1;
                    }
                } else {
                    cmp = compareInts((Integer) n1, (Integer) n2);
                    if (cmp > 0) {
                        System.out.println("Right side is smaller, so inputs are not in the right order");
                        return 1;
                    }
                    if (cmp < 0) {
                        System.out.println("Left side is smaller, so inputs are in the right order");
                        return -1;
                    }
                }
            }
            if (i < l2.size()) {
                System.out.println("Left side ran out of items, so inputs are in the right order");
                return -1;
            }
            return cmp;
        }

        private int compareInts(int o1, int o2) {
            System.out.printf("Compare %s vs %s%n", o1, o2);
            return Integer.compare(o1, o2);
        }

        private List<Object> fix(Object o1, Object o2) {
            if (o1 instanceof Integer && o2 instanceof List) {
                System.out.printf("Mixed types %s - %s%n", o1, o2);
                return List.of(o1);
            }
            return (List<Object>) o1;
        }

        @Override
        public String toString() {
            String s = packet.toString().replaceAll(" ", "");
            return s.substring(1, s.length() - 1);
        }
    }

}

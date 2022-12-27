package com.example.aoc2022;

import com.example.AocBase;
import lombok.NonNull;

import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Day9 extends AocBase {

    private static final Map<String, Point> DIRS = Map.of(
            "R", p(1, 0),
            "L", p(-1, 0),
            "U", p(0, 1),
            "D", p(0, -1)
    );

    public static void main(String[] args) {
        List<String> input = readInput(Day9.class);
        System.out.println(task1(input));
        System.out.println(task2(input));
    }

    private static int task1(List<String> input) {
        Set<Point> visited = new HashSet<>();
        Point head = p(0, 0);
        Point tail = p(0, 0);
        visited.add(tail);
        for (String line : input) {
            String[] cmd = line.split(" ");
            String dir = cmd[0];
            int rep = _int(cmd[1]);

            for (int i = 0; i < rep; i++) {
                head = head.move(DIRS.get(dir));
                tail = tail.follow(head);
                visited.add(tail);
            }
        }
        return visited.size();
    }

    private static int task2(List<String> input) {
        Set<Point> visited = new HashSet<>();
        NumberedPoint head = np("H", p(0, 0));
        NumberedPoint tail = np("T", p(0, 0));
        List<NumberedPoint> ps = List.of(
                head,
                np("1", p(0, 0)),
                np("2", p(0, 0)),
                np("3", p(0, 0)),
                np("4", p(0, 0)),
                np("5", p(0, 0)),
                np("6", p(0, 0)),
                np("7", p(0, 0)),
                np("8", p(0, 0)),
                tail
        );
        visited.add(tail.p);
        for (String line : input) {
            String[] cmd = line.split(" ");
            String dir = cmd[0];
            int rep = _int(cmd[1]);
            for (int i = 0; i < rep; i++) {
                head.move(DIRS.get(dir));
                for (int j = 1; j < ps.size(); j++) {
                    NumberedPoint current = ps.get(j);
                    NumberedPoint next = ps.get(j - 1);
                    current.follow(next);
                }
                visited.add(tail.p);
            }
        }
        return visited.size();
    }

    private static Point p(int x, int y) {
        return new Point(x, y);
    }

    private static NumberedPoint np(String id, Point p) {
        return new NumberedPoint(id, p);
    }

    private static record Point(int x, int y) {

        @NonNull
        public Point move(Point dir) {
            return new Point(x + dir.x, y + dir.y);
        }

        public Point follow(Point head) {
            if (shouldStay(head)) {
                return this;
            }
            int dx = Integer.signum(head.x - x);
            int dy = Integer.signum(head.y - y);
            return this.move(p(dx, dy));
        }

        private boolean shouldStay(Point head) {
            int dx = Math.abs(head.x - x);
            int dy = Math.abs(head.y - y);
            return (dx == 0 && dy == 0)
                    || (dx == 1 && dy == 1)
                    || (dx == 1 && dy == 0)
                    || (dx == 0 && dy == 1);
        }
    }

    private static class NumberedPoint {

        private String id;
        private Point p;

        public NumberedPoint(String id, Point p) {
            this.id = id;
            this.p = p;
        }

        public void move(Point dir) {
            p = p.move(dir);
        }

        public void follow(NumberedPoint next) {
            p = p.follow(next.p);
        }

        @Override
        public String toString() {
            return p.toString();
        }
    }

}

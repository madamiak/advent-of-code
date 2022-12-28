package com.example.aoc2022;

import com.example.AocBase;

import java.util.*;

public class Day15 extends AocBase {

    public static void main(String[] args) {
        List<String> input = readInput(Day15.class);
        System.out.println(task1(input));
        System.out.println(task2(input));
    }

    private static int task1(List<String> input) {
        int y = 2000000;
        Map<Point, Integer> sDists = new HashMap<>();
        Set<Point> ss = new HashSet<>();
        Set<Point> bs = new HashSet<>();
        int xMin = Integer.MAX_VALUE;
        int xMax = Integer.MIN_VALUE;
        for (String line : input) {
            String[] args = line.split(":");
            int sx = _int(args[0].substring(args[0].indexOf("x=") + 2, args[0].indexOf(",")));
            int sy = _int(args[0].substring(args[0].indexOf("y=") + 2));
            int bx = _int(args[1].substring(args[1].indexOf("x=") + 2, args[1].indexOf(",")));
            int by = _int(args[1].substring(args[1].indexOf("y=") + 2));
            Point s = new Point(sx, sy);
            Point b = new Point(bx, by);
            int dist = s.dist(b);
            ss.add(s);
            bs.add(b);
            sDists.put(s, dist);
            if (xMin > s.x - dist) xMin = s.x - dist;
            if (xMax < s.x + dist) xMax = s.x + dist;
        }

        int count = 0;
        for (int x = xMin; x <= xMax; x++) {
            Point cur = new Point(x, y);
            for (Point s : sDists.keySet()) {
                if (!ss.contains(cur) && !bs.contains(cur) && cur.dist(s) <= sDists.get(s)) {
                    count++;
                    break;
                }
            }
        }

        return count;
    }

    private static long task2(List<String> input) {
        Map<Point, Integer> sDists = new HashMap<>();
        for (String line : input) {
            String[] args = line.split(":");
            int sx = _int(args[0].substring(args[0].indexOf("x=") + 2, args[0].indexOf(",")));
            int sy = _int(args[0].substring(args[0].indexOf("y=") + 2));
            int bx = _int(args[1].substring(args[1].indexOf("x=") + 2, args[1].indexOf(",")));
            int by = _int(args[1].substring(args[1].indexOf("y=") + 2));

            Point s = new Point(sx, sy);
            Point b = new Point(bx, by);
            int dist = s.dist(b);
            sDists.put(s, dist);
        }

        int upperLimit = 4000000;
        long constant = 4000000L;

        Set<Point> visited = new HashSet<>();
        for (Map.Entry<Point, Integer> entry : sDists.entrySet()) {
            Point s = entry.getKey();
            int dist = entry.getValue();

            for (int d = dist; d >= 0; d--) {
                int dx = dist - d + 1;
                Point[] ps = new Point[]{
                        new Point(s.x + dx, s.y + d),
                        new Point(s.x - dx, s.y - d),
                        new Point(s.x + d, s.y - dx),
                        new Point(s.x - d, s.y + dx)
                };

                for (Point p : ps) {
                    boolean match = false;
                    if (p.x >= 0 && p.x <= upperLimit && p.y >= 0 && p.y <= upperLimit && !visited.contains(p)) {
                        match = sDists.entrySet().stream().allMatch(oEntry -> oEntry.getKey().dist(p) > oEntry.getValue());
                    }
                    if (match) {
                        return p.x * constant + p.y;
                    }
                    visited.add(p);
                }
            }

        }
        return -1;
    }

    private record Point(int x, int y) {
        int dist(Point p) {
            return Math.abs(x - p.x) + Math.abs(y - p.y);
        }
    }

}

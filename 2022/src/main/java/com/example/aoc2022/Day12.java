package com.example.aoc2022;

import com.example.AocBase;

import java.util.*;
import java.util.function.Function;

import static java.util.stream.Collectors.toMap;

public class Day12 extends AocBase {
    static List<P> dirs = List.of(
            new P(0, 1),
            new P(1, 0),
            new P(-1, 0),
            new P(0, -1));

    public static void main(String[] args) {
        List<String> input = readInput(Day12.class);
        System.out.println(task1(input));
        System.out.println(task2(input));
    }

    private static int task1(List<String> input) {
        P start = new P(-1, -1);
        P end = new P(-1, -1);
        List<String> grid = new ArrayList<>();
        for (int i = 0; i < input.size(); i++) {
            String line = input.get(i);
            int j = line.indexOf("S");
            if (j != -1) {
                start = new P(j, i);
            }
            int k = line.indexOf("E");
            if (k != -1) {
                end = new P(k, i);
            }
            grid.add(line.replaceAll("S", "a").replaceAll("E", "z"));
        }

        return bfs(start, end, grid);
    }

    private static int task2(List<String> input) {
        P end = new P(-1, -1);
        List<P> starts = new ArrayList<>();
        List<String> grid = new ArrayList<>();
        for (int i = 0; i < input.size(); i++) {
            String line = input.get(i);
            int j = line.indexOf("S");
            if (j != -1) {
                starts.add(new P(j, i));
            }
            int k = line.indexOf("E");
            if (k != -1) {
                end = new P(k, i);
            }
            int l = line.indexOf("a");
            if(l != -1) {
                starts.add(new P(l, i));
            }
            grid.add(line.replaceAll("S", "a").replaceAll("E", "z"));
        }

        return bfs(starts, end, grid);
    }

    private static List<P> allowed(P current, List<String> grid) {
        List<P> allowed = new ArrayList<>();
        for (P dir : dirs) {
            P newPoint = current.move(dir);
            if (newPoint.x < 0 || newPoint.x >= grid.get(0).length() || newPoint.y < 0 || newPoint.y >= grid.size()) {
                continue;
            }
            char newPointValue = grid.get(newPoint.y).charAt(newPoint.x);
            char currentValue = grid.get(current.y).charAt(current.x);
            if (newPointValue > currentValue + 1) {
                continue;
            }
            allowed.add(newPoint);
        }

        return allowed;
    }

    private static int bfs(P current, P end, List<String> grid) {
        return bfs(List.of(current), end, grid);
    }

    private static int bfs(List<P> currents, P end, List<String> grid) {
        Queue<P> moves = new LinkedList<>(currents);
        Map<P, Integer> dist = moves.stream().collect(toMap(Function.identity(), e -> 0));

        while (!moves.isEmpty()) {
            P next = moves.poll();
            if(next.equals(end)) return dist.get(next);

            List<P> allowed = allowed(next, grid);
            for (P p : allowed) {
                if(!dist.containsKey(p)) {
                    Integer currentDistance = dist.get(next);
                    dist.put(p, currentDistance + 1);
                    moves.add(p);
                }
            }
        }

        return -1;
    }

    private record P(int x, int y) {
        public P move(P dir) {
            return new P(x + dir.x, y + dir.y);
        }
    }

}

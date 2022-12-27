package com.example.aoc2022;

import com.example.AocBase;

import java.util.*;

import static java.lang.Math.max;
import static java.lang.Math.min;

public class Day14 extends AocBase {

    public static void main(String[] args) {
        List<String> input = readInput(Day14.class);
        System.out.println(task1(input));
        System.out.println(task2(input));
    }

    private static int task1(List<String> input) {
        Set<Cell> rocks = new HashSet<>();
        for (String s : input) {
            List<Integer> xs = new ArrayList<>();
            List<Integer> ys = new ArrayList<>();
            String[] rockPaths = s.split(" -> ");
            for (String rockPath : rockPaths) {
                String[] coords = rockPath.split(",");
                xs.add(_int(coords[0]));
                ys.add(_int(coords[1]));
            }
            for (int i = 0; i < xs.size() - 1; i++) {
                int x1 = xs.get(i);
                int y1 = ys.get(i);
                int x2 = xs.get(i + 1);
                int y2 = ys.get(i + 1);
                if (x2 - x1 == 0) {
                    for (int y = min(y1, y2); y <= max(y1, y2); y++) {
                        rocks.add(Cell.rock(x1, y));
                    }
                } else {
                    for (int x = min(x1, x2); x <= max(x1, x2); x++) {
                        rocks.add(Cell.rock(x, y1));
                    }
                }
            }
        }
        int minX = Integer.MAX_VALUE, minY = 0, maxX = Integer.MIN_VALUE, maxY = Integer.MIN_VALUE;
        for (Cell rock : rocks) {
            if (minX > rock.x) minX = rock.x;
            if (maxX < rock.x) maxX = rock.x;
            if (maxY < rock.y) maxY = rock.y;
        }
        Cell source = Cell.source(500, 0);
        Grid grid = new Grid(minX, minY, maxX, maxY, source, rocks);
        grid.fill();
        return grid.sands.size();
    }

    private static int task2(List<String> input) {
        Set<Cell> rocks = new HashSet<>();
        for (String s : input) {
            List<Integer> xs = new ArrayList<>();
            List<Integer> ys = new ArrayList<>();
            String[] rockPaths = s.split(" -> ");
            for (String rockPath : rockPaths) {
                String[] coords = rockPath.split(",");
                xs.add(_int(coords[0]));
                ys.add(_int(coords[1]));
            }
            for (int i = 0; i < xs.size() - 1; i++) {
                int x1 = xs.get(i);
                int y1 = ys.get(i);
                int x2 = xs.get(i + 1);
                int y2 = ys.get(i + 1);
                if (x2 - x1 == 0) {
                    for (int y = min(y1, y2); y <= max(y1, y2); y++) {
                        rocks.add(Cell.rock(x1, y));
                    }
                } else {
                    for (int x = min(x1, x2); x <= max(x1, x2); x++) {
                        rocks.add(Cell.rock(x, y1));
                    }
                }
            }
        }
        int minX = Integer.MAX_VALUE, minY = 0, maxX = Integer.MIN_VALUE, maxY = Integer.MIN_VALUE;
        for (Cell rock : rocks) {
            if (minX > rock.x) minX = rock.x;
            if (maxX < rock.x) maxX = rock.x;
            if (maxY < rock.y) maxY = rock.y;
        }
        Cell source = Cell.source(500, 0);
        Grid grid = new Grid(minX, minY, maxX, maxY + 1, source, rocks);
        grid.fill2();
        return grid.sands.size() + 1;
    }

    private static final class Grid {
        private int minX;
        private final int minY;
        private int maxX;
        private final int maxY;
        private final Cell source;
        private final Set<Cell> rocks;
        private final Set<Cell> sands = new HashSet<>();

        private Grid(int minX, int minY, int maxX, int maxY, Cell source, Set<Cell> rocks) {
            this.minX = minX;
            this.minY = minY;
            this.maxX = maxX;
            this.maxY = maxY;
            this.source = source;
            this.rocks = rocks;
        }

        public String print() {
            StringBuilder sb = new StringBuilder();
            for (int y = minY; y <= maxY; y++) {
                for (int x = minX; x <= maxX; x++) {
                    Cell asRock = Cell.rock(x, y);
                    Cell asSource = Cell.source(x, y);
                    Cell asSand = Cell.sand(x, y);
                    if (rocks.contains(asRock)) {
                        sb.append(asRock.print());
                    } else if (asSource.equals(source)) {
                        sb.append(asSource.print());
                    } else if(sands.contains(asSand)) {
                        sb.append(asSand.print());
                    } else {
                        sb.append(Cell.air(x, y).print());
                    }
                }
                sb.append("\n");
            }
            return sb.toString();
        }

        @Override
        public boolean equals(Object obj) {
            if (obj == this) return true;
            if (obj == null || obj.getClass() != this.getClass()) return false;
            var that = (Grid) obj;
            return this.minX == that.minX &&
                    this.minY == that.minY &&
                    this.maxX == that.maxX &&
                    this.maxY == that.maxY &&
                    Objects.equals(this.source, that.source) &&
                    Objects.equals(this.rocks, that.rocks);
        }

        @Override
        public int hashCode() {
            return Objects.hash(minX, minY, maxX, maxY, source, rocks);
        }

        @Override
        public String toString() {
            return "Grid[" +
                    "minX=" + minX + ", " +
                    "minY=" + minY + ", " +
                    "maxX=" + maxX + ", " +
                    "maxY=" + maxY + ", " +
                    "source=" + source + ", " +
                    "rocks=" + rocks + ']';
        }

        public void fill() {
            while (true) {
                Cell sand = Cell.sand(source.x, source.y);
                sand = move(sand);
                if(sand != null) {
                    sands.add(sand);
                } else {
                    break;
                }
            }
        }

        private Cell move(Cell sand) {
            Cell newPos = sand;
            boolean canMove = true;
            while (canMove) {
                if (!rocks.contains(Cell.rock(newPos.x, newPos.y + 1)) && !sands.contains(Cell.sand(newPos.x, newPos.y + 1))) {
                    if(newPos.x < minX || newPos.x > maxX) {
                        return null;
                    }
                    newPos = Cell.sand(newPos.x, newPos.y + 1);
                } else if (!rocks.contains(Cell.rock(newPos.x - 1, newPos.y + 1)) && !sands.contains(Cell.sand(newPos.x - 1, newPos.y + 1))) {
                    if(newPos.x < minX) {
                        return null;
                    }
                    newPos = Cell.sand(newPos.x - 1, newPos.y + 1);
                } else if (!rocks.contains(Cell.rock(newPos.x + 1, newPos.y + 1)) && !sands.contains(Cell.sand(newPos.x + 1, newPos.y + 1))) {
                    if(newPos.x > maxX) {
                        return null;
                    }
                    newPos = Cell.sand(newPos.x + 1, newPos.y + 1);
                } else {
                    canMove = false;
                }
            }
            return newPos;
        }

        public void fill2() {
            while (true) {
                Cell sand = Cell.sand(source.x, source.y);
                sand = move2(sand);
                if(sand != null) {
                    sands.add(sand);
                } else {
                    break;
                }
            }
        }

        private Cell move2(Cell sand) {
            Cell newPos = sand;
            boolean canMove = true;
            while (canMove) {
                if (!rocks.contains(Cell.rock(newPos.x, newPos.y + 1)) && !sands.contains(Cell.sand(newPos.x, newPos.y + 1))) {
                    if(newPos.y + 1 == maxY) {
                        canMove = false;
                    }
                    newPos = Cell.sand(newPos.x, newPos.y + 1);
                } else if (!rocks.contains(Cell.rock(newPos.x - 1, newPos.y + 1)) && !sands.contains(Cell.sand(newPos.x - 1, newPos.y + 1))) {
                    if(newPos.y + 1 == maxY) {
                        canMove = false;
                    }
                    newPos = Cell.sand(newPos.x - 1, newPos.y + 1);
                } else if (!rocks.contains(Cell.rock(newPos.x + 1, newPos.y + 1)) && !sands.contains(Cell.sand(newPos.x + 1, newPos.y + 1))) {
                    if(newPos.y + 1 == maxY) {
                        canMove = false;
                    }
                    newPos = Cell.sand(newPos.x + 1, newPos.y + 1);
                } else {
                    canMove = false;
                }
            }
            if(newPos.equals(sand)) {
                return null;
            }
            if(newPos.x > maxX) maxX = newPos.x;
            if(newPos.x < minX) minX = newPos.x;
            return newPos;
        }
    }

    private record Cell(int x, int y, String representation) {
        static Cell rock(int x, int y) {
            return new Cell(x, y, "#");
        }

        static Cell source(int x, int y) {
            return new Cell(x, y, "+");
        }

        static Cell air(int x, int y) {
            return new Cell(x, y, ".");
        }

        static Cell sand(int x, int y) {
            return new Cell(x, y, "o");
        }

        public String print() {
            return representation;
        }
    }

}

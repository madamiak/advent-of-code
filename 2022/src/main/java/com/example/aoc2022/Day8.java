package com.example.aoc2022;

import com.example.AocBase;

import java.util.List;

public class Day8 extends AocBase {

    public static void main(String[] args) {
        List<String> input = readInput(Day8.class);
        System.out.println(task1(input));
        System.out.println(task2(input));
    }

    private static int task1(List<String> input) {
        int[][][] trees = toTrees(input);
        walkRight(trees);
        walkLeft(trees);
        walkDown(trees);
        walkUp(trees);
        return countVisible(trees);
    }

    private static int task2(List<String> input) {
        int[][] trees = toTrees2(input);
        int max = 0;
        for (int i = 0; i < trees.length; i++) {
            for (int j = 0; j < trees[i].length; j++) {
                int score = calculateScore(trees, i, j);
                if (score > max) {
                    max = score;
                }
            }
        }
        return max;
    }

    private static void walkRight(int[][][] trees) {
        for (int i = 0; i < trees.length; i++) {
            int max = -1;
            for (int j = 0; j < trees[i].length; j++) {
                int[] tree = trees[i][j];
                if (tree[0] > max) {
                    max = tree[0];
                    tree[1] = 1;
                }
            }
        }
    }

    private static void walkLeft(int[][][] trees) {
        for (int i = 0; i < trees.length; i++) {
            int max = -1;
            for (int j = trees[i].length - 1; j >= 0; j--) {
                int[] tree = trees[i][j];
                if (tree[0] > max) {
                    max = tree[0];
                    tree[2] = 1;
                }
            }
        }
    }

    private static void walkDown(int[][][] trees) {
        for (int i = 0; i < trees[0].length; i++) {
            int max = -1;
            for (int j = 0; j < trees.length; j++) {
                int[] tree = trees[j][i];
                if (tree[0] > max) {
                    max = tree[0];
                    tree[3] = 1;
                }
            }
        }
    }

    private static void walkUp(int[][][] trees) {
        for (int i = 0; i < trees[0].length; i++) {
            int max = -1;
            for (int j = trees.length - 1; j >= 0; j--) {
                int[] tree = trees[j][i];
                if (tree[0] > max) {
                    max = tree[0];
                    tree[4] = 1;
                }
            }
        }
    }

    private static int countVisible(int[][][] trees) {
        int count = 0;
        for (int i = 0; i < trees.length; i++) {
            for (int j = 0; j < trees[i].length; j++) {
                boolean visible = false;
                for (int k = 1; k < trees[i][j].length; k++) {
                    if (trees[i][j][k] == 1) {
                        visible = true;
                        break;
                    }
                }
                if (visible) {
                    count++;
                }
            }
        }
        return count;
    }

    private static int[][][] toTrees(List<String> input) {
        int[][][] trees = new int[input.size()][][];
        for (int i = 0; i < input.size(); i++) {
            trees[i] = new int[input.size()][];
            for (int j = 0; j < input.size(); j++) {
                trees[i][j] = new int[]{_int(input.get(i).split("")[j]), 0, 0, 0, 0};
            }
        }
        return trees;
    }

    private static int[][] toTrees2(List<String> input) {
        int[][] trees = new int[input.size()][];
        for (int i = 0; i < input.size(); i++) {
            trees[i] = new int[input.size()];
            for (int j = 0; j < input.size(); j++) {
                trees[i][j] = _int(input.get(i).split("")[j]);
            }
        }
        return trees;
    }

    private static int calculateScore(int[][] trees, int i, int j) {
        int right = calculateRight(trees, i, j);
        int left = calculateLeft(trees, i, j);
        int down = calculateDown(trees, i, j);
        int up = calculateUp(trees, i, j);
        int result = right * left * down * up;
        return result;
    }

    private static int calculateRight(int[][] trees, int i, int j) {
        int start = trees[i][j];
        int result = 0;
        for (int k = j + 1; k < trees[i].length; k++) {
            result++;
            if (trees[i][k] >= start) {
                break;
            }
        }
        return result;
    }

    private static int calculateLeft(int[][] trees, int i, int j) {
        int start = trees[i][j];
        int result = 0;
        for (int k = j - 1; k >= 0; k--) {
            result++;
            if (trees[i][k] >= start) {
                break;
            }
        }
        return result;
    }

    private static int calculateDown(int[][] trees, int i, int j) {
        int start = trees[i][j];
        int result = 0;
        for (int k = i + 1; k < trees.length; k++) {
            result++;
            if (trees[k][j] >= start) {
                break;
            }
        }
        return result;
    }

    private static int calculateUp(int[][] trees, int i, int j) {
        int start = trees[i][j];
        int result = 0;
        for (int k = i - 1; k >= 0; k--) {
            result++;
            if (trees[k][j] >= start) {
                break;
            }
        }
        return result;
    }

}

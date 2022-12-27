package com.example.aoc2022;

import com.example.AocBase;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Comparator;
import java.util.List;

public class Day7 extends AocBase {

    private static final Tree fs = new Tree();

    public static void main(String[] args) {
        List<String> input = readInput(Day7.class);
        System.out.println(task1(input));
        System.out.println(task2(input));
    }

    private static int task1(List<String> input) {
        for (int i = 0; i < input.size(); i++) {
            String line = input.get(i);
            if (line.contains("$")) {
                int j = i + 1;
                while (j < input.size() && !input.get(j).contains("$")) {
                    j++;
                }
                List<String> cmd = input.subList(i, j);
                parse(cmd);
            }
        }

        Node root = fs.root();
        List<Node> dirs = root.findDirectoriesWithTotalSizeLessThan(100000);
        return dirs.stream().map(Node::totalSize).reduce(0, Integer::sum);
    }

    private static int task2(List<String> input) {
        for (int i = 0; i < input.size(); i++) {
            String line = input.get(i);
            if (line.contains("$")) {
                int j = i + 1;
                while (j < input.size() && !input.get(j).contains("$")) {
                    j++;
                }
                List<String> cmd = input.subList(i, j);
                parse(cmd);
            }
        }

        Node root = fs.root();
        List<Node> dirs = root.findDirectoriesOrderedByTotalSizeAscending();
        int neededSpace = 30000000;
        int fileSystemSpace = 70000000;
        int spaceToFree = neededSpace - (fileSystemSpace - root.totalSize());
        for (Node dir : dirs) {
            if (dir.totalSize() > spaceToFree) {
                return dir.totalSize();
            }
        }
        return -1;
    }

    private static void parse(List<String> cmd) {
        String[] command = cmd.get(0).split(" ");
        List<String[]> output = cmd.subList(1, cmd.size()).stream()
                .map(e -> e.split(" "))
                .toList();
        if (command[1].equals("cd")) {
            fs.cd(command[2]);
        }
        if (command[1].equals("ls")) {
            fs.ls(output);
        }
    }

    private static class Tree {
        Node current;

        public void cd(String dir) {
            if (dir.equals("/")) {
                current = new Node(dir);
            } else if (current.contains(dir)) {
                current = current.get(dir);
            } else if (dir.equals("..")) {
                current = current.parent;
            } else {
                throw new RuntimeException();
            }
        }

        public void ls(List<String[]> output) {
            for (String[] file : output) {
                if (file[0].equals("dir")) {
                    current.child(file[1]);
                } else {
                    current.child(file[1], _int(file[0]));
                }
            }
        }

        private Node root() {
            Node root = current;
            while (root.hasParent()) {
                root = root.parent;
            }
            return root;
        }
    }

    private static class Node {

        private final List<Node> children = new ArrayList<>();
        private Node parent;
        private String name;
        private int size = 0;

        public Node(String name) {
            this.name = name;
        }

        public Node(Node parent, String name) {
            this.parent = parent;
            this.name = name;
        }

        public Node(String name, int size) {
            this.name = name;
            this.size = size;
        }

        public Node(Node parent, String name, int size) {
            this.parent = parent;
            this.name = name;
            this.size = size;
        }

        public void child(String name) {
            children.add(new Node(this, name));
        }

        public void child(String name, int size) {
            children.add(new Node(this, name, size));
        }

        public boolean contains(String dir) {
            return children.stream().anyMatch(e -> e.name.equals(dir));
        }

        public Node get(String dir) {
            return children.stream().filter(e -> e.name.equals(dir)).findFirst().orElseThrow();
        }

        public boolean hasParent() {
            return parent != null;
        }

        private int totalSize() {
            return size + children.stream().map(Node::totalSize).reduce(0, Integer::sum);
        }

        public List<Node> findDirectoriesWithTotalSizeLessThan(int maxSize) {
            List<Node> dirs = new ArrayList<>();
            if (size == 0 && this.totalSize() < maxSize) dirs.add(this);
            dirs.addAll(children.stream()
                    .map(e -> e.findDirectoriesWithTotalSizeLessThan(maxSize))
                    .flatMap(Collection::stream)
                    .toList());
            return dirs;
        }

        public List<Node> findDirectoriesOrderedByTotalSizeAscending() {
            List<Node> dirs = directories();
            dirs.sort(Comparator.comparingInt(Node::totalSize));
            return dirs;
        }

        private List<Node> directories() {
            List<Node> dirs = new ArrayList<>();
            if (size == 0) {
                dirs.add(this);
                dirs.addAll(children.stream()
                        .filter(e -> e.size == 0)
                        .map(Node::directories)
                        .flatMap(Collection::stream)
                        .toList());
            }
            return dirs;
        }

    }

}

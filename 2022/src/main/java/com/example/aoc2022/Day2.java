package com.example.aoc2022;

import com.example.AocBase;

import java.util.List;

public class Day2 extends AocBase {

    public static void main(String[] args) {
        System.out.println(task1(readFirst(Day2.class)));
        System.out.println(task2(readFirst(Day2.class)));
    }

    private static int task1(List<String> input) {
        int score = 0;
        for (String line : input) {
            String[] round = line.split(" ");
            score += Rps.valueOf(round[1]).score(Rps.valueOf(round[0]));
        }
        return score;
    }

    private static int task2(List<String> input) {
        int score = 0;
        for (String line : input) {
            String[] round = line.split(" ");
            score += Rps.valueOf(round[1]).score2(Rps.valueOf(round[0]));
        }
        return score;
    }

    private enum Rps {
        //ROCK              PAPER               SCISSORS
        X(1), Y(2), Z(3),
        A(0), B(0), C(0);

        private final int partialScore;

        Rps(int partialScore) {
            this.partialScore = partialScore;
        }

        public int score(Rps opponent) {
            return partialScore + roundResult(opponent);
        }

        private int roundResult(Rps opponent) {
            if ((this.equals(X) && opponent.equals(C))
                    || (this.equals(Y) && opponent.equals(A))
                    || (this.equals(Z) && opponent.equals(B))) return 6;
            if ((this.equals(X) && opponent.equals(A))
                    || (this.equals(Y) && opponent.equals(B))
                    || (this.equals(Z) && opponent.equals(C))) return 3;
            return 0;
        }

        public int score2(Rps opponent) {
            int roundResult;
            if(this.equals(X)) { // loose
                roundResult = 0;
                if(opponent.equals(A)) return roundResult + Z.partialScore;
                if(opponent.equals(B)) return roundResult + X.partialScore;
                if(opponent.equals(C)) return roundResult + Y.partialScore;
            }
            if(this.equals(Y)) { // draw
                roundResult = 3;
                if(opponent.equals(A)) return roundResult + X.partialScore;
                if(opponent.equals(B)) return roundResult + Y.partialScore;
                if(opponent.equals(C)) return roundResult + Z.partialScore;
            }
            if(this.equals(Z)) { // win
                roundResult = 6;
                if(opponent.equals(A)) return roundResult + Y.partialScore;
                if(opponent.equals(B)) return roundResult + Z.partialScore;
                if(opponent.equals(C)) return roundResult + X.partialScore;
            }
            return 0;
        }
    }

}

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

class Solution {
    public static void main(String[] args) {
        String path = "input.txt";
        int answer1 = 0, answer2 = 0, value = 0;
        int current = 50;
        try (BufferedReader bfro = new BufferedReader(new FileReader(path))) {
            String st;
            while ((st = bfro.readLine()) != null) {
                String direction = st.substring(0, 1);
                value = Integer.parseInt(st.substring(1));
                answer2 += value / 100;
                value %= 100;

                if (direction.equals("L")) {
                    if (current != 0 && (current - value) <= 0) {
                        answer2 += 1;
                    }
                    current -= value;
                } else {
                    current += value;
                    if (current >= 100) {
                        answer2 += 1;
                    }
                }
                current %= 100;
                if (current < 0) {
                    current += 100;
                }
                if (current == 0) {
                    answer1 += 1;
                }
            }
        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
        }
        System.out.println("Answer 1: " + answer1);
        System.out.println("Answer 2: " + answer2);
    }
}

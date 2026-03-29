import java.util.Random;
import java.util.Scanner;

public class GuessNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random rand = new Random();

        int number = rand.nextInt(100) + 1; // random number between 1-100
        int guess;

        System.out.println("Guess a number between 1 and 100:");

        while (true) {
            System.out.print("Enter your guess: ");
            guess = sc.nextInt();

            if (guess > number) {
                System.out.println("Too high! Try again.");
            } else if (guess < number) {
                System.out.println("Too low! Try again.");
            } else {
                System.out.println("Correct! You guessed the number.");
                break;
            }
        }

        sc.close();
    }
}

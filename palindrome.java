import java.util.Scanner;

public class PalindromeNumber {
    public static void main(String[] args) {
        int number, reversed = 0, remainder, original;

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        number = sc.nextInt();

        original = number;

        while (number != 0) {
            remainder = number % 10;
            reversed = reversed * 10 + remainder;
            number = number / 10;
        }

        if (original == reversed) {
            System.out.println("Palindrome Number");
        } else {
            System.out.println("Not a Palindrome Number");
        }
    }
}

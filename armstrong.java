import java.util.Scanner;

public class ArmstrongNumber {
    public static void main(String[] args) {
        int number, originalNumber, remainder, result = 0;

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        number = sc.nextInt();

        originalNumber = number;

        while (number != 0) {
            remainder = number % 10;
            result = result + remainder * remainder * remainder;
            number = number / 10;
        }

        if (result == originalNumber)
            System.out.println(originalNumber + " is an Armstrong number.");
        else
            System.out.println(originalNumber + " is not an Armstrong number.");
    }
}

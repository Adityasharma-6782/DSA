import java.util.Scanner;

public class maximun_in_TwoNumbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the first Number: ");
        int a = sc.nextInt();
        System.out.print("Enter the second Number: ");
        int b = sc.nextInt();

        String result = (a>b) ? "First is Maximum" : "Second is maximum";
        System.out.println(result);
    }
}

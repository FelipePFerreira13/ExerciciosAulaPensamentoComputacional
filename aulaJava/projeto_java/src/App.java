import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Insira um numero");
        int num = scanner.nextInt();

        System.out.println(num);

        scanner.close();
    }
}

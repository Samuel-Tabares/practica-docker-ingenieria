import java.util.Scanner;

public class Potencia {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("=== CALCULADORA DE POTENCIA EN DOCKER (JAVA) ===");

        try {
            System.out.print("Ingrese la base (b): ");
            double base = scanner.nextDouble();

            System.out.print("Ingrese el exponente entero (e): ");
            int exponente = scanner.nextInt();

            if (exponente < 0) {
                System.out.println("Error: El exponente debe ser no negativo.");
                return;
            }

            double resultado = Math.pow(base, exponente);
            System.out.printf("\nResultado Exitoso: %.2f elevado a la %d es = %.2f\n", base, exponente, resultado);

        } catch (Exception e) {
            System.out.println("Error: Entrada inválida. Intente de nuevo.");
        } finally {
            scanner.close();
        }
    }
}

public class Calculadora{
    public static int calcularArea(int largura, int altura){
        return largura * altura;
    }
    public static double soma(double val1, double val2){
        return val1 + val2;
    }
    public static double subtracao(double val1, double val2){
        return val1 - val2;
    }
    public static double multiplicacao(double val1, double val2){
        return val1 * val2;
    }
    public static double divisao(double val1, double val2){
        double resultado = 0;
        if(val2 != 0){
            resultado = val1 / val2;
        } else System.out.println("O segundo valor precisa ser diferente de 0");
        return resultado;
    }

    public static void main(String[] args){
        System.out.println(soma(1,2));
        System.out.println(subtracao(5,4));
        System.out.println(multiplicacao(1, 8));
        System.out.println(divisao(1, 0));
    }
}
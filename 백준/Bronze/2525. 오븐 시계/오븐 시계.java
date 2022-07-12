import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int a = in.nextInt();
		int b = in.nextInt();
		int c = in.nextInt();
		if(b+c < 60) {System.out.print(a + " "); System.out.print(b + c);}
		else{System.out.print((a + (b+c)/60)%24 + " "); System.out.print((b+c)%60);}
		in.close();
	}
		
}

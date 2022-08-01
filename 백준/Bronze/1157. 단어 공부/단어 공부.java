import java.util.Arrays;
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		String str = in.next();
		String str2 = str.toLowerCase();
		int arr [] = new int[26];
		int arr2 [] = new int[26];
		for(int i = 0; i < str2.length(); i++) {
			int j = str2.charAt(i) - 97;
			arr[j]++;
		}
		for(int i = 0; i < str2.length(); i++) {
			int j = str2.charAt(i) - 97;
			arr2[j]++;
		}

		int max = 0;
		int k = 0;
		int count = 0;

		Arrays.sort(arr2);
		for(int i = 0; i < 26; i++) {
			if(arr2[25] == arr[i]) {count += 1;}
			if(arr[i] > max) {
				k = i;
				max = arr[i];
			}
			
				
		}
		if(count >= 2) {
			System.out.println("?");
		}
		else {System.out.print((char)(k+65));}
	}

}


import java.util.Scanner;
import java.util.Arrays;
import java.util.Comparator;

public class baekjoon_11650{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int i, n = sc.nextInt(), d[][] = new int[n][2];
		for(i=0;i<n;i++) {
			d[i][0] = sc.nextInt();
			d[i][1] = sc.nextInt();
			
		}
		Arrays.sort(d, new Comparator<int []>() {
			public int compare(int a[], int b[]) {
				if (a[0]==b[0]) return Integer.compare(a[1], b[1]);
				else return Integer.compare(a[0], b[0]);
			}
		}) ;
		for(i=0; i<n; i++) {
			System.out.println(d[i][0]+ " " + d[i][1]);
		
		}
		sc.close();
			
		
	}
}
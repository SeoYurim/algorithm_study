import java.util.Scanner;

public class matrixPath {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		
		int[][] c = new int[n+1][n+1];
		int[][] matrix = new int[n+1][n+1];
		
		for(int i=0; i<= n; i++) {
			c[i][0] = 0;
		}
		for(int j=0; j<= n; j++) {
			c[0][j] = 0;
		}
		for(int i =1; i <= n; i++) {
			for(int j=1; j<=n; j++) {
				c[i][j] = matrix[i][j]+Math.max(c[i-1][j], c[i][j-1]);
			}
		}
		System.out.println(c[n][n]);
	}

}

import java.util.Scanner;

public class baekjoon_1890 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		if (n < 4) {
			System.out.println("게임판 크기가 작아");
		}
		int[][] matrix = new int[n+1][n+1];
		long[][] dp = new long[n+1][n+1];
		
		for (int i=1; i<n+1; ++i) {
			for(int j=1; j<n+1; ++j) {
				matrix[i][j] = sc.nextInt();
			}
		}
		
		dp[1][1] = 1;
		
		for(int i=1; i<n+1; i++) {
			for (int j=1; j<n+1; j++) {
				int move = matrix[i][j];
				
				if(dp[i][j]==0 || move==0) {
					continue;
				}
				
				if(i+move < n+1) {
					dp[i+move][j] += dp[i][j];
				}
				if(j+move < n+1) {
					dp[i][j+move] += dp[i][j];
				}
			}
		}
		
		System.out.println(dp[n][n]);
		sc.close();
		
		
		
	}

}

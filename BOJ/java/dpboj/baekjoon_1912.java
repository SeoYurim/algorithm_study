import java.util.Scanner;

public class baekjoon_1912 {
	static int num[], dp[];
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		num = new int[n];
		dp = new int[n];
		
		for (int i=0; i<n; i++) {
			num[i] = sc.nextInt();
		}
		
		dp[0] = num[0];
		int max = dp[0];
		for (int i=1; i<n; i++) {
			dp[i] = Math.max(dp[i-1]+num[i], num[i]);
			max = Math.max(dp[i], max);
		}
		
		System.out.println(max);
		sc.close();
	}

}

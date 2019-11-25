import java.util.Scanner;
import java.util.Arrays;

public class baekjoon_2294 {
	static int coin[], min_num[];
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();
		
		coin = new int[n+1];
		min_num = new int[n+1];
		
		Arrays.sort(coin);
		
		for (int i=1; i<k+2; i++) {
			min_num = new int[100001];
		}
		min_num[0] = 0;
		
		for(int i=0; i<n+1;i++) {
			coin[i] = sc.nextInt();
		}
		
		for (int x=0; x<n+1; x++) {
			for (int y=coin[x]; y<k+1; y++) {
				min_num[y] = Math.min(min_num[y], min_num[y-coin[x]]+1);
			}
		}
		
		if (min_num[k] == 100001){
			min_num[k] = -1;
		}
		
		System.out.println(min_num[-1]);
	}

}

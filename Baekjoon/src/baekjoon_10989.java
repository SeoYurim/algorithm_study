import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;


public class baekjoon_10989{
	
	public static void main(String[] arg) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		int[] number = new int[10001];
		
		for(int i=0; i<N; i++) {
			//number[i] = Integer.parseInt(br.readLine());
			number[Integer.parseInt(br.readLine())]++;
		}
		for(int i =1; i <= 10000; i++) {
			if (number[i]>0) {
				for(int j=0; j<number[i]; j++) {
					bw.write(Integer.toString(i) + "\n");
				}
			}
		}
		
		br.close();
		bw.close();
	}

}
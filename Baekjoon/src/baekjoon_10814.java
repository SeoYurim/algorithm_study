
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class baekjoon_10814 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		String[] members = new String[201];
		Arrays.fill(members, "");
		
		for (int i = 0; i < N; i++) {
			String member = br.readLine();
			members[Integer.parseInt(member.split(" ")[0])] += member + "\n"; 
		}
		
		for (int i = 1; i <= members.length - 1; i++) {
			if(!members[i].equals("")) {
				bw.append(members[i]);
			}
		}
		
		bw.close();
		br.close();
	}
}
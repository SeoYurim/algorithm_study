import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

  public static void main(String[] args) throws Exception {
    // TODO Auto-generated method stub
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(br.readLine());
    int[] arr = new int[10001];
    // 10000000 개이기 때문에 sort를 사용하면 안된다.
    for (int i = 0; i < N; i++) {
      arr[Integer.parseInt(br.readLine())]++;
    }
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    for (int i = 1; i < 10000; i++) {
      if (arr[i] > 0) { // arr[i]가 0보다 작거나 같으면 사용된 횟수가 없기 때문에 패스
        for (int j = 0; j < arr[i]; j++) {
          // 저장된 갯수만큼 출력해줘야 하기 때문에
          bw.write(Integer.toString(i) + "\n");
          // bw.flush(); 가끔 사용안하면 이클립스 Console에 출력이 안됨
        }
      }
    }
    br.close();
    bw.close();
  }

}

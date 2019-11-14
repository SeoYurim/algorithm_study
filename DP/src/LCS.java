import java.util.Scanner;
 
 
public class LCS {
 
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        char [] a = scan.nextLine().toCharArray();
        char [] b = scan.nextLine().toCharArray();
        
        int [][] lcs = new int[a.length+1][b.length+1];
        String [][] solution = new String[a.length+1][b.length+1];
        
        for(int i=1; i<=a.length; i++) {
            for(int j=1; j<=b.length; j++) {
                if(a[i-1]==b[j-1]) {
                    lcs[i][j] = lcs[i-1][j-1]+1;
                    solution[i][j] = "D";
                } else {
                    lcs[i][j] = Math.max(lcs[i-1][j], lcs[i][j-1]);
                    if(lcs[i][j] == lcs[i-1][j]) {
                        solution[i][j] = "U";
                    } else {
                        solution[i][j] = "L";
                    }
                }
            }
        }
        
        int n = a.length;
        int m = b.length;
        StringBuilder sb = new StringBuilder();
        
        while(solution[n][m] != null) {
            if(solution[n][m].equals("D")) {
                sb.append(a[n-1]);
                n--;
                m--;
            } else if(solution[n][m].equals("U")) {
                n--;
            }  else if(solution[n][m].equals("L")) {
                m--;
            } 
        }
        System.out.println(lcs[a.length][b.length]);
        System.out.println(sb.reverse().toString());
    }
 
}

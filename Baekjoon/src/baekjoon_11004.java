//import java.io.BufferedReader;
//import java.io.InputStreamReader;
//import java.util.StringTokenizer;
//
//public class baekjoon_11004 {
//	public static void main(String[] arg) throws Exception {
//		
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		StringTokenizer st = new StringTokenizer(br.readLine());
//		
//		int N = Integer.parseInt(st.nextToken());
//		int K = Integer.parseInt(st.nextToken());
//		
//		int numbers[] = new int[N];
//		
//		st = new StringTokenizer(br.readLine());
//		
//		for(int i=0; i<N; i++) {
//			numbers[i] = Integer.parseInt(st.nextToken());
//		}
//		
//		System.out.println(quickSort(numbers, 0, N-1, K-1));
//	}
//	
//	public static int quickSort(int[] numbers, int start, int end, int k) {
//		int pivot = partition(numbers,start, end);
//		if (pivot ==k) return numbers[pivot];
//	
//		else if (pivot > k) return quickSort(numbers, start, pivot-1,k);
//		
//		else {
//			return quickSort(numbers, pivot+1, end, k-1);
//		}
//		
//	}
//	public static int partition(int[] numbers, int start, int end) {
//		int pivot = numbers[end];
//		int i = start -1;
//		for(int j=start; j<end; j++) {
//			if(numbers[j]< pivot) {
//				i++;
//				swap(numbers, i,j);
//			}
//		}
//		i++;
//		swap(numbers,i,end);
//		
//		return i;
//	}
//	
//	public static void swap(int[] numbers, int x, int y) {
//		int temp = numbers[x];
//		numbers[x] = numbers[y];
//		numbers[y] = temp;
//	}
//}
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon_11004 {
    public static void main(String[] ar) throws Exception{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        
        st = new StringTokenizer(in.readLine());
        int[] arr = new int[N];
        for(int i=0; i<N; i++) {
        	arr[i] = Integer.parseInt(st.nextToken());
        }
        
        System.out.print(quickSearch(arr, 0, N-1, K-1));
    }

    public static int quickSearch(int[] arr, int start, int end, int k){
        int pivot = partition(arr, start, end);
        if(pivot == k) return arr[pivot];
        else if(pivot > k) return quickSearch(arr, start, pivot-1, k);
        else return quickSearch(arr, pivot+1, end, k);
    }

    public static int partition(int[] arr, int start, int end){
        int pivot = arr[end];
        int i = start-1;
        for(int j=start; j<=end; j++){
            if(arr[j] < pivot){
                i++;
                swap(arr, i, j);
            }
        }
        i++;
        swap(arr, i, end);

        return i;
    }

    public static void swap(int[] arr, int a, int b){
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
}
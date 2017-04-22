public class Solution {
    /**
     * @param A: Given an integer array
     * @return: void
     */
    public void siftdown(int[] A, int k){
        while (k * 2 + 1 < A.length){
            int son = k * 2 + 1;
            if (k * 2 + 2 < A.length && A[k * 2 + 2] < A[son])
                son = k * 2 + 2;
            if (A[k] <= A[son])
                break;
            int temp = A[k];
            A[k] = A[son];
            A[son] = temp;
            k = son;
        }
    }

    public void heapify(int[] A) {
        // write your code here
        int n = A.length;
        for (int i = (n - 1) / 2; i >= 0; i--)
            siftdown(A, i);
    }
}
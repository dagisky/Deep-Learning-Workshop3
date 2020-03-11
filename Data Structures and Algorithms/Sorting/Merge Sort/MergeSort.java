package sort;

import java.util.Arrays;

public class MergeSort {
	
	private int[] array;
	public void MergesSort(int[] array) {
		this.array = array;
	}
	
	public int[] getArray() {
		return array;
	}
	
	public void setArray(int[] array) {
		this.array = array;
	}
	
	private int[] merge_sort(int[] arr) {
		int array_len = arr.length;
		if(array_len > 1) {
			int[] left = java.util.Arrays.copyOfRange(arr, 0, array_len/2);
			int[] right = java.util.Arrays.copyOfRange(arr, array_len/2, array_len);
			left = merge_sort(left);
			right = merge_sort(right);
			int i = 0,j = 0,k = 0;
			
			while(i < left.length && j < right.length) {
				if(left[i] <= right[j]) {
					arr[k] = left[i];
					i ++;
				}else {
					arr[k] = right[j];
					j ++;
				}
				k += 1;
			}
			while(i < left.length) {
				arr[k] = left[i];
				i ++; k++;			
			}
			while(j < right.length) {
				arr[k] = right[j];
				j++; k++;
			}
		}	
		return arr;		
	}
	
	public int[] sort() {
		return this.merge_sort(this.array);
	}

}

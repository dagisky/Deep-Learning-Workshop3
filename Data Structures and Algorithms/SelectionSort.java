package sort;

public class SelectionSort {
	int[] array;
	public void SelectionSort(int[] arr) {
		this.array = arr;
	}
	public int[] getArray() {
		return array;
	}
	public void setArray(int[] array) {
		this.array = array;
	}
	
	public int[] sort() {
		int array_length = this.array.length;
		for(int i = 0; i < array_length; i++) {
			int min = this.array[i];
			for(int j = i+1; j < array_length; j++) {
				if(this.array[j] < min) {
					this.array[i] = this.array[j];
					this.array[j] = min;
				}
			}
		}
		return this.array;
	}
	
	
}

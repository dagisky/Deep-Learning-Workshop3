package sort;

public class BubbleSort {
	private int[] array;
	
	public int[] getArray() {
		return array;
	}
	public void setArray(int[] array) {
		this.array = array;
	}
	public void BubbleSort(int []a) {
		this.array = a;
	}
	public int[] sort() {
		for(int i = 0; i < this.array.length; i++) {
			for (int j = 0; j < this.array.length-i-1;j++) {
				if(this.array[j] > this.array[j+1]) {
					int temp = this.array[j];
					this.array[j] = this.array[j+1];
					this.array[j+1] = temp;
				}
			}
		}
		return this.array;
	}
	
}

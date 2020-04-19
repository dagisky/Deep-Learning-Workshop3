package sort;

public class MatrixMul {
	
	public static int[][] NaiveMul(int[][] a, int[][] b){
		assert a[0].length == b.length:"the cols of the first marix must match with the rows of the second";
		int[][] product = new int[a.length][b[0].length];
		for(int i = 0; i<a.length; i++) {
			for(int j = 0; j<b[0].length; j++) {
				for(int k = 0; k < a[0].length; k++) {
					product[i][j] += a[i][k]*b[k][j];
				}
			}
		}
		return product;
	} 

}

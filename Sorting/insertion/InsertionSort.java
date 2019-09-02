package insertion;

import sort.AbstractBase;

/**
 * Class InsertionSort.
 *
 * @author Sanju Sci<sanju.sci9@gmail.com>
 *
 * <p>Complexity in worst case is <b>O(n^2)</b>.</p>
 */
public class InsertionSort extends AbstractBase {
    /**
     * Function sort
     * This function is used to sort array using insertion sort.
     *
     * @param array An array that contains integer input array list.
     * @return Return sorted array list.
     * <p>
     *
     * array[] = {5, 7, 1, 4, 2, 9, 3}
     * 5 7 1 4 2 9 3
     * 1 5 7 4 2 9 3
     * 1 4 5 7 2 9 3
     * 1 2 4 5 7 9 3
     * 1 2 4 5 7 9 3
     * 1 2 3 4 5 7 9
     * */
    public Integer[] sort(Integer array[]){
        int n=array.length, j;
        int value;
        for(int i=1; i<n; i++){
            j = i;
            value = array[i];
            while(j>0 && array[j-1]>value){
                array[j] = array[j-1];
                j--;
            }
            array[j] = value;
        }
        return array;
    }


    @Override
    public <E extends Comparable<E>> E[] genericSort(E[] array) {
        int n=array.length, j;
        E value;
        for(int i=1; i<n; i++){
            j = i;
            value = array[i];
            while(j>0 && array[j-1].compareTo(value)>0) {
                array[j] = array[j-1];
                j--;
            }
            array[j] = value;
        }
        return array;
    }

}
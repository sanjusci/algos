package selection;

import sort.AbstractBase;

/**
 * Class SelectionSort.
 *
 * @author Sanju Sci<sanju.sci9@gmail.com>
 *
 * <p>Complexity in worst case is <b>O(n^2)</b>.</p>
 */
public class SelectionSort extends AbstractBase {
    /**
     * Function sort
     * This function is used to sort array using bubble sort.
     *
     * @param array An array that contains integer input array list.
     * @return Return sorted array list.
     * <p>
     * array[] = {5, 7, 1, 4, 2, 9, 3}
     * 1 4 2 5 3 7 9
     * 1 2 4 3 5 7 9
     * 1 2 3 4 5 7 9
     * 1 2 3 4 5 7 9
     * 1 2 3 4 5 7 9
     * 1 2 3 4 5 7 9
     */

    public Integer[] sort(Integer array[]){
        int n = array.length, temp, imin;
        for(int i=0; i<(n-1); i++){
            imin = i;
            for(int j=i+1; j<n; j++){
                if(array[j]<array[imin]){
                    imin = j;
                }
            }
            temp = array[i];
            array[i] = array[imin];
            array[imin] = temp;
        }
        return array;
    }

    @Override
    public <E extends Comparable<E>> E[] genericSort(E array[]){
        int n = array.length, imin;
        E temp;
        for(int i=0; i<(n-1); i++){
            imin=i;
            for(int j=i+1; j<n; j++){
                if(array[j].compareTo(array[imin])<0) {
                    imin = j;
                }
            }
            temp = array[i];
            array[i] = array[imin];
            array[imin] = temp;
        }
        return array;
    }

}
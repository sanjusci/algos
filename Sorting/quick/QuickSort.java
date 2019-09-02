package quick;

import sort.AbstractBase;

/**
 * Class QuickSort.
 *
 * @author Sanju Sci<sanju.sci9@gmail.com>
 *
 * <p>Complexity in average case is <b>O(nlog(n))</b>.
 * </p> <p>Complexity in worst case is <b>O(n^2)</b>.</p>
 */
public class QuickSort extends AbstractBase {

    /**
     * Function sort
     * This function is used to sort array using quick sort.
     *
     * @param array An array that contains integer input array list.
     * @param start the start
     * @param end   the end
     *
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

    public Integer[] sort(Integer array[], int start, int end){
        if(start<end){
            int pIndex = partition(array, start, end);
            sort(array, start, pIndex-1);
            sort(array, pIndex+1, end);
        }
        return array;
    }

    /**
     * Function partition
     * This function is used to partition of given array.
     *
     * @param array An array that contains integer input array list.
     * @param start the start
     * @param end   the end
     * @return Return partition index. <p>
     */
    public int partition(Integer array[], int start, int end){
        /**
         All the elements <= pivot will be at the left of pIndex.
         */
        int pIndex=start;
        int pivot = array[end], temp;
        for(int i=start; i<end; i++){
            if(array[i]<=pivot){
                // Swap array[pIndex] and current element.
                temp = array[pIndex];
                array[pIndex] = array[i];
                array[i] = temp;
                pIndex++;
            }
        }
        // Swap pivot(array[end]) and array[pIndex]
        temp = array[pIndex];
        array[pIndex] = array[end];
        array[end] = temp;
        return pIndex;
    }

    public <E extends Comparable<E>> E[] genericSort(E[] array, int start, int end) {
        if(start<end) {
            int pIndex = partition(array, start, end);
            genericSort(array, start, pIndex-1);
            genericSort(array, pIndex+1, end);
        }
        return array;
    }

    /**
     * Partition int.
     *
     * @param <E>   the type parameter
     * @param array the array
     * @param start the start
     * @param end   the end
     * @return the int
     */
    public <E extends Comparable<E>> int partition(E[] array, int start, int end) {
        int pIndex = start;
        E pivot = array[end], temp;
        for(int i=start; i<end; i++){
            if(array[i].compareTo(pivot)<=0){
                // Swap array[pIndex] and current element.
                temp = array[i];
                array[i] = array[pIndex];
                array[pIndex] = temp;
                pIndex++;
            }
        }
        // Swap pivot(array[end]) and array[pIndex]
        temp = array[pIndex];
        array[pIndex] = array[end];
        array[end] = temp;
        return pIndex;
    }

}

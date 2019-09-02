package merge;

import java.util.Arrays;

import sort.AbstractBase;

/**
 * Class QuickSort.
 *
 * @author Sanju Sci<sanju.sci9@gmail.com>
 *
 * <p>Complexity in worst case is <b>O(nlog(n))</b>.</p>
 */
public class MergeSort extends AbstractBase  {
    /**
     * Sort integer [ ].
     *
     * @param array the array
     * @return the integer [ ]
     */
/*
    array[] = {5, 7, 1, 4, 2, 9, 3}
    */
    public Integer[] sort(Integer array[]){
        int n=array.length, i, j;
        int mid = n/2;
        Integer left[] = new Integer[mid];
        Integer right[] = new Integer[n-mid];

        for(i=0; i<mid; i++){
            left[i] = array[i];
        }
        for(j=mid; j<n; j++){
            right[j-mid] = array[j];
        }

        if(n<2){
            return array;
        } else{
            sort(left);
            sort(right);
            array = merge(left, right, array);
            left=right=null;
            return array;
        }
    }

    private Integer[] merge(Integer left[], Integer right[], Integer array[]){
        int iL=0, iR=0, iA=0;
        int nL = left.length, nR = right.length;
        while(iL<nL && iR<nR){
            if(left[iL]<=right[iR]){
                array[iA] = left[iL];
                iL++;
            } else {
                array[iA] = right[iR];
                iR++;
            }
            iA++;
        }

        while(iL<nL){
            array[iA] = left[iL];
            iL++;
            iA++;
        }
        while(iR<nR){
            array[iA] = right[iR];
            iR++;
            iA++;
        }
        return array;
    }

    @Override
    public <E extends Comparable<E>> E[] genericSort(E[] array) {
        int n=array.length;
        int mid = n/2;
        E[] left = Arrays.copyOfRange(array, 0, mid);
        E[] right = Arrays.copyOfRange(array, mid, n);
        if(n<2){
            return array;
        } else{
            genericSort(left);
            genericSort(right);
            array = merge(left, right, array);
            left=right=null;
            return array;
        }
    }

    /**
     * Merge e [ ].
     *
     * @param <E>   the type parameter
     * @param left  the left
     * @param right the right
     * @param array the array
     * @return the e [ ]
     */

    public <E extends Comparable<E>> E[] merge(E left[], E right[], E array[]) {
        int nL = left.length, nR = right.length;
        int iL = 0,iR = 0, iA=0;
        while(iL<nL && iR<nR){
            if( (left[iL].compareTo(right[iR])) <=0){
                array[iA] = left[iL];
                iL++;
            } else{
                array[iA] = right[iR];
                iR++;
            }
            iA++;
        }

        while(iL<nL){
            array[iA] = left[iL];
            iL++;
            iA++;
        }

        while(iR<nR){
            array[iA] = right[iR];
            iR++;
            iA++;
        }

        return array;
    }

}
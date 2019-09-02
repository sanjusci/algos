package sort;


import bubble.BubbleSort;


public class SortMain {
    public static void main(String[] args) {

        AbstractBase base = new BubbleSort();
        BubbleSort bs = (BubbleSort) base;

        Integer arrayInteger[] = {5, 7, 1, 4, 2, 9, 3};
        long startTime = System.nanoTime();
        arrayInteger = bs.basicBubbleSort(arrayInteger);
        long endTime   = System.nanoTime();
        base.printArray(arrayInteger);
        long total_time = endTime - startTime;
        System.out.println("Sorting Time: " + total_time);


        long startTime2 = System.nanoTime();
        arrayInteger = bs.optimizedBubbleSort(arrayInteger);
        base.printArray(arrayInteger);
        long endTime2 = System.nanoTime();
        long total_time2 = endTime2 - startTime2;
        System.out.println("Sorting Time: " + total_time2);

        String arrayString[] = {"Kuldeep", "Pramod", "Vijay", "Sanju", "Diwaker", "Rajkamal", "Omprakash", "Suyash"};

        long startTime3 = System.nanoTime();
        arrayString = base.genericSort(arrayString);
        base.printArray(arrayString);
        long endTime3 = System.nanoTime();
        long total_time3 = endTime3 - startTime3;
        System.out.println("Sorting Time: " + total_time3);
    }
}

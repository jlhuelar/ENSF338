int binarySearch (int [] arr, int first, int last, int key) {
    if(first <= last){
        int mid = (first + last)/2;
        if(key == arr[mid])
            return mid; // success: key found
        else if (key < arr[mid])
            return binarySearch(arr, first, mid-1, key);
        else if (key > arr[mid])
            return binarySearch(arr, mid+1, last, key);
    }
    return -1; // failure: key not found
}
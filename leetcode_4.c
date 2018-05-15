double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int median1;
    int median2;

    if (nums1Size == 0){
        if (nums2Size%2 == 0){
            return (nums2[nums2Size/2 -1] + nums2[nums2Size/2])/2;
        }else{
            return nums2[nums2Size/2];
        }
    }

     if (nums2Size == 0){
        if (nums1Size%2 == 0){
            return (nums1[nums1Size/2 -1] + nums1[nums1Size/2])/2;
        }else{
            return nums1[nums1Size/2];
        }
    }

    median1 = nums1[nums1Size/2];
    median2 = nums2[nums2Size/2];

    if ( median1 == median2){
        return median2;
    }

    if (median1 < median2){

    }


    while (nums1Size != 0 || nums2Size != 0){

    }


}

int main() {
    int nums1=[1,2]
    int nums2=[3,4]
    printf(findMedianSortedArrays(nums1, sizeof(nums1)/sizeof(nums1[0]), nums2, sizeof(nums2)/sizeof(nums2[0])))
}
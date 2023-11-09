#include "bits/stdc++.h"

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int i = 0, p = (nums.size() - 1);
        int index_to_find = nums.size() - k;
        quickSelect(nums, i, p, index_to_find);
        return nums[index_to_find];
    }
    
    void quickSelect(vector<int>&nums, int i, int p, int &k){
        if(i < p){
            int equal_pivot = 0;
            int partition_idx = partitionIndex(nums, i, p, equal_pivot);

            if((partition_idx == k) || (k <= partition_idx && k >= partition_idx - equal_pivot)){
                if(k <= partition_idx && k >= partition_idx - equal_pivot)
                {
                     k = partition_idx;
                     cout << "early return" << endl;
                }
                return;
            } else if(k < partition_idx){
                return quickSelect(nums, i, partition_idx - 1, k);
            } else{
                return quickSelect(nums, partition_idx + 1, p, k);
            }
        }  
    }

    int partitionIndex(vector<int> &nums, int left, int right, int &equal_pivot){
        /* randomize the selection of the pivot element to mitigate worst case scenario*/
        srand(time(NULL));
        int pivot_index = left + rand() % (right - left);
        swap(nums, pivot_index, right);
        int pivot_element = nums[right];
        int partition_idx = left;
        int j = left;

        while(j < right){
            if(nums[j] <= pivot_element){
                /* swap partition_idx and j and advance both pointers*/
                swap(nums, partition_idx,j );
                partition_idx ++;
            } else if(nums[j] == pivot_element){
                equal_pivot++;
            }
            j++;
        }
        swap(nums, right, partition_idx);
        return partition_idx;
    } 

    void swap(vector<int> &nums, int index1, int index2){
        int temp = nums[index1];
        nums[index1] = nums[index2];
        nums[index2] = temp;
    } 

};

int main(){
    Solution instance;
    vector<int> array = {3,2,1,5,6,4};
    int k = 2;
    cout << instance.findKthLargest(array, k) << endl;;
}
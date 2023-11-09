#include "bits/stdc++.h"
#include "iostream"


using namespace std;

class Solution {
public:
    std::vector<int> searchRange(std::vector<int>& nums, int target) {
        std::vector<int> solution = {-1, -1};

        if (nums.empty()) return solution;

        int start = 0;
        int end = nums.size() - 1;

        int found_index = binSearch(nums, start, end, target);

        if (found_index == std::numeric_limits<int>::max()) return solution;

        int left_index = binTraverseLeft(nums, start, found_index - 1, target, found_index);
        int right_index = binTraverseRight(nums, found_index + 1, end, target, found_index);

        solution[0] = (left_index == std::numeric_limits<int>::max()) ? found_index : left_index;
        solution[1] = (right_index == std::numeric_limits<int>::max()) ? found_index : right_index;

        return solution;
    }

    int binSearch(std::vector<int>& nums, int start, int end, int target) {
        while (start <= end) {
            int mid_index = start + (end - start) / 2;
            if (nums[mid_index] == target) {
                return mid_index;
            } else if (nums[mid_index] > target) {
                end = mid_index - 1;
            } else {
                start = mid_index + 1;
            }
        }
        return std::numeric_limits<int>::max();
    }

    int binTraverseLeft(std::vector<int>& nums, int start, int end, int target, int min_left) {
        while (start <= end) {
            int mid_index = start + (end - start) / 2;
            if (nums[mid_index] == target) {
                min_left = mid_index;
                end = mid_index - 1;
            } else {
                start = mid_index + 1;
            }
        }
        return min_left;
    }

    int binTraverseRight(std::vector<int>& nums, int start, int end, int target, int max_right) {
        while (start <= end) {
            int mid_index = start + (end - start) / 2;
            if (nums[mid_index] == target) {
                max_right = mid_index;
                start = mid_index + 1;
            } else {
                end = mid_index - 1;
            }
        }
        return max_right;
    }
};

int printVector(vector<int> & vec){
    if (!vec.empty()){
        cout << "\n[";
        for (vector<int>::iterator it = vec.begin(); it != vec.end(); it++){
            cout << *it << ",";
        }
        cout << "]" << endl;
        return vec.size();
    }
    else{
        cout<< "the vector is empty"<<endl;
        return -1;
    }
}

int main(){
    Solution instance;
    vector<int> questionVector = {5,7,7,8,8,10};
    int target = 8;
    auto output = instance.searchRange(questionVector, 8);

    printVector(output);

}
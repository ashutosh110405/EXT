#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        // If the array has only 1 element, we are already at the end.
        if (nums.size() <= 1) return 0;
        
        int jumps = 0;
        int current_jump_end = 0;
        int farthest_reachable = 0;
        
        // We iterate up to the second to last element, 
        // because once we are at the last element, we don't need to jump again.
        for (int i = 0; i < nums.size() - 1; ++i) {
            // Update the farthest index we can reach from the current position
            farthest_reachable = max(farthest_reachable, i + nums[i]);
            
            // If we have reached the end of the current jump boundary,
            // we must make another jump.
            if (i == current_jump_end) {
                jumps++;
                current_jump_end = farthest_reachable;
                
                // Early exit: if our current jump can already reach or pass the end
                if (current_jump_end >= nums.size() - 1) {
                    break;
                }
            }
        }
        
        return jumps;
    }
};
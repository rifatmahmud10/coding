#include <iostream>
using namespace std;
#include <vector>

vector<int> twoSum(vector<int> &nums, int target)
{
    int n = nums.size();

    for (int i = 0; i < n - 1; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (nums[i] + nums[j] == target)
            {
                return {i, j};
            }
        }
    }
    return {};
}

int main()
{
    int target;
    vector<int> nums;
    cout << "Enter traget:" << endl;
    cin >> target;
    cout << "enter the numbers:" << endl;
    int num;
    while (cin >> num && num != -1)
    {
        nums.push_back(num);
    }

    vector<int> result = twoSum(nums, target);

    if (!result.empty())
    {
        cout << "Indices: ";
        for (int index : result)
        {
            cout << index << " ";
        }
        cout << endl;
    }
    else
    {
        cout << "No solution found!" << endl;
    }
};
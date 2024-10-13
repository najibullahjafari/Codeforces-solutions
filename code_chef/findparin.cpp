#include (stdio.h);


void findPair(int nums[], int n, int sum) {
    int i, j;
    for (i = 0; i < n; i++) {
        for (j = i + 1; j < n; j++) {
            if (nums[i] + nums[j] == sum) {
                printf("Pair found at index %d and %d\n", i, j);
                return;
            }
        }
    }
    printf("Pair not found\n");
}
int main(void){
    int t;
    while(t--){
        int n;
        scanf("%d", &n);
        int nums[n];
        for(int i = 0; i < n; i++){
            scanf("%d", &nums[i]);
        }
        int sum;
        scanf("%d", &sum);
        findPair(nums, n, sum);
    }


}
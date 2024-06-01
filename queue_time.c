#include <stdio.h>
#include <stdlib.h>

int queue_time(int *customers, int num_customers, int num_tills) {
    int *tills = (int*)malloc(sizeof(int) * num_tills);
    if (tills == NULL) {
        printf("Memory allocation failed.\n");
        exit(1);
    }

    for (int i = 0; i < num_tills; i++) {
        tills[i] = 0;
    }

    for (int i = 0; i < num_customers; i++) {
        tills[0] += customers[i];
        for (int j = 0; j < num_tills - 1; j++) {
            if (tills[j] > tills[j + 1]) {
                int temp = tills[j];
                tills[j] = tills[j + 1];
                tills[j + 1] = temp;
            }
        }
    }

    int max_time = tills[0];
    free(tills);
    return max_time;
}

int queue_time_optimized(int *customers, int num_customers, int num_tills) {
    int *tills = (int*)malloc(sizeof(int) * num_tills);
    if (tills == NULL) {
        printf("Memory allocation failed.\n");
        exit(1);
    }

    for (int i = 0; i < num_tills; i++) {
        tills[i] = 0;
    }

    for (int i = 0; i < num_customers; i++) {
        int min_index = 0;
        for (int j = 1; j < num_tills; j++) {
            if (tills[j] < tills[min_index]) {
                min_index = j;
            }
        }
        tills[min_index] += customers[i];
    }

    int max_time = tills[0];
    for (int i = 1; i < num_tills; i++) {
        if (tills[i] > max_time) {
            max_time = tills[i];
        }
    }
    free(tills);
    return max_time;
}
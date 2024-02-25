#include <stdio.h>
#include <math.h>

#define NUM_POINTS 1000

int main() {
    double resonant_frequency = 150e3;  // 150 kHz
    double bandwidth = 600.0;  // in Hz
    double frequency_range[NUM_POINTS];
    double magnitude_response[NUM_POINTS];

    // Generate frequency range around the resonant frequency
    for (int i = 0; i < NUM_POINTS; i++) {
        frequency_range[i] = resonant_frequency - bandwidth/2 + (i * bandwidth / (NUM_POINTS - 1));
        magnitude_response[i] = exp(-pow((frequency_range[i] - resonant_frequency) / (bandwidth / 2), 2));
    }

    // Save coordinates to data.txt
    FILE *fp;
    fp = fopen("data.txt", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }
    for (int i = 0; i < NUM_POINTS; i++) {
        fprintf(fp, "%.6f %.6f\n", frequency_range[i], magnitude_response[i]);
    }
    fclose(fp);

    return 0;
}


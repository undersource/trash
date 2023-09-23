#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <float.h>
#include <errno.h>


float fahrenheit_to_celsius(float fahrenheit) {
    float celsius;
    celsius = (fahrenheit - 32.0) / 1.8;

    return celsius;
}


float celsius_to_fahrenheit(float celsius) {
    float fahrenheit;
    fahrenheit = celsius * 1.8 + 32.0;

    return fahrenheit;
}


int help() {
    printf(
            "Usage: [OPTION] [VALUE]\n\n"
            "Options:\n"
            "  -c        convert fahrenheit to celsius\n"
            "  -f        convert celsius to fahrenheit\n"
    );

    return 1;
}


int main(int argc, char *argv[]) {
    if (argc != 3) {
        help();
    } else {
        const char *option;
        char *ptr;
        float value;

        errno = 0;

        option = argv[1];

        double conv = strtod(argv[2], &ptr);

        if (errno != 0 || *ptr != '\0' || conv > DBL_MAX || conv < DBL_MIN) {
            printf("Invalid value\n");
            return 1;
        } else {
            value = conv;
        }

        if (strcmp(option, "-f")) {
            printf("%f\n", fahrenheit_to_celsius(value));
        } else if (strcmp(option, "-c")) {
            printf("%f\n", celsius_to_fahrenheit(value));
        } else {
            help();
        }
    }
}

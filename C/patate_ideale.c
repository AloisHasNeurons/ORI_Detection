#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>
#include <time.h>


//open the file "Borrelia_burgdorferi_B31_complete_genome.txt" and read the data into a string called "data"
char open_file(char *filename, char *data)
{
    FILE *file = fopen(filename, "r");
    if (file == NULL)
    {
        printf("Error opening file!\n");
        return 1;
    }
    fseek(file, 0, SEEK_END);
    long fsize = ftell(file);
    fseek(file, 0, SEEK_SET);
    fread(data, 1, fsize, file);
    fclose(file);
    return 0;
}

int main()
{
    char data[100000];
    open_file("Borrelia_burgdorferi_B31_complete_genome.txt", data);
    printf("%s", data);
    return 0;
}

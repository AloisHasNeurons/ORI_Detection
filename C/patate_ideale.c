#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>
#include <time.h>
#include "fonctions.c"

int main()
{
    FILE *fichier = NULL;
    FILE* test = NULL;
    char *sequence;
    char* new_sequence;
    int caracteres_first_ligne;
    int caracteres;
    int nb_lignes;
    fichier = fopen("C:\\Users\\madgu\\OneDrive\\Cours-L1-Evry\\Bloc Complementaire\\Demarche_scientifique_projet\\La-patate-ideale\\La-patate-ideale\\Sequence\\Borrelia_burgdorferi_B31_complete_genome.txt", "r");
    test = fopen("C:\\Users\\madgu\\OneDrive\\Cours-L1-Evry\\Bloc Complementaire\\Demarche_scientifique_projet\\La-patate-ideale\\La-patate-ideale\\Sequence\\test.txt", "w");
    if (fichier != NULL)
    {
        nb_lignes = cpt_lignes(fichier);
        printf("%d\n", nb_lignes);
        rewind(fichier);
        caracteres = cpt_caracteres(fichier);
        printf("%d\n", caracteres);
        rewind(fichier);
        caracteres_first_ligne = cpt_caracteres_first_ligne(fichier);
        fseek(fichier, caracteres_first_ligne+2, SEEK_SET);
        sequence = malloc(caracteres-caracteres_first_ligne * sizeof(char));
        fread(sequence, sizeof(char), caracteres-caracteres_first_ligne, fichier);
        fputs(sequence, test);
        fclose(fichier);
        fclose(test);
    }
    else
    {
        printf("Erreur d'ouverture du fichier");
    }
    return 0;
}

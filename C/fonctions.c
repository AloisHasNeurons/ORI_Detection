int cpt_lignes(FILE *fichier)
{
    int c;
    int nLignes = 0;
    int c2 = '\0';
    while ((c = fgetc(fichier)) != EOF)
    {
        if (c == '\n')
            nLignes++;
        c2 = c;
    }
    /* Ici, c2 est égal au caractère juste avant le EOF. */
    if (c2 != '\n')
    {
        nLignes++;
    }
    return nLignes;
}
int cpt_caracteres(FILE *fichier)
{
    int nCaracteres = 0;
    while (fgetc(fichier) != EOF)
    {
        nCaracteres++;
    }
    return nCaracteres;
}
int cpt_caracteres_first_ligne ( FILE *fichier )
{
    int nCaracteres = 0;
    int c;
    while ((c = fgetc(fichier)) != '\n')
    {
        nCaracteres++;
    }
    return nCaracteres;
}
char* supp_retourchariot(char* chaine)
{
    int i = 0;
    strlen(chaine);
    for (i = 0; i < strlen(chaine); i++)
    {
        if (chaine[i] == '\n')
        {
            chaine[i] = '\0';
        }
    }
    return chaine;
}
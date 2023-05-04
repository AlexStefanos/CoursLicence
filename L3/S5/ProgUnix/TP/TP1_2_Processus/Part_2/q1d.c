#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(int argc, char **argv, char **arge) {
    char dir[200];
    char *d;
    mode_t mode;
    int fd;
    
    printf("--------------------------------------------------Avant exec--------------------------------------------------\n");
    printf("Mon pid:\t\t%d\n", getpid());
    printf("Le pid de mon père :\t%d\n", getppid());
    printf("Mon UID réel :\t\t%d\n", getuid());
    printf("Mon UID effectif :\t\t%d\n", geteuid());
    printf("Mon GID réel :\t\t%d\n", getgid());
    printf("Mon GID effectif :\t\t%d\n", getegid());
    mode = umask(mode); //Retourne le masque actuel et le modifie
    printf("Mon masque(octal) :\t%o\n", mode);
    mode = umask(mode); // Restauration du masque
    d = getcwd(dir, 200);
    if(d != NULL)
        printf("Mon répertoire courant :\t%s\n", dir);
    else
        perror(dir);
    /* Pas dans le corrigé
    printf("Ouverture d'un fichier avec le flag FD_CL0EXEC\n");
    fd = open("Ouverture d'un fichier sans le flag FD_CLO0EXEC\n");
    if(fd < 0)
      perror("Open");*/
    execl("apres_exec" "apres-exec", NULL);
    perror("apres_exec");
    exit(EXIT_SUCCESS);
}

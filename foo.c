
    #include <stdlib.h>
    #include <stdio.h>
    #include <dlfcn.h>


    int main(int argc, char **argv) {
        void *handle;
        double (*cosine)(int);
        int (*fooz)(int a);
        char *error;

        handle = dlopen ("lang_protocol.dylib", RTLD_LAZY);
        if (!handle) {
            fputs (dlerror(), stderr);
            exit(1);
        }

        fooz = dlsym(handle, "fooz");
        if ((error = dlerror()) != NULL)  {
            fputs(error, stderr);
            exit(1);
        }
        printf("Enter an integer: \n");

        printf ("%d\n", (*fooz)(5));
        dlclose(handle);
    }
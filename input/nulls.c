#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv)
{

  char *envi[100];

  envi[0] = "./input";
  for (int i=1; i < 100; i++)
  {
    if (i == 65)
      envi[i] = "BB";
    else
      envi[i] = "AA";
  }

  for (int i = 0; i < 100; i++)
    printf(envi[i]);

  execve(envi[0], envi, NULL);

  return 0;
}

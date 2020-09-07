#include <stdio.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#define PW_LEN 10
#define XORKEY 1

void xor(char *s, int len)
{
  int i;
  for (i=0; i<len; i++)
    s[i] ^= XORKEY;
}

void pxor(char *s)
{
  printf("Your xor'd password is: %s\n",s);
  printf("In hex:");
  for (int i=0; i<PW_LEN; i++)
    printf("%x", s[i]);
  printf("\n");

}

int main(int argc, char **argv)
{

  char pw_buf[PW_LEN+1];
  printf("input password: ");
  scanf("%10s", pw_buf);

  xor(pw_buf, 10);
  pxor(pw_buf);

  char password[PW_LEN+1] = {'A','B','C','D','E','F','G','H','I','\0'};
  int cmp;
  if (!(cmp=strncmp(password, pw_buf, PW_LEN)))
  {
    printf("Passwords match.\n");
  }
  else
  {
    printf("Passwords do not match.\n");
  }

  return 0;
}

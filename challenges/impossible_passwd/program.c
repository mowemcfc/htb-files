#include <stdlib.h>
#include <stdio.h>
void main()

{
  int local_14;
  char* local_10;
  
  local_14 = 0;
  local_10 = "A]Kr=9k0=0o0;k1?k81t";  
  while ((*local_10 != 9 && (local_14 < 0x14))) {
    putchar((int)(char)(*local_10 ^ 9));
    local_10 = local_10 + 1;
    local_14 = local_14 + 1;
  }
  putchar(10);
  return;
}

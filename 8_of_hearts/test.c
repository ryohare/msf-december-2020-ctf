#include <stdio.h>
#include <string.h>

int main(void)
{
  int iVar1;
  size_t sVar2;
  char local_7f9;
  char local_7f8 [1008];
  char local_408 [1000];
  FILE *local_20;
  FILE *local_18;
  int local_10;
  int local_c;
  
  local_c = 0;
  memset(local_408,0,1000);
  memset(local_7f8,0,1000);
  fgets(local_7f8,2000,stdin);
  iVar1 = strncmp("buffalo",local_7f8,7);
  if (iVar1 == 0) {
    local_10 = 0;
    while (local_10 < 0x3e2) {
      iVar1 = 0;//strncmp("buffalo",local_408 + local_10,7);
      if (iVar1 == 0) {
        local_c = 1;
        local_18 = fopen("8_of_hearts.enc","rb");
        local_20 = fopen("8_of_hearts.png","wb");
        while( 1 ) {
          sVar2 = fread(&local_7f9,1,1,local_18);
          if (sVar2 != 1) break;
          fputc((int)(char)(local_7f9 ^ 0x41),local_20);
        }
        fclose(local_18);
        fclose(local_20);
      }
      local_10 = local_10 + 1;
    }
    if (local_c == 0) {
      puts("MOAR buffalo!");
    }
  }
  else {
    puts("You did not say buffalo!");
  }
  return 0;
}	

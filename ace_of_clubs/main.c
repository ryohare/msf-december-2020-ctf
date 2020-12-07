/* decompiled from ghidra*/
int main(int argc,char **argv)

{
  long lVar1;
  bool bVar2;
  bool bVar3;
  int iVar4;
  int iVar5;
  long in_FS_OFFSET;
  int user_ent;
  int pass_ent;
  int auth_stat;
  int opt;
  int fp;
  char *log_name;
  char *user;
  char *pass;
  char conn_msg [200];
  
  lVar1 = *(long *)(in_FS_OFFSET + 0x28);
  bVar2 = false;
  bVar3 = false;
  log_name = (char *)0x0;
  if (argc == 1) {
    print_usage();
  }
  while (iVar4 = getopt(argc,argv,"u:p:l:"), iVar4 != -1) {
    if (iVar4 == 0x6c) {
      log_name = optarg;
    }
    else {
      if (iVar4 < 0x6d) {
        if (iVar4 == 0x3f) {
          print_usage();
        }
      }
      else {
        if (iVar4 == 0x70) {
          pass = optarg;
          bVar3 = true;
        }
        else {
          if (iVar4 == 0x75) {
            user = optarg;
            bVar2 = true;
          }
        }
      }
    }
  }
  if ((!bVar2) || (!bVar3)) {
    print_usage();
  }
  if (log_name == (char *)0x0) {
    log_name = "./logs/logfile";
  }
  umask(0);
  iVar4 = open(log_name,0x41,0x1fc);
  if (iVar4 == -1) {
    puts("File could not be opened for writing.");
    iVar4 = 1;
  }
  else {
    printf("Logging to %s\n",log_name);
    snprintf(conn_msg,200,"Attempting to connect to server with %s and %s\n",user,pass);
    log_res(iVar4,conn_msg);
    log_res(iVar4,"Connection handled\n");
    iVar5 = authenticate(user,pass,pass);
    if (iVar5 == 1) {
      log_res(iVar4,"Authentication successful\n");
    }
    else {
      log_res(iVar4,"Authentication failed\n");
    }
    close(iVar4);
    iVar4 = 0;
  }
  if (lVar1 == *(long *)(in_FS_OFFSET + 0x28)) {
    return iVar4;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}



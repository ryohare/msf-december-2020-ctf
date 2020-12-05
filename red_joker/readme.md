Port 9007

The home page had a singe zip file which fails to unzip with the standard `unzip` binary. Doing some [googling](https://askubuntu.com/questions/54904/unzip-error-end-of-central-directory-signature-not-found) it was discovered that java has an unzip feature for jars (which are really just zip files of classes) which seemed to work just fine.

`jar xvf red_joker.zip`

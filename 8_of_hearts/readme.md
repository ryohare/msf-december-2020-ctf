From strings:

buffalo
You did not say buffalo!
8_of_hearts.enc
8_of_hearts.png
MOAR buffalo!

Put this into ghidra to see WTF is going on. Saw the decompile C code and tried to give it continuous input of buffalo as it appeared to want however seemed get something wrong becauer I got the MOAR buffalo branch.

So I decided to test in C to figure out the string. Then, looming at the src code, I noticed that it has no nested local functions, only libs. So, I copied and pasted it into the C file, fixed some compile errors and it worked. So I stubbed out the check, ran it and got the decrytped file.

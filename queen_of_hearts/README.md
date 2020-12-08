This one has a java server reading java serialized objects on port 9008. Port 9010 is serving a java client or integrating with this service. The service requires an authetnication event which would allow the dowload of the flag. Perhaps, there is more to the authentication bypass in doing something for RCE with ysoserial to bet something like a reverse shell.

Initial attempts where focused around bypassing client side controls. This was done in 2 ways.

1. Manually patching the jar file with byte code to remove a return statement on authentication failures with a noop. This didnt work however
```bash
jar xf QOA_Client.jar

# use open source [java byte code](https://www.talksinfo.com/how-to-edit-class-file-from-a-jar/) editor to insert a noop in the return on auth failure. Source code was discovered using jd-gui then mapped to the byte code in java byte code editor.

jar cmvf META-INF/MANIFEST.MF qoh2.jar AuthState.class Client.class

# this and this worked however it was discovered that the auth is stateful server side, not just client side via wireshark captures.
```

State Machine server side it seems.

Not Connected --[connect event]--> Connected --[Auth Pass]--> Authenticated --[download]--> !get file!
					       [Auth Fail]--> Not Auth --[go to Connected]	

So, we need to get an auth bypass with no knowledge of the server side decision making. We do know we are sending the AuthState java object which we can get the definition from via jd-gui. Thus, we can probably, using ysoserial, create a payload we can send which will either bypass the authentication or create an RCE event to get  a shell or to pull the file.

Link for follow up research: https://medium.com/bugbountywriteup/a-comprehensive-guide-to-java-serialization-vulnerability-18fad6e37b64

A good lab for this is deserlab.



Target: 8202

Heading to this site, it was a login screen. After looking at the network traffic in firefox, it looked like a graphql API. Some research [here](https://the-bilal-rizwan.medium.com/graphql-common-vulnerabilities-how-to-exploit-them-464f9fdce696) found the steps to get the info. 

Used burp to proxy the traffic and sent some sample queries to repeater. First step was to get the schema via instrospection and visualize it. It showed the users table and posts table. Modifying the query allowed the disclosure of data in the users table which had one user, Admin. So, the next thought, is maybe there is some data in the posts table which can reveal the password. Querying this table revealed the link to the queen of spades pictuer.

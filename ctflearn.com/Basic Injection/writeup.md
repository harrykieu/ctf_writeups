# Basic Injection
## Requirement
Using SQL Injections to get the flag
## Solution
- Go to the provided website, we can see that it's a simple website that take input - a name from user and make a query.

- Try to inject simple payload - `noah' or '1' = '1`, we get all the contents of database with the flag inside:  

=> Flag: `CTFlearn{th4t_is_why_you_n33d_to_sanitiz3_inputs}` 

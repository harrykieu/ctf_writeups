# Basic Injection

* Go to the provided website, we can see that it's a simple website that takes an input - a name from user and makes a query.\
  ![Screenshot\_2022-09-18\_10\_48\_49](https://user-images.githubusercontent.com/89294020/190885443-224cb4e6-9ab6-4fd5-a427-15ab708e5cf3.png)
* When we try to inject simple SQLi payload - `noah' or '1' = '1`, we get all the contents of the database with the flag inside:\
  ![Screenshot 2022-09-18 111350](https://user-images.githubusercontent.com/89294020/190885475-5d31ee77-07d7-4413-8c35-46606f476c8e.png)&#x20;

\=> Flag: `CTFlearn{th4t_is_why_you_n33d_to_sanitiz3_inputs}`

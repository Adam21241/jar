**How to setup project**  

In this project I used only python3.9 and its standard library.
Assuming you have python3.9 installed on your machine,
there is no need to install anything else.
But ff you want to perform clean code check,
you should also install flake8 (via pip).
Other python3 version should also be fine,
but there is no guarantee that program will work correctly.

<br/>

**How to run project**

1) Navigate to the root of the project
2) Run *python3.9 main.py*

<br/>

**How to use flake (optional)**

1) flake8 . --exclude venv --count --max-line-length="79" --show-source --statistics

<br/>

**How to view history of transactions**

1) Navigate to the root of the project
2) Run *sqlite3 jar.db*
3) Use sql to select proper transactions

<br/>

**Proposals of enhancement**

1) Prepare more detailed tests (especially for class Jar, db connection mocking)
2) Perform more often and precise git commits
3) Rewrite some redundant code (probably there is still some remaining)
4) Dockerize app
5) Rebuild the project as Django app with frontend interface, api and authentication
6) Deploy somewhere this app

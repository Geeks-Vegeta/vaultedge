
<code><img height="80" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code> <code><img height="80" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/flask/flask.png"></code> 

# Flask-Rest-API

This is an simple non flask blueprint, restful services build on flask framework integrated with heroku and github actions

This repository is really better to understand and it is also an begginer friendly.

> Read comments for better understand what is exactly going on in each function, and on each variable.

> It would be helpful if you fork and add stars to this repo and I also welcome you to make changes in this respository


To download this respository follow the following steps given below.


## Steps for setting up this respository


### ➡️ Step 1

Clone/Download this repository 

```bash
$ git clone https://github.com/Geeks-Vegeta/Flask-Rest-Boilerplate.git

```

after that 

```bash
$ cd [folder name]

```

Install all the given packages globally
```bash
$ pip install -r requirements.txt

```
**OR**

If you want to install the packages in virtual environment
```bash
$ pip install virtualenv

```

then create a virtual  environment in your package
```bash
$ python -m venv venv

```

activate this virtual environment
```bash
$ source venv/bin/activate

```

and if you want to deactivate this virtual environment
```bash
$ deactivate

```

> do not deactivate venv if you are running this project

Once your virtual enviroment is activate download all packages

Install all the given packages 
```bash
$ pip install -r requirements.txt

```

### ➡️ Step 2

Run this repository

```bash
$ python -m app

```

### ➡️ Step 3
Checkout API
https://vaultedgeapi.herokuapp.com

###### pdf route
It contain __two__ query parameter and __one__ body section where you can send your pdf file in binary format

**Query Parameter**
<br/>
*angle_of_rotation* [90, 180, 270]
<br/>
*page_number* [1..n]
<br/>
*isbase* [True/False]
if isbase is set to False then it will return download file, if its not False then it will return base64 pdf url.

```bash
/pdf?isbase=False&angle_of_rotation=180&page_number=18

```

**Body Section**
<br/>
make sure to send pdf in body in binary format



**Compleate Link**
<br/>
```bash
https://vaultedgeapi.herokuapp.com/pdf?isbase=True&angle_of_rotation=180&page_number=18
```

###### Sample Image
![image](https://user-images.githubusercontent.com/89457811/200666035-2925e40a-bd92-452d-b279-e37c919e7f3b.png)

<br/>
Here I have used <strong>thunderClient</strong> (vs code extention for testing api's). <br/>
You can use <strong>postman</strong> where while making post request please make sure to click send and download

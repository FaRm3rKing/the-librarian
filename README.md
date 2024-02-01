# What is 'The Librarian'
`The Librarian` is a telegram bot that saves your messages to a database. This bot was made to centralize my bookmarks and saved links using telegram.

## The problem that its trying to solve.
Do you read a lot of articles? Do you send those links to your `messenger` account? or in `instagram` or in any other app? Then one day you want to find where you saved that link so you could share it to others or read it again. But its now buried deep in one of your social media accounts never to be seen again. Well you don't have to do that anymore. You can just send those links in telegram.

The telegram bot will save those links in a database. and with [The Library](https://github.com/FaRm3rKing/the-library) you can view all your bookmarks in one place. 

## Getting Started
> This code was deployed in AWS Lambda. The guide below will only show you how to set it up in aws but not in other platforms. You will have to do your own research if you want to use it anywhere else.

### Pre-requisites
- Python 3.11 (Optional: If you're only going to run it in aws lambda)
- AWS account
- Telegram account

### Get your telegram bot token
The instructions to get your token can be found [here](https://core.telegram.org/bots/features#botfather)

### Clone and setup the repository

**Clone the repository**
```sh
git clone https://github.com/FaRm3rKing/the-librarian.git
```

**Setup .env**

You don't really need to set up a `.env` file since you will be setting the environment variables in AWS Lambda website later. But this is a good place to save your credentials for reference later. A `.env.example` is already created in the repository that you could use, just rename it to `.env`.

The environment variables we need are:
```
TELEGRAM_API=https://api.telegram.org/bot<YOUR_BOT_TOKEN>

# database credentials
HOST= 
USER=
PASSWORD= 
DATABASE=
```

**Create a mysql database in AWS RDS**

This video from `Be A Better Dev`'s channel is a great guide to setting up a basic mysql database in AWS RDS. Save your database credentials to the `.env` file for reference.

Link: [Youtube: AWS RDS MySQL Database Setup | Step by Step Tutorial](https://www.youtube.com/watch?v=Ng_zi11N4_c)

**Create a lambda function**

You can just follow this guide from `Be A Better Dev` as well. You'll learn how to create a lambda function, query your mysql database, and upload your dependencies and code to aws lambda.

Link: [Youtube: How to Query RDS MySQL From AWS Lambda in Python | Step by Step Tutorial](https://youtu.be/vyLvmPkQZkI?si=-n2WHEl2ASFovRSd&t=498)

I have already included a `layer.zip` file in this repository that you could use as a layer for dependencies. 

Just scroll to the bottom of the code tab in AWS Lambda and you will see a `Layers` section. Click `Add a layer`
![Layer section image](https://github.com/FaRm3rKing/the-librarian/blob/main/public/img/layers-section.png)

Then click `create a new layer`.
![Create a new layer image](https://github.com/FaRm3rKing/the-librarian/blob/main/public/img/create-layer.png)

You will then have to configure this new layer. You can name it however you want. Upload the `layers.zip` file here and copy the configurations seen in the screenshot.
![Create layer configuration](https://github.com/FaRm3rKing/the-librarian/blob/main/public/img/create-layer-config.png)

Add this newly created layer to your lambda function and you can now code with all your dependencies set up.

**Setting up the webhook and API Gateway**
# TODO
for API gateway use REST instead of HTTP. In my experience, HTTP would just repeatedly send the first message to the gateway.


**Add bot to group**

Create a group and add the bot as an administrator. 

> **DO NOT** add the bot and then set its role to admin, doing so would make the bot unable to receive messages. 

To do this in mobile, go to your group chat `settings` > `pencil icon` > `administrators` > `add admin`.  

You can learn more about this behavior [here](https://core.telegram.org/bots/faq#what-messages-will-my-bot-get).

**Chat away**

You are now free to send links in your group and the telegram bot will save it to your database. Use the urls saved in your database however you want or add or delete features from the lambda function. Happy Hacking!

# TODO
- [ ] for now, the librarian can only handle URLs. Maybe add command for when you want to pass a note.
- [ ] images as note
- [ ] text as note
- [ ] 

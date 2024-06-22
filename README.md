OdaAnime TelegramChatbot
Developed by [Oyedele Bolaji]

This is a Chatbot for Telegram that can generate Images using  stabble diffusion api with a prompt from the User and sends back the generated Image to the chat.

Implemented Commands

Command	Description
/start	Does nothing special just writes a welcoming message to the user.
/generate Generates an image according to what was entered behind the command. For example "/generate Van Gogh playing american football".
/help	Shows a small informational text about how /generate works.
Setup
For the Bot we need two Tokens which are simple to get but you need a github account for one of them.

Requirements 

1. Telegram Bot Token
2. Stable Diffusion API Token from replicate.com [Detailed Tutorial: https://replicate.com/blog/run-stable-diffusion-with-an-api]
You need to Sign In to Replicate using your GitHub Account with the following Link: https://replicate.com/signin?next=/blog/run-stable-diffusion-with-an-api. After that you can find your API Token on your Replicate Account: https://replicate.com/account. Now you need to set the Token as environment variable, which is different for Windows and Linux.

Set environmental variable for replicate api token key

On Windows you can open a command prompt (enter cmd in windows seearch bar) and then enter SET REPLICATE_API_TOKEN=<token> where <token> is your Token from Replicate
On Linux you open the Terminal (CTRL+ALT+T) and then enter export REPLICATE_API_TOKEN=<token> where <token> is your Token from Replicate.
After this is done, you are almost good to go you just need to run the requirements.txt with 
```
pip install -r requirement.txt
```
Open the executable file called set-token and replace the token with your replicate api token. Then run it to set the token with
```
./set-token
```
and then execute the main.py.



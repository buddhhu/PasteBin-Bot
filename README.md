<h1>PasteBin-Bot</h1>

<b> Elegant Open Source Pastebin Telegram Bot </b>

<h2>Deploy</h2>

- Get your [Environment Variables](#Variables) 

- Deploy to Heroku , Click the Icon below to deploy<br><br>
<a href="https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2Fbuddhhu%2FPasteBin-Bot"><img src="https://telegra.ph/file/84f1b9276359c25453a28.jpg" height=40 width=120 alt="Deploy" /></a>

- Local Deployment<br><br>
Execute the following commands<br>
```
git clone https://github.com/buddhhu/PasteBin-Bot
cd PasteBin-Bot
pip install -r requirements.txt
nano sample.env
```

Fill your [Variables](#Variables) in this and save it as `.env`.<br>
Now execute `python paste-it.py`


<h2>Features</h2>

- Supports readable files too
- For custom paste name - `/paste name`
- For custom highlights - `/paste None format`
- For custom name and highlights - `/paste name format`
- Highlight formats can be found [here](https://telegra.ph/Highlights-08-04)
---

<h2>Variables</h2>

- `API_ID` - Get Your API_ID from [here](https://my.telegram.org/)

- `API_HASH` - Get Your API_HASH from [here](https://my.telegram.org/) 

- `BOT_TOKEN` - Get it from [@botfather](https://t.me/botfather)

- `PASTEBIN_API_KEY` - Sign Up/Sign In and get Your PASTEBIN_API_KEY from [here](https://pastebin.com/doc_api#1)

- `PASTE_EXPIRY` - Set the key to amount of time you want the Paste to be deleted in  i.e  10M (N, 10M, 1H, 10, 1M)<br> N - `Never`<br>  10M - `10 minutes`<br>  1H - `1 hour`<br>  1D - `1 day`<br>  1M - `1 month`
 
- `PRIVATE_PASTE` - Set the Value (NO, YES)


<h2>Mandatory Environment Variables</h2>

- `API_ID`
- `API_HASH`
- `BOT_TOKEN`
- `PASTEBIN_API_KEY`

<h2>Extra Environment Variables</h2>

- `PASTE_EXPIRY`
- `PRIVATE_PASTE`

<h2>Credits</h2>

- [@buddhhu](https://github.com/buddhhu)
- [@Neon7580](https://github.com/Neon7580)


If this has been helpful and you appreciate our work , support  us by giving us a Star 🌟 


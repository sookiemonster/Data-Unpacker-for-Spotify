# Data Unpacker for Spotify


Visualizes the Spotify 1-year data package from 

```
Spotify Account Settings -> Privacy Settings
```
[This link](https://www.spotify.com/account/privacy/) should work as well.



## Setting up 
```bash
# Get repo
git clone https://github.com/sookiemonster/Data-Unpacker-for-Spotify.git
cd Data-Unpacker-for-Spotify
```

<b>Highly suggested to run this in a virtual environment</b>
```bash
pip install virtualenv
python3 -m venv venv
```
```bash
source ./venv/Scripts/Activate # Linux/macOS/Git Bash
```
```bash
.\venv\Scripts\Activate # Windows CMD
```

Install dependencies
```bash
pip install -r requirements.txt
```

Run
```bash
flask run --with-threads
```

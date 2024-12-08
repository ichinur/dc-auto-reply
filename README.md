# How to Retrieve Your Discord Token

1. **Open Discord in Your Browser**  
   Log in to your Discord account in a browser (Chrome or Firefox).

2. **Open Developer Tools**  
   Press `Ctrl + Shift + I` (Windows) or `Cmd + Option + I` (Mac) to open Developer Tools.

3. **Go to the Network Tab**  
   In Developer Tools, click the **Network** tab.

4. **Send a Message**  
   Type and send any message in a channel to trigger network activity.

5. **Find the `authorize` Request**  
   Look for a request labeled **authorize** in the Network tab.

6. **Copy Your Token**  
   - Click on the `authorize`request.
   - Go to the `Headers` tab.
   - Copy the value next to `Authorization`. This is your Discord token.

>> **Note:**   - Keep your token private.  - Do not share it with anyone.


# How to Retrieve a Discord Channel ID

1. **Enable Developer Mode**  
   - Go to User `Settings` (gear icon at the bottom).  
   - Navigate to the `Advanced`tab.  
   - Enable the `Developer Mode` option.

2. **Copy the Channel ID**  
   - Right-click on the channel you want to get the ID for.  
   - Select `Copy ID`.  
   The copied value is the Channel ID you need.

## File `massage.txt`:
>>  yourtoken

## File `massage.txt`:
>>  response 1  
>>  response 2  
>>  response 3  

## Run the script
```bash
pip install -r requirements.txt
```
```bash
python3 dcreply.py
```


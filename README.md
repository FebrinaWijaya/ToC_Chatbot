# TOC Chatbot Project 2019

## Localhost with ngrok
To add environment variable:
```sh
sudo -H subl /etc/environment
```
![](https://i.imgur.com/Eeupr13.png)

1. ```sh
    ./ngrok http 5000
    ```
    - will generate https link
        - e.g  https://7398aaae.ngrok.io
    ![](https://i.imgur.com/cvqkhpF.png)
2. run the script:
    ```sh
    python3 app.py
    ```
    ![](https://i.imgur.com/U3vcOTa.png)
3. copy the ngrok link to webhook, fill in the right verification token
    verify token: FWy9z9bjutzBb1oLfjt2D
    ![](https://i.imgur.com/p0j5CpO.png)

    - First time:
        - setup from messenger->settings->webhooks
        - if we want to change the URL:
            - Webhooks->edit subscription
            - ![](https://i.imgur.com/SxHtigq.png)

    - Verification token should be the same as the VERIFY_TOKEN in **app.py**
4. subscribe fb page to webhook(messenger->settings->webhooks)
    ![](https://i.imgur.com/KZWayaD.png)

5. Generate token for the page and copy to ACCESS_TOKEN in utils.py
    ![](https://i.imgur.com/c5nYRKf.png)

# Deploy to Heroku
## Webhook
Callback URL:  https://itsvacationtime.herokuapp.com/webhook
Verify token: FWy9z9bjutzBb1oLfjt2D

## Push to Heroku
- Install the Heroku CLI

- If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.
    ```sh
    $ heroku login
    ```
- Clone the repository
Use Git to clone itsvacationtime's source code to your local machine.
    ```sh
    $ heroku git:clone -a itsvacationtime
    $ cd itsvacationtime
    ```
- Deploy your changes
Make some changes to the code you just cloned and deploy them to Heroku using Git.
    ```sh
    $ git add .
    $ git commit -am "make it better"
    $ git push heroku master
    ```


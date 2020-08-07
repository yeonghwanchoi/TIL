import requests, json

def weather(key, lat, lon):
    url = "https://api.darksky.net/forecast/{}/{},{}".format(key, lat, lon)
    response = requests.get(url)
    return response.json()["daily"]["summary"]

def send_slack(key, msg, channel="#dss", username="날씨봇_yh"):
    payload = {
        "channel": channel,
        "username": username,
        "text": msg
    }
    requests.post(key, json.dumps(payload))
    
darksky_key = "16a09268a167f2c538467d9ce4f9fecc"
data = weather(darksky_key, 37.5665, 126.9780)
slack_key = "https://hooks.slack.com/services/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"
send_slack(slack_key, data)

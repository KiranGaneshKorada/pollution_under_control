import requests


def sendMessage(number):

    url = "https://www.fast2sms.com/dev/bulkV2"

    payload = "kindly renew your puc certificate&language=english&route=q&numbers=f'{number}"

    headers = {
    'authorization': "YD23n1LBsGSVue7JEXvZTH0xprlA9tFbQ5hwUfcNPaMRqOmW6oUStVnIRETQCMFW1p9iyhmZdsc6e5JA",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
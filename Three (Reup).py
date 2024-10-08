def ordersim():
    import time
    import requests
    import names
    import os
    import random
    from twocaptcha import TwoCaptcha
    headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'dnt': '1',
    'Host': 'www.three.co.uk',
    'Origin': 'https://www.three.co.uk',
    'Referer': 'https://www.three.co.uk/Support/Free_SIM/Order',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
    }
    solver = TwoCaptcha({API_HERE})
    result = solver.hcaptcha(
        sitekey='28d6ff2e-5725-4d95-a4b8-2c0a400fd47c',
        url='https://www.three.co.uk/Support/Free_SIM/Order',
        version='v2',
        action='demo_action',
        score=0.3
    )
    fname = {FIRST_NAME_HERE}
    lname = {LAST_NAME_HERE}
    postcode = {POSTCODE_HERE}
    address1 = {ADDRESS_HERE}
    address2 = {ADDRESS2_HERE}
    city = {CITY_HERE} #Must match with dropdown menu
    payload = {
        "_form_url":"",
        "_success_url":"/Support/Free_SIM/Order_Confirmation",
        "_failure_url":"",
        "hiddenField":"tr-triosim",
        "firstname":fname,
        "surname":lname,
        "existingContactNumber":"",
        "email":{EMAIL_HERE},
        "confirmemail":{EMAIL_HERE},
        "postcode":postcode,
        # "addressDropdown":"55094489.00",
        "street":address1,
        "address2":address2,
        "town":city,
        "marketingPrefs":"Yes",
        "g-recaptcha-response":f'{str(result["code"])}',
        "h-captcha-response":f'{str(result["code"])}'
    }
    r = requests.post('https://www.three.co.uk/cs/form/freesimreg', headers=headers, json=payload)
    if r.status_code == 200:
        response_text = r.text
    
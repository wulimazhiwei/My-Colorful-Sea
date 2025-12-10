import requests

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://jzsc.mohurd.gov.cn/data/company",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "accessToken;": "",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "timeout": "30000",
    "v": "231012"
}
cookies = {
    "Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c": "1753875226,1753949409",
    "HMACCOUNT": "BB7C66DF142F5466",
    "Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c": "1753952338"
}

url = "https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/list"


def encrypt_response(page):
    params = {
        "pg": page,
        "pgsz": "15",
        "total": "450"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    return response.text


def decrypt_response(response):
    form_data = {
        'group': 'my_rpc',
        'action': 'get_rpc',
        'data': response
    }

    # 加密数据只能通过post的方式传递，get请求对于查询字符串有长度限制
    response = requests.post('http://127.0.0.1:5620/business-demo/invoke', data=form_data)
    print(response.json())


encrypt_data = encrypt_response(page=1)
decrypt_response(encrypt_data)

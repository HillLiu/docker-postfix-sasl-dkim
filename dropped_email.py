import sys
from http import client

STATUS_CODE_MAP = {'431': '2', '450': '5', '452': '2',
                   '510': '1', '511': '1', '512': '1',
                   '513': '4', '523': '2', '530': '4',
                   '535': '4', '541': '3', '544': '3',
                   '550': '1', '551': '3', '552': '2',
                   '553': '1', '554': '1'}

STATUS_CODE_MSG_MAP = {'1': '郵件地址錯誤',
                       '2': '信箱空間不足',
                       '3': '拒收外部信件',
                       '4': '系統驗證錯誤',
                       '5': '查無使用者',
                       '6': '其他'}

SERVER = "omnisegment.com"
REPORT_URL = "/ma_account/bounced-email-callback/"

def extract_info():
    cycle_id, audience_id, email_node_id, status_code, status_msg = None, None, None, None, None
    status_code = '6'
    status_msg = STATUS_CODE_MSG_MAP[status_code]

    for line in sys.stdin:
        if line.startswith("X-TRACKING-ID"):
            tokens = line.split(':')[1].strip().split('-')
            cycle_id = int(tokens[0])
            audience_id = int(tokens[1])
            email_node_id = int(tokens[2])
        elif line.startswith("Diagnostic-Code:"):
            _status_msg = line.split(':')[1].strip()

            for k, v in STATUS_CODE_MAP.items():
                if k in _status_msg:
                    status_code = v
                    status_msg = STATUS_CODE_MSG_MAP[status_code]


    return (cycle_id, audience_id, email_node_id, status_code, status_msg)

cycle_id, audience_id, email_node_id, status_code, status_msg = extract_info()
if cycle_id is not None:
    conn = client.HTTPSConnection(SERVER)
    url = f"{REPORT_URL}?cycle={cycle_id}&audience={audience_id}&email_node={email_node_id}"
    conn.request("GET", url)

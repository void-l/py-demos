# -*- coding:utf-8 -*-


def trans_header_to_dict(headers):
    """
    :parameter headers :
        Host: fanyi.baidu.com
        Connection: keep-alive
        Content-Length: 57
        Accept: application/json, text/javascript, */*; q=0.01
        Origin: http://fanyi.baidu.com
        X-Requested-With: XMLHttpRequest
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36
        Content-Type: application/x-www-form-urlencoded; charset=UTF-8
        Referer: http://fanyi.baidu.com/collection
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,zh;q=0.8,en;q=0.6
        Cookie: BAIDUID=2A69256500084BDE59B370E789589709:FG=1; BIDUPSID=7447B3FB210243BC214F81B85E15F5F9; PSTM=1489889990; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=ZiYzR2Q2xMdzRHemkzYU9reFlsQWUxWUllcX5JWXRPUFpGbnR5TjZnVGR0fnhZSVFBQUFBJCQAAAAAAAAAAAEAAAB6YhYwwfWyqGNvZGluZwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN0q1VjdKtVYSj; locale=zh; BDRCVFR[PGs3nHvqVLt]=mbxnW11j9Dfmh7GuZR8mvqV; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=7; BDSFRCVID=L48sJeCCxG3mpiTiclRzBHoNO_6C_elKAH-53J; H_BDCLCKID_SF=JJ4O_C-5tCvKeJbYK4oj5KCyMfca5C6JKCOa3RA8Kb7VbpFRQRbkbftd2-te-xnEKK5E5-59L-J-MKJJQ-5f3MrDyf64ajJZfJuDoDtMJIDabP365IFMD5oH-frMetJya4o2WDkatqb5OR5Jj65CMq-9bNo00fJ7Qe08QJ7v5KnrOq-63MA--fFihbQgQtrrL-jNaJRyLMbSsq0x0-jWe-bQypoa3j3tJIOMahkb5h7xOKbk05CaD5oXeH_8q6nQ-PoeLRrsKRrfKR74bITjh6PTja7eBtQm05bxob6M2xbEHnR-2x51hUCgBNjmy-QQW267sCKbWDcjqR8ZD6uWD6cP; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; H_PS_PSSID=1462_18195_21083_17001_20928; pgv_pvi=6958253056; pgv_si=s7076079616; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1490365141; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1490493733
    :return dict_headers
    """
    headers = headers.split('\n')
    headers = [item.strip(' ') for item in headers]
    headers = [item.strip(' ') for item in headers if len(item) > 0]

    dict_headers = {}
    for item in headers:
        index = item.find(':')
        if index == -1:
            raise Exception('the headers data goes wrong, please check: ' + item)
        k = item[: index]
        v = item[index + 1:]
        dict_headers[k] = v

    return dict_headers


if __name__ == "__main__":
    header_origin = '''
        Host: fanyi.baidu.com
        Connection: keep-alive
        Content-Length: 57
        Accept: application/json, text/javascript, */*; q=0.01
        Origin: http://fanyi.baidu.com
        X-Requested-With: XMLHttpRequest
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36
        Content-Type: application/x-www-form-urlencoded; charset=UTF-8
        Referer: http://fanyi.baidu.com/collection
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,zh;q=0.8,en;q=0.6
        Cookie: BAIDUID=2A69256500084BDE59B370E789589709:FG=1; BIDUPSID=7447B3FB210243BC214F81B85E15F5F9; PSTM=1489889990; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=ZiYzR2Q2xMdzRHemkzYU9reFlsQWUxWUllcX5JWXRPUFpGbnR5TjZnVGR0fnhZSVFBQUFBJCQAAAAAAAAAAAEAAAB6YhYwwfWyqGNvZGluZwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN0q1VjdKtVYSj; locale=zh; BDRCVFR[PGs3nHvqVLt]=mbxnW11j9Dfmh7GuZR8mvqV; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=7; BDSFRCVID=L48sJeCCxG3mpiTiclRzBHoNO_6C_elKAH-53J; H_BDCLCKID_SF=JJ4O_C-5tCvKeJbYK4oj5KCyMfca5C6JKCOa3RA8Kb7VbpFRQRbkbftd2-te-xnEKK5E5-59L-J-MKJJQ-5f3MrDyf64ajJZfJuDoDtMJIDabP365IFMD5oH-frMetJya4o2WDkatqb5OR5Jj65CMq-9bNo00fJ7Qe08QJ7v5KnrOq-63MA--fFihbQgQtrrL-jNaJRyLMbSsq0x0-jWe-bQypoa3j3tJIOMahkb5h7xOKbk05CaD5oXeH_8q6nQ-PoeLRrsKRrfKR74bITjh6PTja7eBtQm05bxob6M2xbEHnR-2x51hUCgBNjmy-QQW267sCKbWDcjqR8ZD6uWD6cP; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; H_PS_PSSID=1462_18195_21083_17001_20928; pgv_pvi=6958253056; pgv_si=s7076079616; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1490365141; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1490493733
    '''

    trans_header_to_dict(header_origin)

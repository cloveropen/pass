from aip import AipOcr

APP_ID = '22296336'
API_KEY = 'oxI8Yjg9jXZfRQ9ofVvgTte0'
SECRET_KEY = 'C7L8CcGnQww7FGEc0GATGBw1zq7mIE5z'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def image2text(fileName):
    image = get_file_content(fileName)
    dic_result = client.accurate(image)
    res = dic_result['words_result']
    result = ''
    for m in res:
        result = result + str(m['words'])
    print("result=" + result)
    return result


getresult = image2text('./盐酸二甲双胍片-中美上海施贵宝制药有限公司1.jpg')
fp = open('盐酸二甲双胍片-中美上海施贵宝制药有限公司1.txt', 'wt')
fp.write(getresult)
fp.close()

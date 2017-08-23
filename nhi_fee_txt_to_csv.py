import sys

# https://www.nhi.gov.tw/Content_List.aspx?n=58ED9C8D8417D00B&topn=D39E2B72B0BDFA15
# Download 支付標準壓縮檔(NHI Fee Schedule)(.txt)

def parse(fn):
    with open(fn, 'r') as f:
        lines = f.readlines()
    fee_file = open('fee.csv', 'w')
    headers = ['診療項目代碼', '健保支付點數', '開始日期', '結束日期', '英文項目名稱',
               '中文項目名稱', '附註']
    fee_file.write(','.join(headers) + '\n')
    for line in lines:
        data_arr = [x.strip().replace('"', '') for x in line.split('^')][:-1]
        fee_file.write(','.join(data_arr) + '\n')
    fee_file.close()


if __name__ == '__main__':
    try:
        parse(sys.argv[1])
    except IndexError:
        print('no arg')

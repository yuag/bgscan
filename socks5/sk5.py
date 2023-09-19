#接口：https://docs.proxyscrape.com/?_ga=2.204069714.371948258.1694509768-128409466.1694509768
import argparse
import requests

def proxy(api_url, output_file):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.text
        with open(output_file, "w") as file:
            file.write(data)
        print("数据已成功下载并保存到根目录{}文件。".format(output_file))
    else:
        print("无法获取API数据。响应状态码：", response.status_code)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-socks5", action="store_true")
    parser.add_argument("-http", action="store_true")
    parser.add_argument("-socks4", action="store_true")
    args = parser.parse_args()

    if args.socks5:
        api_url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all"
        proxy(api_url, output_file="socks5.txt")

    if args.http:
        api_url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
        proxy(api_url, output_file="http.txt")
    
    if args.socks4:
        api_url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all"
        proxy(api_url, output_file="socks4.txt")

if __name__ == "__main__":
    main()

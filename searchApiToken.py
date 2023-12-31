import concurrent.futures
import requests
import time

out = []
CONNECTIONS = 100
TIMEOUT = 5
import requests

burp0_url = "https://app.feedblitz.com:443/f/f.Fbz?UserManager=-100&ownerid=238587531"
cookies = {"cookieprefs": "\"~yM3Zihr9HTI=\"", "_ga": "GA1.2.1755614629.1703853448", "_gid": "GA1.2.2021354578.1703853448", "_ga_QRNE5KMX63": "GS1.2.1703857093.2.0.1703857093.0.0.0", "_hjSessionUser_2256847": "eyJpZCI6IjQxOWY1NmY4LTAzMDAtNTE3Yi04NjQwLTQyZDU5NDQ2MGM1NSIsImNyZWF0ZWQiOjE3MDM4NTM0NzA5OTUsImV4aXN0aW5nIjp0cnVlfQ==", "v5": "\"100\"", "__utma": "225336010.1876708372.1703853486.1703864517.1703873611.4", "__utmz": "225336010.1703853486.1.1.utmccn=(referral)|utmcsr=feedblitz.com|utmcct=/|utmcmd=referral", "_hjSessionUser_2256856": "eyJpZCI6IjE4ODQyZGIzLTRhMGEtNWU1Ny05MDYxLTM5MWY0ZjQ0ZjFkMSIsImNyZWF0ZWQiOjE3MDM4NTM1NzUwNDQsImV4aXN0aW5nIjp0cnVlfQ==", "_lc2_fpi": "fdbfc301baa5--01hjtscn8akw6qj8e8d98h04wy", "_lc2_fpi_meta": "{%22w%22:1703853577482}", "_fw_crm_v": "96b6195f-1694-4124-e250-7b6db620217c", "__utmb": "225336010", "__utmc": "225336010", "UserID": "\"~I6T2scL66t857pGYZiPfr5UU455zQRiYy5SbyrYfNUaciJ9uSGlX3aw2MNPDSUzEfg5E4s30RAP7ff+Sj8V4c75XOeXpr0T1/H4PZCfaVbrBZtRgBhh/JD/G02ImG/7/\"", "_li_dcdm_c": ".feedblitz.com", "_hjIncludedInSessionSample_2256856": "0", "_hjSession_2256856": "eyJpZCI6IjAwYzNkM2JkLTI5NjgtNDZmOC05NzViLTg0NDEzMDFhMTc4NSIsImMiOjE3MDM4NzM2NTA5NDMsInMiOjAsInIiOjAsInNiIjoxfQ==", "_hjAbsoluteSessionInProgress": "0"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate, br", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1", "Te": "trailers", "Connection": "close"}

urls = open('dz.txt.txt').read().splitlines()

result = open("apitoken.txt","w")
def load_url(url, timeout):
    ans = requests.get(url)
    return ans

with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
    future_to_url = (executor.submit(load_url, url, TIMEOUT) for url in urls)
    time1 = time.time()
    i=0
    for future in concurrent.futures.as_completed(future_to_url):
        try:
            ans = future.result()
            data = ans.text
            url = ans.url
            #print(data)
            if "api.telegram" in str(data):
                print("found")
                result.write(url+"\n")

        except Exception as exc:
            #print(str(exc))
            data = str(type(exc))
        finally:
            out.append(data)

            print(str(len(out)),end="\r")

    time2 = time.time()
print(f'Took {time2-time1:.2f} s')


#!/usr/bin/env python3
import requests
import os
import json
from colorama import Fore, init, Back
from cfonts import say

init(autoreset=True)

class NikChecker:

    @staticmethod
    def Banner():
        os.system("cls" if os.name == "nt" else "clear")
        say("NIK INDONESIA", colors=["red", "white"], align="center")
        
        print("")
    
    @staticmethod
    def Run():
        NikChecker.Banner()
        nikInput = input(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTYELLOW_EX}#{Fore.LIGHTCYAN_EX}] {Fore.WHITE}Masukkan NIK Atau NPWP --> ")
        print(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTYELLOW_EX}#{Fore.LIGHTCYAN_EX}] {Fore.WHITE}Harap Bersabar...")

        try:
            req = requests.get(f"https://api-matchid.watalks.com/app/dataku/Ktp?ssaid=384e5584128b93c7&nik_data={nikInput}&uuid=ea35be83-a485-4bf9-b9b4-42a8df699780&nama_data=&token_data=null&loc=31.24916%2C121.48789833333333&build=dev", headers={
                "Host": "api-matchid.watalks.com",
                "Build-Type": "release",
                "Key": "19505e6963b7e2e9f0dc6eab600a966b",
                "Authorization": "BearerTOKEN",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/N2G48H)",
                "Accept-Encoding": "gzip, deflate"
            }).json()
            data = json.loads(json.dumps(req))

            if data["Status"] == "true" and data["Server"][0]["Status_Server"] == "OK":
                if data["Data"]["status"] == 200:
                    print("")
                    print(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTYELLOW_EX}#{Fore.LIGHTCYAN_EX}] {Fore.WHITE}{Back.LIGHTGREEN_EX}Data DiTemukan!")
                    print(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTYELLOW_EX}#{Fore.LIGHTCYAN_EX}] {Fore.WHITE}NIK           : {Fore.LIGHTGREEN_EX}{nikInput}")
                    print(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTYELLOW_EX}#{Fore.LIGHTCYAN_EX}] {Fore.WHITE}Jenis Kelamin : {Fore.LIGHTGREEN_EX}{data['Data']['message']['data']['jk']}")
                    print(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTYELLOW_EX}#{Fore.LIGHTCYAN_EX}] {Fore.WHITE}Tgl Lahir     : {Fore.LIGHTGREEN_EX}{data['Data']['message']['data']['tgl']}")
                    print(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTYELLOW_EX}#{Fore.LIGHTCYAN_EX}] {Fore.WHITE}Kecamatan     : {Fore.LIGHTGREEN_EX}{data['Data']['message']['data']['kec']}")
                    print(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTYELLOW_EX}#{Fore.LIGHTCYAN_EX}] {Fore.WHITE}Kabupaten     : {Fore.LIGHTGREEN_EX}{data['Data']['message']['data']['kab']}")
                    print(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTYELLOW_EX}#{Fore.LIGHTCYAN_EX}] {Fore.WHITE}Provinsi      : {Fore.LIGHTGREEN_EX}{data['Data']['message']['data']['prov']}")
                else:
                    print("")
                    print(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTYELLOW_EX}#{Fore.LIGHTCYAN_EX}] {Fore.BLACK}{Back.LIGHTGREEN_EX}Data Tidak DiTemukan!")
            else:
                print("")
                print(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTYELLOW_EX}#{Fore.LIGHTCYAN_EX}] {Fore.BLACK}{Back.LIGHTGREEN_EX}Data Tidak DiTemukan!")
        except:
            print("")
            print(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTYELLOW_EX}#{Fore.LIGHTCYAN_EX}] {Fore.BLACK}{Back.LIGHTGREEN_EX}Data Tidak DiTemukan!")



if __name__ == "__main__":
    NikChecker.Run()

import sys
import zipfile
import os
from os import path
import shutil
import zipfile as zp
import re
import pyutil
import json
import requests
from pathlib import Path
from datetime import date
from DownloadResources import DownloadResources

apigee_mgmt_url="https://apigee.googleapis.com/v1/organizations/"
#apigee_apigeex_mgmt_url="https://api.enterprise.apigee.com/v1//organizations/"

print("This tool Downloads All the ApigeeX Data")
apigeex_org_name = input("Enter ApigeeX Org Name: ")
apigeex_token = input("Enter ApigeeX Org Token: ")

response,status_code=DownloadResources.get_resource("apis",apigee_mgmt_url,apigeex_org_name,apigeex_token)
if status_code == 200:
    DownloadResources.delete_all_existing_directory()
    user_choice =''
    while user_choice !='quit':
        print("--------------------------------------------")    
        print("|  Type All to Download All Resources      |")
        print("|  Type Proxy to Download Only Proxies     |")
        print("|  Type SF to Download Only SharedFlows    |")
        print("|  Type Product to Download Only Products  |")
        print("|  Type App to Download Only Apps          |")
        print("|  Type KVM to Download Only KVM           |")
        print("|  Type TS to Download Only Target Servers |")
        print("|  Type DEV to Download Only Developers    |")
        print("|  Type QUIT to Download EXIT              |")
        print("--------------------------------------------")   
        user_choice = input("Enter Your Choice : ")
        user_choice = user_choice.lower().strip()
        if user_choice == "all" or user_choice == "ts":
            apigeex_evn=DownloadResources.Envs(apigee_mgmt_url,apigeex_org_name,apigeex_token)
            arr_env  = apigeex_evn.split(',')
            for env in arr_env:
                env = re.sub(r'[\[\]\"]','',env)
                env=env.strip();
                DownloadResources.Target_Servers(apigee_mgmt_url,apigeex_org_name,apigeex_token,env)
            print("All Target Servers Downloaded")

        if user_choice == "all" or user_choice == "kvm":    
            apigeex_evn=DownloadResources.Envs(apigee_mgmt_url,apigeex_org_name,apigeex_token)
            arr_env  = apigeex_evn.split(',')
            for env in arr_env:
              env = re.sub(r'[\[\]\"]','',env)
              env=env.strip();
              DownloadResources.Kvms_Env_Level(apigee_mgmt_url,apigeex_org_name,apigeex_token,env)
            print("All KVM's Downloaded")

        if user_choice == "all" or user_choice == "dev":
            DownloadResources.Developers(apigee_mgmt_url,apigeex_org_name,apigeex_token)
            print("All Developers Downloaded")

        if user_choice == "all" or user_choice == "app":
            list_of_apps,status_code_apps=DownloadResources.get_resource("apps",apigee_mgmt_url,apigeex_org_name,apigeex_token)
            list_of_apps = re.sub(r'\n','',list_of_apps.text)
            arr_apps=list_of_apps.split("}")
            for app in arr_apps:
            	app=app.replace('\"','')
            	app=app.replace('app:','')
            	app=app.replace('appId:','')
            	app = re.sub(r'[\[\]\"\,\s*\}\{]','',app)
            	if app != '':
            		DownloadResources.Apps(apigee_mgmt_url,app,apigeex_org_name,apigeex_token)
            print("All Apps Downloaded")

        if user_choice == "all" or user_choice == "product":
            list_of_products,status_code_products=DownloadResources.get_resource("apiproducts",apigee_mgmt_url,apigeex_org_name,apigeex_token)
            list_of_products = re.sub(r'\n','',list_of_products.text)
            arr_products=list_of_products.split(",")
            for product in arr_products:
            	product=product.replace('\"','')
            	product=product.replace('name:','')
            	product=product.replace('apiProduct:','')
            	product=product.strip()
            	product = re.sub(r'[\[\]\"\,\}\{]','',product)
            	product=product.strip()
            	if product !='':
            		DownloadResources.Products(apigee_mgmt_url,product,apigeex_org_name,apigeex_token)
            print("All Products Downloaded")

        if user_choice == "all" or user_choice == "proxy":
            list_of_proxies,status_code_proxies=DownloadResources.get_resource("apis",apigee_mgmt_url,apigeex_org_name,apigeex_token)
            list_of_proxies = re.sub(r'\n','',list_of_proxies.text)
            list_of_proxies = re.sub(r'[\[\]\"\}\{]','',list_of_proxies)
            list_of_proxies=list_of_proxies.replace("proxies:",'')
            list_of_proxies=list_of_proxies.replace("apiProxyType: PROGRAMMABLE",'')
            list_of_proxies=list_of_proxies.replace("name:",'')
            arr_proxies=list_of_proxies.split(",")
            for proxy_names in arr_proxies:
                proxy_names=proxy_names.strip()
                if proxy_names != '':
                    print("Downloading Proxy : "+ proxy_names)
                    DownloadResources.Proxies(apigee_mgmt_url,proxy_names,apigeex_org_name,apigeex_token)
            print("All Proxies Downloaded")
        
        if user_choice == "all" or user_choice == "sf":
            list_of_shared_flows,status_code_shared_flows=DownloadResources.get_resource("sharedflows",apigee_mgmt_url,apigeex_org_name,apigeex_token)
            list_of_shared_flows = re.sub(r'\n','',list_of_shared_flows.text)
            list_of_shared_flows = re.sub(r'[\[\]\"\}\{]','',list_of_shared_flows)
            list_of_shared_flows=list_of_shared_flows.replace("sharedFlows:",'')
            list_of_shared_flows=list_of_shared_flows.replace("name:",'')
            arr_shared_flows=list_of_shared_flows.split(",")
            for shared_flow in arr_shared_flows:
                shared_flow=shared_flow.strip()
                if shared_flow != '':
                    print("Downloading Shared Flow : "+ shared_flow)
                    DownloadResources.Shared_Flows(apigee_mgmt_url,shared_flow,apigeex_org_name,apigeex_token)
            print("All Shared Flows Downloaded")
else:
    print("Error !!! ")
    print("Invalid Org Name or Invalid Token")
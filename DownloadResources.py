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

folder_name="data-apigeex-"+str(date.today())

class DownloadResources:
	def __init__(self, arg):
		super(DownloadResources, self).__init__()
	def get_resource(resource,apigee_mgmt_url,org,token):
	    url = apigee_mgmt_url+org+"/"+resource+"/"
	    payload={}
	    headers = {'Authorization': 'Bearer '+token}
	    response = requests.request("GET", url, headers=headers, data=payload, stream=True)
	    status_code = response.status_code
	    return response,status_code

	def Apps(apigee_mgmt_url,app_name,org,token):
	    response,status_code=DownloadResources.get_resource("apps/"+app_name,apigee_mgmt_url,org,token)
	    if status_code == 200:
	        path=folder_name+"/apps/"
	        print("Downloading APP : "+app_name)
	        Path(path).mkdir(parents=True, exist_ok=True)
	        with open(folder_name+"/apps/"+app_name, "w") as file:
	            file.write(response.text)

	def Products(apigee_mgmt_url,product_name,org,token):
	    response,status_code=DownloadResources.get_resource("apiproducts/"+product_name,apigee_mgmt_url,org,token)    
	    if status_code == 200:
	        path=folder_name+"/products/"
	        print("Downloading Product : "+product_name)
	        Path(path).mkdir(parents=True, exist_ok=True)
	        with open(folder_name+"/products/"+product_name, "w") as file:
	            file.write(response.text)

	def Proxies(apigee_mgmt_url,proxy_name,org,token):
	    response,status_code=DownloadResources.get_resource("apis/"+proxy_name+"/revisions",apigee_mgmt_url,org,token)        
	    path=folder_name+"/proxies/"
	    match_multiple_revisions = re.search('\,', response.text)
	    if match_multiple_revisions:
	        proxies_revision_names_arr=response.text.split(',')
	        rev_no=len(proxies_revision_names_arr)
	        url = apigee_mgmt_url+org+"/apis/"+proxy_name+"/revisions/"+str(rev_no)+"?format=bundle"
	        payload={}
	        headers = {'Authorization': 'Bearer '+token}
	        response = requests.request("GET", url, headers=headers, data=payload)
	        Path(path).mkdir(parents=True, exist_ok=True)
	        target_path = path+"/"+proxy_name+".zip"
	        response = requests.request("GET", url, headers=headers, data=payload, stream=True)
	        handle = open(target_path, "wb")
	        for chunk in response.iter_content(chunk_size=512):
	            if chunk:  # filter out keep-alive new chunks
	                handle.write(chunk)
	        handle.close()
	    else:
	        url = apigee_mgmt_url+org+"/apis/"+proxy_name+"/revisions/1"+"?format=bundle"
	        payload={}
	        headers = {'Authorization': 'Bearer '+token}
	        response = requests.request("GET", url, headers=headers, data=payload)
	        Path(path).mkdir(parents=True, exist_ok=True)
	        target_path = path+"/"+proxy_name+".zip"
	        response = requests.request("GET", url, headers=headers, data=payload, stream=True)
	        handle = open(target_path, "wb")
	        for chunk in response.iter_content(chunk_size=512):
	            if chunk:  # filter out keep-alive new chunks
	                handle.write(chunk)
	        handle.close()  

	def Shared_Flows(apigee_mgmt_url,shared_flow_name,org,token):
	    response,status_code=DownloadResources.get_resource("sharedflows/"+shared_flow_name+"/revisions",apigee_mgmt_url,org,token)
	    path=folder_name+"/sharedflows/"
	    match_multiple_revisions = re.search('\,', response.text)
	    if match_multiple_revisions:
	        shared_flows_revision_names_arr=response.text.split(',')
	        rev_no=len(shared_flows_revision_names_arr)
	        url = apigee_mgmt_url+org+"/sharedflows/"+shared_flow_name+"/revisions/"+str(rev_no)+"?format=bundle"
	        payload={}
	        headers = {'Authorization': 'Bearer '+token}
	        response = requests.request("GET", url, headers=headers, data=payload)
	        Path(path).mkdir(parents=True, exist_ok=True)
	        target_path = path+"/"+shared_flow_name+".zip"
	        response = requests.request("GET", url, headers=headers, data=payload, stream=True)
	        handle = open(target_path, "wb")
	        for chunk in response.iter_content(chunk_size=512):
	          if chunk:  # filter out keep-alive new chunks
	            handle.write(chunk)
	        handle.close()
	    else:
	        url = apigee_mgmt_url+org+"/sharedflows/"+shared_flow_name+"/revisions/1"+"?format=bundle"
	        payload={}
	        headers = {'Authorization': 'Bearer '+token}
	        response = requests.request("GET", url, headers=headers, data=payload)
	        Path(path).mkdir(parents=True, exist_ok=True)
	        target_path = path+"/"+shared_flow_name+".zip"
	        response = requests.request("GET", url, headers=headers, data=payload, stream=True)
	        handle = open(target_path, "wb")
	        for chunk in response.iter_content(chunk_size=512):
	          if chunk:  # filter out keep-alive new chunks
	            handle.write(chunk)
	        handle.close()  


	def Envs(apigee_mgmt_url,org,token):
	    response,status_code=DownloadResources.get_resource("environments",apigee_mgmt_url,org,token)
	    response = re.sub(r'\n','',response.text)
	    output = re.search('\[(.*?)\]', response, flags=re.IGNORECASE)
	    if output is not None:
	        all_env = output.group(0)
	        all_env = re.sub(r'[\[\]\s*]\"\"','',all_env)
	        return all_env

	def Target_Servers(apigee_mgmt_url,org,token,env):
	    response,status_code=DownloadResources.get_resource("environments/"+env+"/targetservers",apigee_mgmt_url,org,token)
	    response = re.sub(r'\n','',response.text)
	    output = re.search('\[(.*?)\]', response, flags=re.IGNORECASE)
	    if output is not None:
	        all_target_servers = output.group(0)
	        arr_target_servers =all_target_servers.split(",")
	        for target_servers in arr_target_servers:
	            target_servers = re.sub(r'[\[\]\"]','',target_servers)
	            target_servers=target_servers.strip()
	            if target_servers !='':
	                response,status_code=DownloadResources.get_resource("environments/"+env+"/targetservers/"+target_servers,apigee_mgmt_url,org,token)
	                if status_code == 200:
	                    target_servers = re.sub(r'[\[\]\"]','',target_servers)
	                    target_servers = target_servers.strip()
	                    print("Downloading Target Servers : "+target_servers+" ENVIRONMENT "+env )
	                    path=folder_name+"/targetservers/env/"+env+"/"
	                    Path(path).mkdir(parents=True, exist_ok=True)
	                    with open(path+target_servers, "w") as file:
	                        file.write(response.text)

	def Kvms_Env_Level(apigee_mgmt_url,org,token,env):
	    response,status_code=DownloadResources.get_resource("environments/"+env+"/keyvaluemaps",apigee_mgmt_url,org,token)
	    response = re.sub(r'\n','',response.text)
	    output = re.search('\[(.*?)\]', response, flags=re.IGNORECASE)
	    if output is not None:
	        all_kvms_env_level = output.group(0)
	        arr_kvms=all_kvms_env_level.split(",")
	        for kvm in arr_kvms:
	            kvm = re.sub(r'[\[\]\"]','',kvm)
	            kvm =kvm.strip()
	            if kvm != '':
	                response,status_code=DownloadResources.get_resource("environments/"+env+"/keyvaluemaps",apigee_mgmt_url,org,token)
	                if status_code == 200:
	                    kvm = re.sub(r'[\[\]\"]','',kvm)
	                    kvm = kvm.strip()
	                    print("Downloading KVM : "+kvm+" ENVIRONMENT "+env )	                    
	                    path=folder_name+"/kvm/env/"+env+"/"
	                    Path(path).mkdir(parents=True, exist_ok=True)
	                    with open(path+kvm, "w") as file:
	                        file.write("KVM's are default encrypted in ApigeeX hence values cannot be retrieved")

	def Developers(apigee_mgmt_url,org,token):
	    response,status_code=DownloadResources.get_resource("developers",apigee_mgmt_url,org,token)
	    response = re.sub(r'\n','',response.text)
	    output = re.search('\[(.*?)\]', response, flags=re.IGNORECASE)
	    if output is not None:
	        all_developers = output.group(0)
	        arr_developers	= all_developers.split(',')
	        for developer in arr_developers:
	            developer = re.sub(r'[\[\]\"\{\}\s*]','',developer)
	            developer = re.sub(r'email:','',developer)
	            developer = developer.strip()
	            response,status_code=DownloadResources.get_resource("developers/"+developer,apigee_mgmt_url,org,token)
	            if status_code == 200:
	                developer = re.sub(r'[\[\]\s*\"]','',developer)
	                developer = developer.strip()
	                print("Downloading Developer : "+developer )	                
	                path=folder_name+"/devs/"
	                Path(path).mkdir(parents=True, exist_ok=True)
	                with open(folder_name+"/devs/"+developer, "w") as file:
	                    file.write(response.text)          
	
	def delete_all_existing_directory():
		path_proxies=folder_name+"/proxies/"
		if os.path.exists(path_proxies):
			shutil.rmtree(path_proxies)	

		path_apps=folder_name+"/apps/"
		if os.path.exists(path_apps):
			shutil.rmtree(path_apps)	

		path_products=folder_name+"/products/"
		if os.path.exists(path_products):
			shutil.rmtree(path_products)		


		path_target_servers=folder_name+"/targetservers/"
		if os.path.exists(path_target_servers):
			shutil.rmtree(path_target_servers)		

		path_kvm=folder_name+"/kvm/"
		if os.path.exists(path_kvm):
			shutil.rmtree(path_kvm)		

		path_dev=folder_name+"/devs/"
		if os.path.exists(path_dev):
			shutil.rmtree(path_dev)		

		path_sharedflows=folder_name+"/sharedflows/"
		if os.path.exists(path_sharedflows):
			shutil.rmtree(path_sharedflows)






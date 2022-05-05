# Apigee X Resources Download
Use this tool to download configuration, information and entities from  Apigee X Organization.

  <b>Note :</b>
  The tool supports only bearer tokens when authenticating with your Apigee X Orgs.

# Data Download
With the tool, you can download below information and entities:

  <ul>
  <li>developers</li>
  
  <li>proxies (latest revision)</li>
  
  <li>shared flows</li>
  
  <li>products</li>
  
  <li>apps</li>
  
  <li>app keys</li>
  
  <li>KVMs (only env)</li>
  
  <li>Target Servers</li>
  
</ul>

# What data cannot be Downloaded

Please note that the following entities won't be downloaded as part of this tool.

<ul>
<li>Cache resources and cached values.</li>
<li>Environment resources such as virtualhosts, and keystores.</li>
<li>KVM entries for "encrypted" key-value maps. Encrypted values can't be retrieved using the management API. Get the values you're using in your old org, then add these values manually to the new org.</li>
</ul>


# Prerequisites

<ol>
  <li>Download and install Python at https://www.python.org/downloads.</li>
  <li>Configure Below Environment Variable for Python.</li>
  <li>C:\Users\Administrator\AppData\Local\Programs\Python\Python39\Scripts\</li>
  <li>C:\Users\Administrator\AppData\Local\Programs\Python\Python39\</li>
  <li>C:\Users\Administrator\AppData\Local\Programs\Python\Python39\Lib\site-packages</li>
</ol>

# Before you get started

Before you start downloading data, be sure to do the following to ensure that your org is in a stable state when downloading.
<ul>
<li>Freeze revisions on proxies in the Apigee X org you're downloading data from.</li>
<li>Pause the process of adding new proxies or features.</li>
</ul>

# Needed Configuration

There is no configuration for this tool except for the Python Configuration.

You will need Apigee X Org Name and a fresh Bearer Token Generated on GCP Console.

<table>
  <tr>
    <td><b>Property</b></td>
    <td><b>Description</b></td>
  </tr>
  <tr>
      <td>Apigee X Org Name</td>
      <td>eg.  favarity-wings-768733</td>
  </tr>
  <tr>
      <td>Bearer Token</td>
      <td>eg.  ya29.A0ARrdaM9_Vyd3snc9yml_JwPYr6oohyFs23gKj7Po60Uwu3PL_T9oI9lJKODSXgPNuZpvFLbEI59uHJZQrN4EUQDtT8HE6KKwgcatsAU3W5MomV9_EEWoFemHhUUUbtKOAys_TW8bju-nwo8C7Yt1dqLj2rdqbuCq5LvkdwCo6HchtXvSWgAUOIISY1yg25PZLiJ2sGQSV_X_wZ1jmAURdA3zKAzbLihA5THpQfNKmzKJfpZ64d8fIbL4JnXWsZ8ONXtuPjmPpw</td>
  </tr>  
</table>

# How to Use the tool

Method 1: 

<ul>
  <li>By Cloning the Repository Code </li>
  <li>
  To use the tool, open a command prompt and change to the root directory of the repository you cloned.
  </li>  
</ul>  

Method 2: 

<ul>
  <li>By Downloading the Repository as a zip file</li>
  <li>Extract the contents of the zip file.</li>  
  <li>Open a command prompt and change to the root directory to the extracted folder.</li>  
</ul>

Once we are at the root directory in the command prompt use below command to start downloading the resources
<ul>
  <li>python apigeex_tool.py</li>
</ul>

You will presented with several options to download information,resources and entities based on your use-case.
![image](https://user-images.githubusercontent.com/19343906/166515345-70198be1-b0a1-48ca-8ba6-9dd72d7e2680.png)

There are 8 Available Options:
<ol>
  <li>Download All Resources</li>
  <li>Download Only Proxies </li>
  <li>Download Only SharedFlows </li>
  <li>Download Only Products</li>
  <li>Download Only Apps </li>
  <li>Download Only KVM </li>
  <li>Download Only Target Servers</li>
  <li>Download Only Developers</li>
</ol>

# Download Only Proxies
To download only Proxies from the Apigee X Org.
<ul>
  <li>Type <b>Proxy</b> ( Case Insensitive ) in the command prompt.</li>
</ul>

Below is the sample Screenshot.

![Screenshot (391)](https://user-images.githubusercontent.com/19343906/166897336-e5f6251d-2c81-46b6-a369-10b734dc91d7.png)

# Download Only Shared Flows
To download only Shared Flows from the Apigee X Org.
<ul>
  <li>Type <b>SF</b> ( Case Insensitive ) in the command prompt.</li>
</ul>

Below is the sample Screenshot.

![Screenshot (385)](https://user-images.githubusercontent.com/19343906/166896590-9a2bab2d-7713-4444-a5b7-e395aa63c332.png)

# Download Only Products
To download only Product from the Apigee X Org.
<ul>
  <li>Type <b>Product</b> ( Case Insensitive ) in the command prompt.</li>
</ul>

Below is the sample Screenshot.

![Screenshot (386)](https://user-images.githubusercontent.com/19343906/166896742-7dff2a2b-7f6a-44b8-be41-e2e20d34acd7.png)

# Download Only Apps
To download only Apps from the Apigee X Org.
<ul>
  <li>Type <b>APP</b> ( Case Insensitive ) in the command prompt.</li>
</ul>

Below is the sample Screenshot.

![Screenshot (387)](https://user-images.githubusercontent.com/19343906/166896851-9c2ff96b-c8e4-4ba0-abcd-22efc323cc62.png)

# Download Only KVMs
To download only KVMs from the Apigee X Org.
<ul>
  <li>Type <b>KVM</b> ( Case Insensitive ) in the command prompt.</li>
</ul>

Below is the sample Screenshot.

![Screenshot (388)](https://user-images.githubusercontent.com/19343906/166896957-9cb5682e-ff30-43f7-a310-dfaa88d524d9.png)

# Download Only Target Servers
To download only Target Servers from the Apigee X Org.
<ul>
  <li>Type <b>TS</b> ( Case Insensitive ) in the command prompt.</li>
</ul>

Below is the sample Screenshot.

![Screenshot (389)](https://user-images.githubusercontent.com/19343906/166897070-c67d1a42-942e-4f17-a240-65ce922bdf4b.png)

# Download Only Developers
To download only Developers from the Apigee X Org.
<ul>
  <li>Type <b>DEV</b> ( Case Insensitive ) in the command prompt.</li>
</ul>

Below is the sample Screenshot.

![Screenshot (390)](https://user-images.githubusercontent.com/19343906/166897194-17323a97-1139-454e-a17a-956a821b7a69.png)

# Download All Resources
To download all Resources from the Apigee X Org.
<ul>
  <li>Type <b>ALL</b> ( Case Insensitive ) in the command prompt.</li>
</ul>

Below is the sample Screenshot.

![Screenshot (393)](https://user-images.githubusercontent.com/19343906/166897523-a24baafc-e1f2-480a-ba29-58f465366420.png)



The following folder structure with data will be created in your current directory.

![image](https://user-images.githubusercontent.com/19343906/166903611-116ea3f3-2dce-4aff-a50e-125b7b08f11d.png)









# This is for Python version 3.7.  
# Created by Nate Revello 2019 Jan 18

# Meraki-API-Network-CSV-List
This takes the curl output of the Meraki API network list and re-formats it to a CSV file that's easier to read as a human.

# Meraki API Docs:
API Docs: https://dashboard.meraki.com/api_docs
To get your org id; go to the API Docs link above > Organizations > List the organizations that the user has privileges on.
To see the specific entry on the curl command for the Network list; go to the API Docs link above > network > List the networks in an organization.

# Example Curl Command:
Here's an example of the curl command for a windows machine: (**Note: the double quotes for a windows box.  Use single quotes for a linux box.  Also fill out your org ID and API key.):
      curl -L -H "X-Cisco-Meraki-API-Key: <your api key here>" -H "Content-Type: application/json" -X GET "https://api.meraki.com/api/v0/organizations/<your org id here>/networks"
  
# To run this script on a windows box:
Save the Network List curl output to a file named "Network list.txt" in the same directory as the script.  The output will be a single line.
Open a CMD prompt. 
cd to the directory of the script. 
Verify the curl output is saved as "Network list.txt"
Run 'py MerakiNetworkIDReformatScript.py' in the cmd prompt

After the script runs, you'll have a csv file created in the same directory as the script.  It can then be opened in your spreadsheet software.

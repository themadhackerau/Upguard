import requests
import json


api_key = "Enter your API Key Here"
url = "https://cyber-risk.upguard.com/api/public/typosquat"

#Add Authorisation Header for API Key
headers = {
  'Authorization': api_key
}

#Get list of Domains with TypoSquatting enabled, iterate through and get the details for any typosquatting domains

#Send GET Request to Upguard API and retrieve JSON Response
response = requests.request("GET", url, headers=headers)
jsonresponse= response.json()

#Iterate through the JSON Reponse to retrieve domain name and retriee typosquatting details for each
for domain in jsonresponse["domains"]:
    print(domain["domain"])
    params = {'domain': domain["domain"]}
    detailresponse = requests.request("GET", url + '/details', headers=headers, params=params)
    details = detailresponse.json()
    pretty = json.dumps(details, indent=4)
    print(pretty)

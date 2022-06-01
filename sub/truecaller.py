import  requests

#headers required and bearer is authorization token

head={
    "Host": "search5-noneu.truecaller.com",
    "authorization": "Bearer a1i0Q--YLbhyeF9-Wrv86LslFomuMonYQBfGiV5X-ma5m_EXKgSZPWn_R6K0SJaS",
    "accept-encoding": "gzip",
    "user-agent": "Truecaller/11.66.7 (Android;10)"
 } 
  
def main(num):

    url='https://search5-noneu.truecaller.com/v2/search?countryCode=BD&type=4&locAddr=&placement=SEARCHRESULTS%2CHISTORY%2CDETAILS&adId=&encoding=json&q='+str(num)
    req=requests.get(url,headers=head)
    data=req.json()
    if data:
        name=data['data'][0]['name'] if data['data'] else None                
        carrier=data['data'][0]['phones'][0]['carrier']  if data['data'][0]['phones'] else None
        email=data['data'][0]['internetAddresses'][0]['id']  if data['data'][0]['internetAddresses'] else None
        address=data['data'][0]['addresses'][0]['city']  if data['data'][0]['addresses'] else None
        info = [name,carrier,email,address]
        info = list(filter(None,info))

    
         
    return info



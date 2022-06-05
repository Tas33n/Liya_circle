import  requests

#headers required and bearer is authorization token

head={
    
 } 
  
def main(num):

    url='https://redthryssa.xyz/numberlookup.php?id='+str(num)
    req=requests.get(url,headers=head)
    data=req.json()
    if data:
        name=data['data'][0]['name'] if data['data'] else None       
        gender=data['data'][0]['gender'] if data['data'] else None                   
        carrier=data['data'][0]['phones'][0]['carrier']  if data['data'][0]['phones'] else None
        phone=data['data'][0]['phones'][0]['e164Format']  if data['data'][0]['phones'] else None
        email=data['data'][0]['internetAddresses'][0]['id']  if data['data'][0]['internetAddresses'] else None
        address=data['data'][0]['addresses'][0]['address']  if data['data'][0]['addresses'] else None
        img=data['data'][0]['image'] if data['data'] else None   
        info = [img,"User infos",name,phone,carrier,email,address]
       # info = ("name: ", name, )
        info = list(filter(None,info))

    
         
    return info



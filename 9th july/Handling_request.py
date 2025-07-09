import requests
# writing image on local file
r = requests.get('https://i.natgeofe.com/k/07176791-9577-4e31-b101-b10ca7ca9a3c/Stripes_Tiger-Terrific_KIDS_0722.jpg?wp=1&w=1084.125&h=721.875')
with open('tiger.png' ,mode ='wb') as f:
    f.write(r.content)

#posting data
payload  = {'Username':'Haris', 'Password':'Haris@238'}
r= requests.post('https://httpbin.org/post' , data=payload)
print(r.json())

#checking responses
r = requests.get('https://httpbin.org/basic-auth/Haris/Haris@238' , auth=('Haris', 'Haris@238'))
print(r) #response 200 (success)

r = requests.get('https://httpbin.org/basic-auth/Haris/Haris@238' , auth=('Hais', 'Haris@238'))
print(r) #response 401 (auth failed)

#timeout
r = requests.get('https://httpbin.org/delay/3' , timeout=2)
print(r)

r = requests.get('https://httpbin.org/delay/3' , timeout=5)
print(r)
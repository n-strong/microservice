import requests

url = "http://localhost:5000/blog_post"

blog_post = {'user1':'My name is noah strong and I am posting this to my personal blog.'}

response = requests.post(url, json=blog_post)

print('\nResponse status code: \n', response.status_code) 
print(response.text)

import pandas as pd
import requests


url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

posts = response.json()
df = pd.DataFrame(posts)
# filter_post = [post for post in posts if post["userId"]==1]

result = df[(df['userId'] == 1)]

with open("posts.txt", "w", encoding="utf-8") as file:
        for index,row in result.iterrows():
            file.write(f"Title: {row['title']}\n")
            file.write(f"Body: {row['body']}\n")
            file.write("-" * 40 + "\n")
            


# for index, row in result.iterrows():
#     print("Title:", row['title'])
#     print("body:", row['body'])
#     print("-" * 40)

# for post in filter_post:
#     print(post)
 
# print("Total posts",len(posts))
# for post in posts[:5]:
#     print("Title:",post['title'])
#     print("body:",post['body'])
#     print("-" * 40)
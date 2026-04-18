import requests 

def search_app():
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url)
        posts = response.json()
        print(posts)
    except Exception as e:
        print(f"Error fetching data: {e}")
        return

    keyword = input("enter keyword for search item").lower()
    found_count = 0

    for post in posts:
        if keyword in post["title"].lower():
            print(f"✅ Found: {post['title']}\n UserId: {post['userId']}\n PostId:{post["id"]}")
            found_count +=1


    if found_count == 0:
        print("❌ No posts matched your keyword.")
    else:
        print(f"\nTotal matches found: {found_count}")

if __name__ == "__main__":
    search_app()            

    
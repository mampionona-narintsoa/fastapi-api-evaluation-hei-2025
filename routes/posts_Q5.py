@app.get("/posts")
def get_posts():
    return posts_db
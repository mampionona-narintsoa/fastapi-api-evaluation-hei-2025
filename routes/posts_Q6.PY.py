@app.put("/posts")
def upsert_post(post: Post):
    for i, existing_post in enumerate(posts_db):
        if existing_post.title == post.title:
            posts_db[i] = post
            return {"message": "Post updated", "post": post}
    posts_db.append(post)
    return {"message": "Post added", "post": post}
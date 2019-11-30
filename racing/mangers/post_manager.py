def generate_post_response(post):
    return {
        "id": post.id,
        "biker_id": post.biker_id,
        "status": post.status
    }

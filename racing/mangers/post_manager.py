def generate_post_response(post):
    return {
        "id": post.id,
        "biker_id": post.biker_id,
        "is_active": post.is_active,
        "like_number": post.like_number,
        "share_number": post.share_number,
        "view_number": post.view_number,
        "title": post.title,
        "description": post.description,
        "created_time": post.created_time,
        "updated_time": post.updated_time
    }

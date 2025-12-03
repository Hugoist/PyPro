from django.shortcuts import get_object_or_404
from ninja import Router

from app.api.auth import auth
from app.models.blog import Post, Tag, Comment
from app.schemas.blog import (
    TagSchema, TagCreateSchema,
    CommentSchema, CommentCreateSchema,
    PostSchema, PostCreateSchema, PostUpdateSchema
)

router = Router(tags=["Blog"])


@router.post("/tags", response=TagSchema, auth=auth)
def create_tag(request, payload: TagCreateSchema):
    tag = Tag.objects.create(name=payload.name)
    return tag


@router.get("/tags", response=list[TagSchema])
def list_tags(request):
    return Tag.objects.all()


@router.post("/posts", response=PostSchema, auth=auth)
def create_post(request, payload: PostCreateSchema):
    post = Post.objects.create(
        author=request.user,
        title=payload.title,
        content=payload.content,
    )

    if payload.tag_ids:
        post.tags.set(payload.tag_ids)

    return post.to_dict()


@router.get("/posts", response=list[PostSchema])
def list_posts(request):
    qs = Post.objects.all().prefetch_related("tags", "comments", "author")

    return [post.to_dict() for post in qs]


@router.get("/posts/{post_id}", response=PostSchema)
def get_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    return post.to_dict()


@router.put("/posts/{post_id}", response=PostSchema, auth=auth)
def update_post(request, post_id: int, payload: PostUpdateSchema):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        return {"error": "Forbidden"}

    if payload.title:
        post.title = payload.title
    if payload.content:
        post.content = payload.content
    if payload.tag_ids is not None:
        tags = Tag.objects.filter(id__in=payload.tag_ids)
        post.tags.set(tags)

    post.save()

    return post.to_dict()


@router.delete("/posts/{post_id}", auth=auth)
def delete_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        return {"error": "Forbidden"}

    post.delete()
    return {"success": True}


@router.post("/posts/{post_id}/comments", auth=auth, response=CommentSchema)
def create_comment(request, post_id: int, payload: CommentCreateSchema):
    post = get_object_or_404(Post, id=post_id)

    comment = Comment.objects.create(
        post=post,
        author=request.user,
        text=payload.text
    )

    return comment.to_dict()


@router.get("/posts/{post_id}/comments", response=list[CommentSchema])
def list_comments(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    qs = post.comments.all()

    return [comment.to_dict() for comment in qs]

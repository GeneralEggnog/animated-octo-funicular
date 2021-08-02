from flask import render_template, url_for, flash, redirect, request, Blueprint
from flaskblog.posts.forms import PostForm, CommentForm
from flaskblog import db
from flaskblog.models import Post, Comment
from datetime import datetime


posts = Blueprint('posts', __name__)


comment_per_page = 5

@posts.route("/blog")
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=comment_per_page)
    return render_template("blog.html", posts = posts, title='Blog')

@posts.route("/blog/post/<int:post_id>", methods=["GET", "POST"])
def post(post_id):
    page = request.args.get('page', 1, type=int)
    blogpage = request.args.get('blogpage', 1, type=int)
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    comments = Comment.query.filter_by(post=post).order_by(Comment.date_posted.desc()).paginate(page=page, per_page=5)
    if form.validate_on_submit():
        comment = Comment(author=form.name.data, content=form.comment.data, post=post)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('posts.post', post_id=post.id, _anchor="comments"))
    return render_template('post.html', title=post.title, post=post, form=form, comments=comments, blogpage=blogpage)

@posts.route("/blog/post/<int:post_id>/edit", methods=["GET", "POST"])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.last_updated = datetime.utcnow()
        db.session.commit()
        flash('Post updated!', 'success')
        return redirect(url_for('posts.post',post_id = post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form =form, legend='Edit Post')

@posts.route("/blog/post/<int:post_id>/delete")
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(post_id=post_id)
    for comment in comments:
        db.session.delete(comment)
    db.session.delete(post)
    db.session.commit()
    flash('Post has been deleted!', 'danger')
    return redirect(url_for('posts.blog'))

@posts.route("/blog/post/<int:post_id>/deletecomment")
def delete_comment(post_id):
    comment_id = request.args.get('comment_id')
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    flash('Comment has been deleted!', 'danger')
    return redirect(url_for('posts.post', post_id=post_id, _anchor="comments"))



@posts.route("/blog/new_post", methods=["GET", "POST"])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        flash('Post created!', 'success')
        return redirect(url_for('posts.blog'))
    return render_template ('create_post.html', title = 'Create Post', form = form, legend="New Post")


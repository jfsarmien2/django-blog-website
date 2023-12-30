from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "https://media.istockphoto.com/id/1457497595/photo/couple-relaxing-on-hiking-trip-in-the-mountains.jpg?s=612x612&w=0&k=20&c=OAhA1XmsSjE-_NoPRSQ6vI0_GMGsSJhtfVxHs4o5Di0=",
        "author": "JS",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "https://media.istockphoto.com/id/1432260067/photo/a-cheerful-man-sits-at-a-conference-table-across-from-his-two-female-colleagues-and-learns-to.jpg?s=612x612&w=0&k=20&c=-R9hSEjFjK1mQVglesouou3Wsq2qZQ5tsP2quKkYnRY=",
        "author": "JS",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "https://media.istockphoto.com/id/1224590498/photo/sunlight-shines-through-trees-in-the-forest.jpg?s=612x612&w=0&k=20&c=clGApzNAdqI8eK0Vzbf-iap0TVPGkK-84U8aRDFozVA=",
        "author": "JS",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]


def get_date(post):
    return post["date"]

# Create your views here.


def blog_index(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_posts})


def blog_posts(request):
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})


def blog_detail(request, slug):
    blog_post = next(post for post in all_posts if post['slug'] == slug)

    return render(request, "blog/post-info.html", {"post": blog_post})

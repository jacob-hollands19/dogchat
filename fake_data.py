dogs = [
    {
        "name" : "Melba",
        "handle" : "melba",
        "bio" : "Hi, I'm Melba! I'm a mini-goldendoodle and I love to play.",
        "age" : 3
    },
    {
        "name" : "Charlie",
        "handle" : "chucky",
        "bio" : "Hi I'm Charlie! I'm a big white standard poodle.",
        "age" : 7
    },
    {
        "name" : "Rosie",
        "handle" : "rose",
        "bio" : "Hi I'm Rosie! I'm from the hard streets of LA, don't mess with me.",
        "age" : 9
    }
]

def get_dog_by_handle(handle):
    for dog in dogs:
        if dog['handle'] == handle:
            return dog
    return None

posts = [
    {
        "Postee": "melba",
        "Post": "I'm so excited to move to California!",
        "LikedBy": "chucky, rose, tyler",
        "Likes": "3",
        "Reposts": "5"
    },
    {
        "Postee": "melba",
        "Post": "Great game of fetch today with my Dad, Paul",
        "LikedBy": "chucky, rose, tyler",
        "Likes": "3",
        "Reposts": "1"
        
    },
    {
        "Postee": "chucky",
        "Post": "Took a great 8 hour nap today, then guarded the household",
        "LikedBy": "melba, tyler",
        "Likes": "2",
        "Reposts": "19"
    },
    {
        "Postee": "melba",
        "Post": "Peanut butter is my favorite snack!",
        "LikedBy": "chucky, rose",
        "Likes": "3",
        "Reposts": "5"
    },
    {
        "Postee": "rose",
        "Post": "Today I stole food from a blind dog.",
        "LikedBy": "chucky",
        "Likes": "1",
        "Reposts": "2"
    },
    {
        "Postee": "rose",
        "Post": "Today my owner fed me ramen.",
        "Likes": "",
        "Likes": "0",
        "Reposts": "3"
    }
]

def get_posts_by_handle(handle):
    results = []
    temp = []
    for post in posts:
        if post['Postee'] == handle:
            temp.append(post['Postee'])
            temp.append(post['Post'])
            results.append(temp)
            temp = []
    return results


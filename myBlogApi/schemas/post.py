from datetime import date

today = date.today()

def postEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "title":item["title"],
        "content":item["content"],
        "postedDay": today.strftime("%d/%m/%Y"),

    }

def postsEntity(entity) -> list:
    return [postEntity(item) for item in entity]
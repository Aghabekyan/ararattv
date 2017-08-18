from main.models import *
from random import randint
for number in range(1, 100000):
    from django.contrib.auth.models import User
    cat = Category.objects.get(pk=randint(1, 6))
    ct = Content.objects.get(pk=randint(21, 24))
    print number
    obj = Content(
        title=ct.title,
        desc=ct.desc,
        img=ct.img,
        video=ct.video,
        general_slider=1,
        news_line=1,
        publish_date=ct.publish_date,
        create_date=ct.create_date,
    )
    obj.save()
    obj.category.add(cat)

print 5

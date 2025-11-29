import time
from scop.models import Review

start = time.time()
reviews = list(Review.objects.filter(rating__gte=4))
print(time.time() - start)


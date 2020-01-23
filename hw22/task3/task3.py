from hw22.models import *
from django.db.models import Count

group1 = MusicBand.objects.create(name='group1', year_of_foundation=2000, genre='pop')
album1 = Album.objects.create(title='album1', group=group1)
track = Track.objects.create(title='track1', album=album1)

# Получение всех альбомов группы
all_group_albums = group1.album.all()

# Получение всех треков альбома
all_album_tracks = album1.track.all()

# Получение всех треков группы
MusicBand.objects.aggregate(Count('album__track'))

# Получение всех альбомов, группы которых были основаны в 1990 году
Album.objects.filter(group__year_of_foundation=1990)

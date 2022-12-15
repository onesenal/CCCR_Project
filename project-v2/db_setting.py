DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'travelinfo',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'db-svc.default.svc.cluster.local',
        'PORT': '3306',
    }
}

SECRET_KEY = 'c+2gan!)%kjm&xp3xtbnv#nw734-l_&(qa$rxdd4(1oee2tso('
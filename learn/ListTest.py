movies = ["The Holy Grail",
          "The Life of Brian",
          "The Meaning of Life"
]
cast = ["Cleese",
        "Palin",
        movies,
        "Jones",
        "Idle"
        ]
cast.append("Gilliam")

for i in cast:
    if isinstance(i,list):
        for j in i:
            print(j)
    else:
        print(i)
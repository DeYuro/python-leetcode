def get_names(names):
    return [v for v in names if len(v) == 4]

print(get_names(['asdv','vcsds','sws', 'sdfs']))
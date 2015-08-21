import urllib

def quote_groupdict(groupdict, quotelist):
    return dict(map(lambda (k,v): (k, urllib.quote(v)) if k in quotelist else (k, v), groupdict.iteritems()));

def quote_group(group, quotelist):
    if group is None:
        group = []
    return [urllib.quote(v) if k in quotelist else v for (k, v) in zip(map(str, range(len(group))), group)]

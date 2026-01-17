def TOC(text):
    res=[]
    c=0
    s=0
    for i in text:
        if i.startswith("##"):
            s+=1
            title=i[3:]
            res.append(f"{c}.{s}. {title}")
        elif i.startswith("#"):
            c+=1
            title=i[2:]
            s=0
            res.append(f"{c}. {title}")
        else:
            continue
    return res
            
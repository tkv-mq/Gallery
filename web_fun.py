def save_data(text, url):
    if text and url:
        basefile = open('data.txt', 'a+', encoding='utf-8')
        text = '<st>' + text + '<st>'
        url = '<ur>' + url + '<ur>'
        basefile.write(text + url + '\n')
        basefile.close()
        return True
    else:
        return False

def read_data(name):
    basefile = open('data.txt', 'r+', encoding='utf-8')
    lst = []
    if name == 'text':
        for row in basefile:
            if row.split('<st>')[1]:
                lst.append(row.split('<st>')[1])
    elif name == 'url':
        for row in basefile:
            if row.split('<ur>')[1]:
                lst.append(row.split('<ur>')[1])
    else:
        return False
    basefile.close()
    return lst
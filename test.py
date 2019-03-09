lst = ['C:\\CicadaInc\\whois\\test_versions\\fotoVerification/dimas.jpg',
       'C:\\CicadaInc\\whois\\test_versions\\fotoVerification/dima_2.jpg',
       'C:\\CicadaInc\\whois\\test_versions\\fotoVerification/dima_passport.jpg',
       'C:\\CicadaInc\\whois\\test_versions\\fotoVerification/group.jpg']
for i in range(len(lst)):
    lst[i] = lst[i].replace('\\', '/')
print(lst)
print(lst[0].replace('\\', '/'))

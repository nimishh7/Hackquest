life = '526172211A0700CE997380000D00000000000000E58715565537BE2D27843B7C2FD41A25C5A71DEB625717152E17EB0037B4F03503BB5C944D219F12C5C01A55326C8557D98991FC930D7F5BC84FA892049B6210D69927676C0D0E5746D05F13F12FCAE0F53A48B77FDFE02BDCADDA32FC7CF1FEA91322D1BE88B185035AFAFC0E38A77E053232DDDBBE049741E89B85F35ACB7E70C08885A53ED3DFE58715565537BE2DA97AFC2B961ECA5A929B074205B9EF31'
fp = open('test.rar', 'wb')
for c in range(len(life) / 2):
    fp.write(chr(int(life[c * 2:(c + 1) * 2], 16)))

class TxtUtils :
    def clean_txt(txt):
        import re
        p1 = re.compile(r'-\{.*?(zh-hans|zh-cn):([^;]*?)(;.*?)?\}-')
        p2 = re.compile(r'[(][: @ . , ？！\s][)]')
        p3 = re.compile(r'[「『]')
        p4 = re.compile(r'[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）0-9 , : ; \-\ \[\ \]\ ]')
        txt = p1.sub(r' ', txt)
        txt = p2.sub(r' ', txt)
        txt = p3.sub(r' ', txt)
        txt = p4.sub(r' ', txt)
        return txt
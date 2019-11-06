import sys
import xmltodict
import json

'''
辞書型の中身をエクスポート(JSONファイル)したい形に整形する
'''
def ParseDic(dic):
    return dic

def main():
    args = sys.argv
    xmlf = args[1]
    jsonf = xmlf.split(".")[0] + ".json"

    with open(xmlf) as fdr:
        dic = xmltodict.parse(fdr.read())
        # transform dictionary
        pdic = ParseDic(dic)
        result = json.dumps(pdic, ensure_ascii=False, indent=2)

        # file wrte
        with open(jsonf, "w") as fdw:
            fdw.write(result)

if __name__ == '__main__':main()


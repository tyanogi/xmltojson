# xmlファイルをjsonファイルに変換する
## 環境構築
```
$ pip install -r requirements.txt

```

## 実行方法
```
$ python main.py <XMLFileName>
```

## 一括変換する方法
```
$ find *.xml | xargs -I {} python main.py {}
```


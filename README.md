#taiker&listenerコマンド
* talkerで送った文字列をlistenerに表示する

![test](https://github.com/Takumi-Fukazawa/mypkg/actions/workflows/test.yml/badge.svg)


## ダウンロード方法
*  操作
 ```
 $ git https://github.com/Takumi-Fukazawa/mypkg/tree/master /#手元にリポジトリをコピー`
 $ cd ~/ros2_ws/src/mypkg/mypkg                             /#作られたディレクトリに移動
````
このディレクトリ内で以下のコマンドを実行できる

## デモンストレーション
talkerで送った文字列をlistenerに表示する。
* 使用例
 * 端末1(talker)
```
 $ ros2 run mypkg talker             　　　　 /#実行
 $ 文字列を入力してください Hello everyone.   /#「文字列を入力してください｝の後に任意の文字列を入力してEnter
 $ 文字列を入力してください こんにちは皆さん。
 $ 文字列を入力してください Nice to meet you.
 $ 文字列を入力してください よろしくお願いします。

```
 * 端末2(listener)
```
 $ ros2 run mypkg listener                     /#実行
 $ [INFO] [1672389632.282577500] [listener]: Listen: person_msgs.msg.Person(message='Hello everyone.', log=1) 
 /#～(message='[talkerから送られてきた文字列]', log=[送られてきた順に割り振られた番号])が表示される
 $ [INFO] [1672389643.553213700] [listener]: Listen: person_msgs.msg.Person(message='こんにちは皆さん。', log=2)
 $ [INFO] [1672389650.016655300] [listener]: Listen: person_msgs.msg.Person(message='Nice to meet you.', log=3)
 $ [INFO] [1672389657.427276700] [listener]: Listen: person_msgs.msg.Person(message='よろしくお願いします。', log=4)

```
## 必要なソフトウェア
* Python
  * テスト済み: 3.7〜3.10

## テスト環境
* Ubuntu 22.04

## ライセンス
* このソフトウェアパッケージは、3条項BSDライセンスの下、再配布および使用が許可されます。
  * [LICENSE](https://github.com/Takumi-Fukazawa/mypkg/main/LICENSE)
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
  * [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* ©　2022 Takumi Fukazawa



# taiker&listenerコマンド
* ランダムに生成したアルファベットの文字列をlistenerに表示する

![test](https://github.com/Takumi-Fukazawa/mypkg/actions/workflows/test.yml/badge.svg)


## ダウンロード方法
*  操作
 ```
 $ git https://github.com/Takumi-Fukazawa/mypkg/tree/master /#手元にリポジトリをコピー`
 $ cd ~/ros2_ws/src/mypkg/mypkg                             /#作られたディレクトリに移動
````
このディレクトリ内で以下のコマンドを実行できる

## デモンストレーション
 ランダムに生成したアルファベットの文字列をlistenerに表示する
* 使用例
  * 端末1(talker)
```
 $ ros2 run mypkg talker             　　　　 /#実行(Ctrl+Cで終了)

```
    * 端末2(listener)
```
 $ ros2 run mypkg listener                     /#実行
 $ [INFO] [1672476341.589967700] [listener]: Listen: person_msgs.msg.Person(message='hClbzDgknY', log=19)
 /#～(message='[ランダムに生成したアルファベットの文字列]', log=[送られてきた順に割り振られた番号])が表示される
 $ [INFO] [1672476342.081379000] [listener]: Listen: person_msgs.msg.Person(message='CkvxgLpHDW', log=20)
 $ [INFO] [1672476342.580624000] [listener]: Listen: person_msgs.msg.Person(message='fKTDsh7b80', log=21)
 $ [INFO] [1672476343.080695800] [listener]: Listen: person_msgs.msg.Person(message='r1Wr3Afu4P', log=22)
 $ [INFO] [1672476343.580590200] [listener]: Listen: person_msgs.msg.Person(message='IxCPxZJTNK', log=23)
 $ [INFO] [1672476344.080744400] [listener]: Listen: person_msgs.msg.Person(message='vRObnWJqAY', log=24)

```
## 必要なソフトウェア
* Python
  * テスト済み: 3.7〜3.10
* ROS2

## テスト環境
* Ubuntu 22.04

## ライセンス
* このソフトウェアパッケージは、3条項BSDライセンスの下、再配布および使用が許可されます。
  * [LICENSE](https://github.com/Takumi-Fukazawa/mypkg/blob/master/LICENS)
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
  * [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* ©　2022 Takumi Fukazawa


# 目的
サイステビンスシステム（si stebbins system）によるカード当ての練習をするためのプログラムです。

wadeさんの動画：【[混ぜた状態でも相手のカードの位置がわかってしまうあの名作を解説](https://youtu.be/BYR49QezWo0)】をもとに作りました。

# 使用方法


# 注意
- 目的の練習をできればよいので例外処理を記述していない簡素な作りになっています。
- 一番下の4枚のカードの組み合わせはお好みで変更してください（先に示したwadeさんの動画では「1-4-7-10」の組み合わせですが、ここでは「4-7-10-13」としました）。
- 一番下の4枚のカード（ダイヤ4、クラブ7、ハート10、スペード13）を求めたい場合は、差がマイナスになるパターンつまりそれらに+13してから計算します（`from_top`関数の`else`節）。

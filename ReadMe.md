# cps学習用 ハードウェア

以下に実世界で動かす場合の方法を記載する．

手順は次の通りである．

1. ハードウェアの準備
1. Raspbeery pi用のソフトウェアの構築

## ハードウェア準備
- 必要な物品
    - [Dynamixel contorller](https://www.besttechnology.co.jp/modules/onlineshop/index.php?fct=photo&p=291)
        - これは代替品でも構わない
    - Dynamixel 電源供給基盤部品
        - ユニバーサル基盤
        - [JSTコネクタ](https://e-shop.robotis.co.jp/product.php?id=373)
            -購入先は一例
        - 電源用コネクタ
            - XT60を推奨
        - 配線
    - Sensor接続用基盤部品
        - [2 x 20 pin コネクタ](https://jp.misumi-ec.com/vona2/detail/222000486813/?HissuCode=PS-40SD-D4C2)
        - [コネクタ用コンタクト](https://jp.misumi-ec.com/vona2/detail/222000484057/?HissuCode=030-51307-001)
        - [レベルコンバータIC](https://ssci.to/2375)
        - 配線
- 組み立て
    - Dynamixel 電源供給基盤部品
        - JSTコネクタ1番ピンをGND,2番ピンに電源を供給するようにする．
    - Sensor接続用基盤部品
        - 以下通りに配線を行う．
            | 2x20 pin コネクタ| レベルコンバータIC | Grove Connector|
            | ---- | ---- | ---- |
            | pin 1 (3.3V) | pin 1 (VCC A) | - |
            | pin 5 (SDL) | pin 3 (SCLA) | - |
            | pin 3 (SDA) | pin 2 (SDAA) | - |
            | pin 2 (5V) | pin 8 (VCCB) | pin 3 (VCC) |
            | - | pin 7 (SDLB) | pin 1 (SDL) |
            | - | pin 6 (SDAB) | pin 2 (SDA) |
            | pin 6 (GND) | pin 4 (GND) | pin 4 (GND)|
            |-|pin 5 (EN)|-|


## Raspbeery pi 構築
1. OSイメージをmicro sdへコピーする．
    - [この](https://ascii.jp/elem/000/004/094/4094421/)ページを参考にUbuntu 22.04.2 (64bit)をインストールする．
1. micro sdをraspbery piへ挿入し，起動する．
    - 起動した後初回セットアップでユーザー名やパスワードの設定を求められるので適切に入力する．
    - 自動的に再起動となり，そのあとログインを行う．
1. ターミナルを立ち上げ，以下操作を行う．
    1. 必要ソフトウェアをインストールする．
        ```
        apt update
        apt install -y git curl ssh
        ```
    1. dockerのインストールする．
        ```
        curl https://get.docker.com | sh
        sudo usermod -aG docker ${USER}
        ```
    1. 一度再起動し，再度ログインする．
    1. 本リポジトリをクローンする．
        ```
        cd ~
        git clone --recursive https://github.com/Hiroaki-Masuzawa/cps_rpi_docker.git
        ```
    1. docker imageのビルドする．(注意:2~3時間程度かかる)
        ```
        cd ~/cps_rpi_docker/docker 
        ./build.sh
        ```
    1. ソースのビルドをする．
        ```
        cd ~/cps_rpi_docker/docker 
        ./source_build.sh
        ```
    1. デバイスの初期設定値を変更する．
        ```
        cd ~/cps_rpi_docker
        sudo cp udev/99-udev.rules /etc/udev/rules.d/. 
        sudo udevadm control --reload-rules
        sudo udevadm trigger
        ```

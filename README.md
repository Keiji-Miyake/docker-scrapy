# docker-scrapy

## vscode remote container

Remote Developmentをインストール。
open in containerで、docker containerが立ち上がりコンテナ内で操作できる。

## vscode以外

```shell
cd .devcontainer
docker-compose up -d
docker-compose exec python bash
cd src
```

## create a scrapy project

```shell
scrapy startproject [projectname]
```

## create a crawler

```shell
cd [projectname]
scrapy genspider [projectname]_spider [target_domain]
```

## run crawl

```shell
scrapy crawl [projectname]_spider
# ファイルに出力
scrapy crawl [projectname]_spider -o [filename].json
```

# simple app for generate test data in elasticsearch

for generate some data like this
```bash
curl -XGET "http://localhost:9200/_cat/indices?s=index"

yellow open customer4.logs-2022.02.21 XAlL3XfYT8iGeuoNnIcjzQ 1 1   1 0  37.5kb  37.5kb
yellow open customer1.logs-2022.02.19 LgsvYGvSSS6T8PRkH5G2Iw 1 1   1 0  18.1kb  18.1kb
yellow open customer4.logs-2022.02.20 9_yXDsBjQqKXikrYcgWElw 1 1   1 0  37.5kb  37.5kb
yellow open customer5.logs-2022.02.19 sLQyeimzS7aSdwx-dRq_9g 1 1   1 0 128.1kb 128.1kb
yellow open customer1.logs-2022.02.20 yFAvChg3QSGdPCRbKw_SFg 1 1   1 0  18.1kb  18.1kb
yellow open customer4.logs-2022.02.19 CDmizaYCQLeHURdrrCf45g 1 1   1 0  37.5kb  37.5kb
yellow open customer1.logs-2022.02.21 Agbk6AXBTk-t_OqrzInxbQ 1 1   1 0  18.1kb  18.1kb
yellow open customer5.logs-2022.02.20 KNOhhtFLTuiJBphJbifThg 1 1   1 0 128.1kb 128.1kb
yellow open customer5.logs-2022.02.21 OHpojuLrQAaNmFmeQTf7Gg 1 1   1 0 128.1kb 128.1kb
```

## How to run
```bash
# run elasticsearch
docker-compose up -d

# run with IDE or in console
python main.py
```




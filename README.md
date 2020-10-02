# ORI-TEST

## Build image:
```sudo docker build --tag ori_test:1.0 .```

## Run image:
```sudo docker run -e SOURCE_FOLDER={source folder} -e DEST_FOLDER={destination folder} -e SOURCE_FORMAT='{source format} -e DEST_FORMAT={destination format} ori_test:1.0```

### Example
```sudo docker run -e SOURCE_FOLDER='/data/markup' -e DEST_FOLDER='/result/markup' -e SOURCE_FORMAT='internal' -e DEST_FORMAT='internal_csv' ori_test:1.0```

### Note
At this time, source data is taken from host using Dockerfile and located in 'data/markup' directory. I'm working on it 

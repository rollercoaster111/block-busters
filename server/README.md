# bbserver

Implementation of blockchain based on [hypnopump's `pysimplechain`](https://github.com/hypnopump/pysimplechain).

Run this server with the following:

``` shell
python bbserver.py

```

## api methods

#### [POST] `/add`

* : add a block to the chain

- input is a json ojbect of the form

```json
{
    "temp": 22.1,
    "rh": 55,
    "timestamp": "YYYY-MM-DDTHH:MM:SSZ"
}
```


#### [GET] `/chain`

* : show current chain


#### [GET] '/{block_hash}'

* : retrieve the data in a block

## Start docker compose

- Start docker
- Run `docker compose up` (may require elevated access)
    - The command will download the necessary images, build them and start the services.
- To stop, press `CTRL` + `c`

## HTTP Requests

Once starting the docker compose process, the gateway container will be reachable through localhost:8080 using http requests. Requests should be asking for a math operation and should use a query to pass the operands, otherwise a 404 error will be returned.

Available queries:
- `/math/<op>?a=<a>&b=<b>` where:
    - `<op>` can be one of `[add, sub, mul, div, mod]`
    - `<a>` and `<b>` are any numbers.
- `/str/<op>?a=<a>&b=<b>` where:
    - `<op>` can be one of `[lower, upper, concat, editdistance]`
        - The Levenshtein edit distance between two strings is the number of individual single-character changes (insert, delete, substitute) necessary to change string `a` into `b`.
    - `<a>` and `<b>` are any strings.
    - if `<op>` is `lower` or `upper`, the `b` argument can be omitted and it is ignored by default.

Example queries:
- http://localhost:8080/math/add?a=2&b=3
    - This should return a json with an element `s` with the value `5`.
- http://localhost:8080/math/div?a=7&b=3
    - This should return a json with an element `s` with the value `2.333333...`
- http://localhost:8080/str/upper?a=ciao
    - This should return a json with an element `res` with the value `CIAO`.
- http://localhost:8080/str/concat?a=Hello&b=%20World!
    - This should return a json with an element `res` with the value `Hello World!`.
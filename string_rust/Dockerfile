FROM rust:latest

ADD . /string_rust
WORKDIR /string_rust

RUN cargo install --path .

EXPOSE 5000

CMD ["string_rust"]
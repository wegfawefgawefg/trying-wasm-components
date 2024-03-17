make ur venv
python3 -m venv venv

you need componentize-py
pip install componentize-py

componentize-py -d filename.wit -w packagename bindings .

the above command spits out template folder with your type defs and unimplemented functions

then you make an implementation python file, and you have to mow over the abstract base class of your wit file with the same name class in your implementation file or the componentize tool wont be able to find it

then you can build your component 
componentize-py -d ./somemath.wit -w somemath componentize fmath -o fmath.wasm
where somemath.wit is the witfile, somemath is the package name, fmath.py is the name of the implementation file

## then devops time:

you need a specific version of the rust compiler
rustup install 1.76.0
rustup default nightly-2024-02-04

you need wasm-tools
cargo install wasm-tools

you need the wasm32-wasi stuff 
rustup target add wasm32-wasi

you also need the python wasmtime stuff
pip3 install wasmtime

now you build the wasm automatic bindings for the manual bindings you made. what the fuck??
python3 -m wasmtime.bindgen fmath.wasm --out-dir fm

this errors out for me. i cant get past this part. let alone importing into another langauge
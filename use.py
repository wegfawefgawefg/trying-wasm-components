from fmath import Root, RootImports
from wasmtime import Store


def main():
    store = Store()
    component = Root(
        store,
        RootImports(
            poll=None,
            monotonic_clock=None,
            wall_clock=None,
            streams=None,
            filesystem=None,
            random=None,
            environment=None,
            preopens=None,
            exit=None,
            stdin=None,
            stdout=None,
            stderr=None,
        ),
    )
    print("1 + 2 = ", component.add(store, 1, 2))


if __name__ == "__main__":
    main()

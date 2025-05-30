@typing.no_type_check
def import_data(path: str, verbose: int = 0) -> Tuple[str, str]:
    """Read data from file"""
    try:
        if verbose > 0:
            print(f"path = {path}")
        with open(path + "_example", encoding="utf-8") as fp:
            example_data = fp.read().strip()
        with open(path, encoding="utf-8") as fp:
            full_data = fp.read().strip()
        return (example_data, full_data)
# pylint: enable=unused-variable
    except OSError as exception:
        print(repr(exception))
        raise SystemExit(1) from exception

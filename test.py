import pytest

from main import run_etl_process


def test_full_process():
    data_path = 'SUBTLEXus74286wordstextversion.tsv'
    run_etl_process(data_path)


if __name__ == '__main__':
    pytest.main()
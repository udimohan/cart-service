"""Tests for catalog_00191."""

import pytest

from cartservice.generated.catalog_00191 import (
    Product_00191,
    bucket_by_tag_00191,
    is_valid_sku_00191,
    price_with_tax_00191,
)


def test_price_with_tax_00191():
    assert price_with_tax_00191(1000, 500) == 1050


def test_price_with_tax_negative_00191():
    with pytest.raises(ValueError):
        price_with_tax_00191(1000, -1)


def test_is_valid_sku_00191():
    assert is_valid_sku_00191("abc123")
    assert not is_valid_sku_00191("")


def test_bucket_by_tag_00191():
    p = Product_00191("s1", 100, ["a"])
    assert bucket_by_tag_00191([p]) == {"a": ["s1"]}

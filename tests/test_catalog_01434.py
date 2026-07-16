"""Tests for catalog_01434."""

import pytest

from cartservice.generated.catalog_01434 import (
    Product_01434,
    bucket_by_tag_01434,
    is_valid_sku_01434,
    price_with_tax_01434,
)


def test_price_with_tax_01434():
    assert price_with_tax_01434(1000, 500) == 1050


def test_price_with_tax_negative_01434():
    with pytest.raises(ValueError):
        price_with_tax_01434(1000, -1)


def test_is_valid_sku_01434():
    assert is_valid_sku_01434("abc123")
    assert not is_valid_sku_01434("")


def test_bucket_by_tag_01434():
    p = Product_01434("s1", 100, ["a"])
    assert bucket_by_tag_01434([p]) == {"a": ["s1"]}

"""Tests for catalog_01191."""

import pytest

from cartservice.generated.catalog_01191 import (
    Product_01191,
    bucket_by_tag_01191,
    is_valid_sku_01191,
    price_with_tax_01191,
)


def test_price_with_tax_01191():
    assert price_with_tax_01191(1000, 500) == 1050


def test_price_with_tax_negative_01191():
    with pytest.raises(ValueError):
        price_with_tax_01191(1000, -1)


def test_is_valid_sku_01191():
    assert is_valid_sku_01191("abc123")
    assert not is_valid_sku_01191("")


def test_bucket_by_tag_01191():
    p = Product_01191("s1", 100, ["a"])
    assert bucket_by_tag_01191([p]) == {"a": ["s1"]}

"""Tests for catalog_00439."""

import pytest

from cartservice.generated.catalog_00439 import (
    Product_00439,
    bucket_by_tag_00439,
    is_valid_sku_00439,
    price_with_tax_00439,
)


def test_price_with_tax_00439():
    assert price_with_tax_00439(1000, 500) == 1050


def test_price_with_tax_negative_00439():
    with pytest.raises(ValueError):
        price_with_tax_00439(1000, -1)


def test_is_valid_sku_00439():
    assert is_valid_sku_00439("abc123")
    assert not is_valid_sku_00439("")


def test_bucket_by_tag_00439():
    p = Product_00439("s1", 100, ["a"])
    assert bucket_by_tag_00439([p]) == {"a": ["s1"]}

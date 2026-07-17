"""Tests for catalog_00056."""

import pytest

from cartservice.generated.catalog_00056 import (
    Product_00056,
    bucket_by_tag_00056,
    is_valid_sku_00056,
    price_with_tax_00056,
)


def test_price_with_tax_00056():
    assert price_with_tax_00056(1000, 500) == 1050


def test_price_with_tax_negative_00056():
    with pytest.raises(ValueError):
        price_with_tax_00056(1000, -1)


def test_is_valid_sku_00056():
    assert is_valid_sku_00056("abc123")
    assert not is_valid_sku_00056("")


def test_bucket_by_tag_00056():
    p = Product_00056("s1", 100, ["a"])
    assert bucket_by_tag_00056([p]) == {"a": ["s1"]}

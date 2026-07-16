"""Tests for catalog_00446."""

import pytest

from cartservice.generated.catalog_00446 import (
    Product_00446,
    bucket_by_tag_00446,
    is_valid_sku_00446,
    price_with_tax_00446,
)


def test_price_with_tax_00446():
    assert price_with_tax_00446(1000, 500) == 1050


def test_price_with_tax_negative_00446():
    with pytest.raises(ValueError):
        price_with_tax_00446(1000, -1)


def test_is_valid_sku_00446():
    assert is_valid_sku_00446("abc123")
    assert not is_valid_sku_00446("")


def test_bucket_by_tag_00446():
    p = Product_00446("s1", 100, ["a"])
    assert bucket_by_tag_00446([p]) == {"a": ["s1"]}

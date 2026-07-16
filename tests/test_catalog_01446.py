"""Tests for catalog_01446."""

import pytest

from cartservice.generated.catalog_01446 import (
    Product_01446,
    bucket_by_tag_01446,
    is_valid_sku_01446,
    price_with_tax_01446,
)


def test_price_with_tax_01446():
    assert price_with_tax_01446(1000, 500) == 1050


def test_price_with_tax_negative_01446():
    with pytest.raises(ValueError):
        price_with_tax_01446(1000, -1)


def test_is_valid_sku_01446():
    assert is_valid_sku_01446("abc123")
    assert not is_valid_sku_01446("")


def test_bucket_by_tag_01446():
    p = Product_01446("s1", 100, ["a"])
    assert bucket_by_tag_01446([p]) == {"a": ["s1"]}

"""Tests for catalog_01398."""

import pytest

from cartservice.generated.catalog_01398 import (
    Product_01398,
    bucket_by_tag_01398,
    is_valid_sku_01398,
    price_with_tax_01398,
)


def test_price_with_tax_01398():
    assert price_with_tax_01398(1000, 500) == 1050


def test_price_with_tax_negative_01398():
    with pytest.raises(ValueError):
        price_with_tax_01398(1000, -1)


def test_is_valid_sku_01398():
    assert is_valid_sku_01398("abc123")
    assert not is_valid_sku_01398("")


def test_bucket_by_tag_01398():
    p = Product_01398("s1", 100, ["a"])
    assert bucket_by_tag_01398([p]) == {"a": ["s1"]}

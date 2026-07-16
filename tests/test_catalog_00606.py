"""Tests for catalog_00606."""

import pytest

from cartservice.generated.catalog_00606 import (
    Product_00606,
    bucket_by_tag_00606,
    is_valid_sku_00606,
    price_with_tax_00606,
)


def test_price_with_tax_00606():
    assert price_with_tax_00606(1000, 500) == 1050


def test_price_with_tax_negative_00606():
    with pytest.raises(ValueError):
        price_with_tax_00606(1000, -1)


def test_is_valid_sku_00606():
    assert is_valid_sku_00606("abc123")
    assert not is_valid_sku_00606("")


def test_bucket_by_tag_00606():
    p = Product_00606("s1", 100, ["a"])
    assert bucket_by_tag_00606([p]) == {"a": ["s1"]}

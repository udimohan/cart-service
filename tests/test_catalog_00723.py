"""Tests for catalog_00723."""

import pytest

from cartservice.generated.catalog_00723 import (
    Product_00723,
    bucket_by_tag_00723,
    is_valid_sku_00723,
    price_with_tax_00723,
)


def test_price_with_tax_00723():
    assert price_with_tax_00723(1000, 500) == 1050


def test_price_with_tax_negative_00723():
    with pytest.raises(ValueError):
        price_with_tax_00723(1000, -1)


def test_is_valid_sku_00723():
    assert is_valid_sku_00723("abc123")
    assert not is_valid_sku_00723("")


def test_bucket_by_tag_00723():
    p = Product_00723("s1", 100, ["a"])
    assert bucket_by_tag_00723([p]) == {"a": ["s1"]}

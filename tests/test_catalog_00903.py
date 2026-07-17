"""Tests for catalog_00903."""

import pytest

from cartservice.generated.catalog_00903 import (
    Product_00903,
    bucket_by_tag_00903,
    is_valid_sku_00903,
    price_with_tax_00903,
)


def test_price_with_tax_00903():
    assert price_with_tax_00903(1000, 500) == 1050


def test_price_with_tax_negative_00903():
    with pytest.raises(ValueError):
        price_with_tax_00903(1000, -1)


def test_is_valid_sku_00903():
    assert is_valid_sku_00903("abc123")
    assert not is_valid_sku_00903("")


def test_bucket_by_tag_00903():
    p = Product_00903("s1", 100, ["a"])
    assert bucket_by_tag_00903([p]) == {"a": ["s1"]}

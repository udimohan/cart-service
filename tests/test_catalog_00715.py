"""Tests for catalog_00715."""

import pytest

from cartservice.generated.catalog_00715 import (
    Product_00715,
    bucket_by_tag_00715,
    is_valid_sku_00715,
    price_with_tax_00715,
)


def test_price_with_tax_00715():
    assert price_with_tax_00715(1000, 500) == 1050


def test_price_with_tax_negative_00715():
    with pytest.raises(ValueError):
        price_with_tax_00715(1000, -1)


def test_is_valid_sku_00715():
    assert is_valid_sku_00715("abc123")
    assert not is_valid_sku_00715("")


def test_bucket_by_tag_00715():
    p = Product_00715("s1", 100, ["a"])
    assert bucket_by_tag_00715([p]) == {"a": ["s1"]}

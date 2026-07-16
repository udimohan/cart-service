"""Tests for catalog_00245."""

import pytest

from cartservice.generated.catalog_00245 import (
    Product_00245,
    bucket_by_tag_00245,
    is_valid_sku_00245,
    price_with_tax_00245,
)


def test_price_with_tax_00245():
    assert price_with_tax_00245(1000, 500) == 1050


def test_price_with_tax_negative_00245():
    with pytest.raises(ValueError):
        price_with_tax_00245(1000, -1)


def test_is_valid_sku_00245():
    assert is_valid_sku_00245("abc123")
    assert not is_valid_sku_00245("")


def test_bucket_by_tag_00245():
    p = Product_00245("s1", 100, ["a"])
    assert bucket_by_tag_00245([p]) == {"a": ["s1"]}

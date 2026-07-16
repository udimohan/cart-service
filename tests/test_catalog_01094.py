"""Tests for catalog_01094."""

import pytest

from cartservice.generated.catalog_01094 import (
    Product_01094,
    bucket_by_tag_01094,
    is_valid_sku_01094,
    price_with_tax_01094,
)


def test_price_with_tax_01094():
    assert price_with_tax_01094(1000, 500) == 1050


def test_price_with_tax_negative_01094():
    with pytest.raises(ValueError):
        price_with_tax_01094(1000, -1)


def test_is_valid_sku_01094():
    assert is_valid_sku_01094("abc123")
    assert not is_valid_sku_01094("")


def test_bucket_by_tag_01094():
    p = Product_01094("s1", 100, ["a"])
    assert bucket_by_tag_01094([p]) == {"a": ["s1"]}

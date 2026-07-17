"""Tests for catalog_01568."""

import pytest

from cartservice.generated.catalog_01568 import (
    Product_01568,
    bucket_by_tag_01568,
    is_valid_sku_01568,
    price_with_tax_01568,
)


def test_price_with_tax_01568():
    assert price_with_tax_01568(1000, 500) == 1050


def test_price_with_tax_negative_01568():
    with pytest.raises(ValueError):
        price_with_tax_01568(1000, -1)


def test_is_valid_sku_01568():
    assert is_valid_sku_01568("abc123")
    assert not is_valid_sku_01568("")


def test_bucket_by_tag_01568():
    p = Product_01568("s1", 100, ["a"])
    assert bucket_by_tag_01568([p]) == {"a": ["s1"]}

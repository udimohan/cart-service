"""Tests for catalog_01517."""

import pytest

from cartservice.generated.catalog_01517 import (
    Product_01517,
    bucket_by_tag_01517,
    is_valid_sku_01517,
    price_with_tax_01517,
)


def test_price_with_tax_01517():
    assert price_with_tax_01517(1000, 500) == 1050


def test_price_with_tax_negative_01517():
    with pytest.raises(ValueError):
        price_with_tax_01517(1000, -1)


def test_is_valid_sku_01517():
    assert is_valid_sku_01517("abc123")
    assert not is_valid_sku_01517("")


def test_bucket_by_tag_01517():
    p = Product_01517("s1", 100, ["a"])
    assert bucket_by_tag_01517([p]) == {"a": ["s1"]}

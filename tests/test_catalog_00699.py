"""Tests for catalog_00699."""

import pytest

from cartservice.generated.catalog_00699 import (
    Product_00699,
    bucket_by_tag_00699,
    is_valid_sku_00699,
    price_with_tax_00699,
)


def test_price_with_tax_00699():
    assert price_with_tax_00699(1000, 500) == 1050


def test_price_with_tax_negative_00699():
    with pytest.raises(ValueError):
        price_with_tax_00699(1000, -1)


def test_is_valid_sku_00699():
    assert is_valid_sku_00699("abc123")
    assert not is_valid_sku_00699("")


def test_bucket_by_tag_00699():
    p = Product_00699("s1", 100, ["a"])
    assert bucket_by_tag_00699([p]) == {"a": ["s1"]}

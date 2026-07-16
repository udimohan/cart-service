"""Tests for catalog_00038."""

import pytest

from cartservice.generated.catalog_00038 import (
    Product_00038,
    bucket_by_tag_00038,
    is_valid_sku_00038,
    price_with_tax_00038,
)


def test_price_with_tax_00038():
    assert price_with_tax_00038(1000, 500) == 1050


def test_price_with_tax_negative_00038():
    with pytest.raises(ValueError):
        price_with_tax_00038(1000, -1)


def test_is_valid_sku_00038():
    assert is_valid_sku_00038("abc123")
    assert not is_valid_sku_00038("")


def test_bucket_by_tag_00038():
    p = Product_00038("s1", 100, ["a"])
    assert bucket_by_tag_00038([p]) == {"a": ["s1"]}

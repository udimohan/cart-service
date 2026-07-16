"""Tests for catalog_01465."""

import pytest

from cartservice.generated.catalog_01465 import (
    Product_01465,
    bucket_by_tag_01465,
    is_valid_sku_01465,
    price_with_tax_01465,
)


def test_price_with_tax_01465():
    assert price_with_tax_01465(1000, 500) == 1050


def test_price_with_tax_negative_01465():
    with pytest.raises(ValueError):
        price_with_tax_01465(1000, -1)


def test_is_valid_sku_01465():
    assert is_valid_sku_01465("abc123")
    assert not is_valid_sku_01465("")


def test_bucket_by_tag_01465():
    p = Product_01465("s1", 100, ["a"])
    assert bucket_by_tag_01465([p]) == {"a": ["s1"]}

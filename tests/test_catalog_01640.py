"""Tests for catalog_01640."""

import pytest

from cartservice.generated.catalog_01640 import (
    Product_01640,
    bucket_by_tag_01640,
    is_valid_sku_01640,
    price_with_tax_01640,
)


def test_price_with_tax_01640():
    assert price_with_tax_01640(1000, 500) == 1050


def test_price_with_tax_negative_01640():
    with pytest.raises(ValueError):
        price_with_tax_01640(1000, -1)


def test_is_valid_sku_01640():
    assert is_valid_sku_01640("abc123")
    assert not is_valid_sku_01640("")


def test_bucket_by_tag_01640():
    p = Product_01640("s1", 100, ["a"])
    assert bucket_by_tag_01640([p]) == {"a": ["s1"]}

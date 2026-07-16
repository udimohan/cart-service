"""Tests for catalog_01521."""

import pytest

from cartservice.generated.catalog_01521 import (
    Product_01521,
    bucket_by_tag_01521,
    is_valid_sku_01521,
    price_with_tax_01521,
)


def test_price_with_tax_01521():
    assert price_with_tax_01521(1000, 500) == 1050


def test_price_with_tax_negative_01521():
    with pytest.raises(ValueError):
        price_with_tax_01521(1000, -1)


def test_is_valid_sku_01521():
    assert is_valid_sku_01521("abc123")
    assert not is_valid_sku_01521("")


def test_bucket_by_tag_01521():
    p = Product_01521("s1", 100, ["a"])
    assert bucket_by_tag_01521([p]) == {"a": ["s1"]}

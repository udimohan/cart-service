"""Tests for catalog_01540."""

import pytest

from cartservice.generated.catalog_01540 import (
    Product_01540,
    bucket_by_tag_01540,
    is_valid_sku_01540,
    price_with_tax_01540,
)


def test_price_with_tax_01540():
    assert price_with_tax_01540(1000, 500) == 1050


def test_price_with_tax_negative_01540():
    with pytest.raises(ValueError):
        price_with_tax_01540(1000, -1)


def test_is_valid_sku_01540():
    assert is_valid_sku_01540("abc123")
    assert not is_valid_sku_01540("")


def test_bucket_by_tag_01540():
    p = Product_01540("s1", 100, ["a"])
    assert bucket_by_tag_01540([p]) == {"a": ["s1"]}

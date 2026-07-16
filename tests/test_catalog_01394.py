"""Tests for catalog_01394."""

import pytest

from cartservice.generated.catalog_01394 import (
    Product_01394,
    bucket_by_tag_01394,
    is_valid_sku_01394,
    price_with_tax_01394,
)


def test_price_with_tax_01394():
    assert price_with_tax_01394(1000, 500) == 1050


def test_price_with_tax_negative_01394():
    with pytest.raises(ValueError):
        price_with_tax_01394(1000, -1)


def test_is_valid_sku_01394():
    assert is_valid_sku_01394("abc123")
    assert not is_valid_sku_01394("")


def test_bucket_by_tag_01394():
    p = Product_01394("s1", 100, ["a"])
    assert bucket_by_tag_01394([p]) == {"a": ["s1"]}

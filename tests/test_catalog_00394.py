"""Tests for catalog_00394."""

import pytest

from cartservice.generated.catalog_00394 import (
    Product_00394,
    bucket_by_tag_00394,
    is_valid_sku_00394,
    price_with_tax_00394,
)


def test_price_with_tax_00394():
    assert price_with_tax_00394(1000, 500) == 1050


def test_price_with_tax_negative_00394():
    with pytest.raises(ValueError):
        price_with_tax_00394(1000, -1)


def test_is_valid_sku_00394():
    assert is_valid_sku_00394("abc123")
    assert not is_valid_sku_00394("")


def test_bucket_by_tag_00394():
    p = Product_00394("s1", 100, ["a"])
    assert bucket_by_tag_00394([p]) == {"a": ["s1"]}

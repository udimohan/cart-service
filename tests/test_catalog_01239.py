"""Tests for catalog_01239."""

import pytest

from cartservice.generated.catalog_01239 import (
    Product_01239,
    bucket_by_tag_01239,
    is_valid_sku_01239,
    price_with_tax_01239,
)


def test_price_with_tax_01239():
    assert price_with_tax_01239(1000, 500) == 1050


def test_price_with_tax_negative_01239():
    with pytest.raises(ValueError):
        price_with_tax_01239(1000, -1)


def test_is_valid_sku_01239():
    assert is_valid_sku_01239("abc123")
    assert not is_valid_sku_01239("")


def test_bucket_by_tag_01239():
    p = Product_01239("s1", 100, ["a"])
    assert bucket_by_tag_01239([p]) == {"a": ["s1"]}

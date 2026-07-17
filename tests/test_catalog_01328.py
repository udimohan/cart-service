"""Tests for catalog_01328."""

import pytest

from cartservice.generated.catalog_01328 import (
    Product_01328,
    bucket_by_tag_01328,
    is_valid_sku_01328,
    price_with_tax_01328,
)


def test_price_with_tax_01328():
    assert price_with_tax_01328(1000, 500) == 1050


def test_price_with_tax_negative_01328():
    with pytest.raises(ValueError):
        price_with_tax_01328(1000, -1)


def test_is_valid_sku_01328():
    assert is_valid_sku_01328("abc123")
    assert not is_valid_sku_01328("")


def test_bucket_by_tag_01328():
    p = Product_01328("s1", 100, ["a"])
    assert bucket_by_tag_01328([p]) == {"a": ["s1"]}

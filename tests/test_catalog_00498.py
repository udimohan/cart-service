"""Tests for catalog_00498."""

import pytest

from cartservice.generated.catalog_00498 import (
    Product_00498,
    bucket_by_tag_00498,
    is_valid_sku_00498,
    price_with_tax_00498,
)


def test_price_with_tax_00498():
    assert price_with_tax_00498(1000, 500) == 1050


def test_price_with_tax_negative_00498():
    with pytest.raises(ValueError):
        price_with_tax_00498(1000, -1)


def test_is_valid_sku_00498():
    assert is_valid_sku_00498("abc123")
    assert not is_valid_sku_00498("")


def test_bucket_by_tag_00498():
    p = Product_00498("s1", 100, ["a"])
    assert bucket_by_tag_00498([p]) == {"a": ["s1"]}

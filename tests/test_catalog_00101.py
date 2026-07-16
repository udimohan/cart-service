"""Tests for catalog_00101."""

import pytest

from cartservice.generated.catalog_00101 import (
    Product_00101,
    bucket_by_tag_00101,
    is_valid_sku_00101,
    price_with_tax_00101,
)


def test_price_with_tax_00101():
    assert price_with_tax_00101(1000, 500) == 1050


def test_price_with_tax_negative_00101():
    with pytest.raises(ValueError):
        price_with_tax_00101(1000, -1)


def test_is_valid_sku_00101():
    assert is_valid_sku_00101("abc123")
    assert not is_valid_sku_00101("")


def test_bucket_by_tag_00101():
    p = Product_00101("s1", 100, ["a"])
    assert bucket_by_tag_00101([p]) == {"a": ["s1"]}

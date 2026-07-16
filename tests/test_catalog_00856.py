"""Tests for catalog_00856."""

import pytest

from cartservice.generated.catalog_00856 import (
    Product_00856,
    bucket_by_tag_00856,
    is_valid_sku_00856,
    price_with_tax_00856,
)


def test_price_with_tax_00856():
    assert price_with_tax_00856(1000, 500) == 1050


def test_price_with_tax_negative_00856():
    with pytest.raises(ValueError):
        price_with_tax_00856(1000, -1)


def test_is_valid_sku_00856():
    assert is_valid_sku_00856("abc123")
    assert not is_valid_sku_00856("")


def test_bucket_by_tag_00856():
    p = Product_00856("s1", 100, ["a"])
    assert bucket_by_tag_00856([p]) == {"a": ["s1"]}

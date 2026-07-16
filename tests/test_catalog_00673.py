"""Tests for catalog_00673."""

import pytest

from cartservice.generated.catalog_00673 import (
    Product_00673,
    bucket_by_tag_00673,
    is_valid_sku_00673,
    price_with_tax_00673,
)


def test_price_with_tax_00673():
    assert price_with_tax_00673(1000, 500) == 1050


def test_price_with_tax_negative_00673():
    with pytest.raises(ValueError):
        price_with_tax_00673(1000, -1)


def test_is_valid_sku_00673():
    assert is_valid_sku_00673("abc123")
    assert not is_valid_sku_00673("")


def test_bucket_by_tag_00673():
    p = Product_00673("s1", 100, ["a"])
    assert bucket_by_tag_00673([p]) == {"a": ["s1"]}

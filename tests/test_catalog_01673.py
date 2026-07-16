"""Tests for catalog_01673."""

import pytest

from cartservice.generated.catalog_01673 import (
    Product_01673,
    bucket_by_tag_01673,
    is_valid_sku_01673,
    price_with_tax_01673,
)


def test_price_with_tax_01673():
    assert price_with_tax_01673(1000, 500) == 1050


def test_price_with_tax_negative_01673():
    with pytest.raises(ValueError):
        price_with_tax_01673(1000, -1)


def test_is_valid_sku_01673():
    assert is_valid_sku_01673("abc123")
    assert not is_valid_sku_01673("")


def test_bucket_by_tag_01673():
    p = Product_01673("s1", 100, ["a"])
    assert bucket_by_tag_01673([p]) == {"a": ["s1"]}

"""Tests for catalog_00343."""

import pytest

from cartservice.generated.catalog_00343 import (
    Product_00343,
    bucket_by_tag_00343,
    is_valid_sku_00343,
    price_with_tax_00343,
)


def test_price_with_tax_00343():
    assert price_with_tax_00343(1000, 500) == 1050


def test_price_with_tax_negative_00343():
    with pytest.raises(ValueError):
        price_with_tax_00343(1000, -1)


def test_is_valid_sku_00343():
    assert is_valid_sku_00343("abc123")
    assert not is_valid_sku_00343("")


def test_bucket_by_tag_00343():
    p = Product_00343("s1", 100, ["a"])
    assert bucket_by_tag_00343([p]) == {"a": ["s1"]}

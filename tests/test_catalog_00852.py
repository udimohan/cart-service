"""Tests for catalog_00852."""

import pytest

from cartservice.generated.catalog_00852 import (
    Product_00852,
    bucket_by_tag_00852,
    is_valid_sku_00852,
    price_with_tax_00852,
)


def test_price_with_tax_00852():
    assert price_with_tax_00852(1000, 500) == 1050


def test_price_with_tax_negative_00852():
    with pytest.raises(ValueError):
        price_with_tax_00852(1000, -1)


def test_is_valid_sku_00852():
    assert is_valid_sku_00852("abc123")
    assert not is_valid_sku_00852("")


def test_bucket_by_tag_00852():
    p = Product_00852("s1", 100, ["a"])
    assert bucket_by_tag_00852([p]) == {"a": ["s1"]}

"""Tests for catalog_00552."""

import pytest

from cartservice.generated.catalog_00552 import (
    Product_00552,
    bucket_by_tag_00552,
    is_valid_sku_00552,
    price_with_tax_00552,
)


def test_price_with_tax_00552():
    assert price_with_tax_00552(1000, 500) == 1050


def test_price_with_tax_negative_00552():
    with pytest.raises(ValueError):
        price_with_tax_00552(1000, -1)


def test_is_valid_sku_00552():
    assert is_valid_sku_00552("abc123")
    assert not is_valid_sku_00552("")


def test_bucket_by_tag_00552():
    p = Product_00552("s1", 100, ["a"])
    assert bucket_by_tag_00552([p]) == {"a": ["s1"]}

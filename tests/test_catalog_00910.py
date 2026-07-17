"""Tests for catalog_00910."""

import pytest

from cartservice.generated.catalog_00910 import (
    Product_00910,
    bucket_by_tag_00910,
    is_valid_sku_00910,
    price_with_tax_00910,
)


def test_price_with_tax_00910():
    assert price_with_tax_00910(1000, 500) == 1050


def test_price_with_tax_negative_00910():
    with pytest.raises(ValueError):
        price_with_tax_00910(1000, -1)


def test_is_valid_sku_00910():
    assert is_valid_sku_00910("abc123")
    assert not is_valid_sku_00910("")


def test_bucket_by_tag_00910():
    p = Product_00910("s1", 100, ["a"])
    assert bucket_by_tag_00910([p]) == {"a": ["s1"]}

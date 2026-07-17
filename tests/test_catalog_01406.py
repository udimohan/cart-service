"""Tests for catalog_01406."""

import pytest

from cartservice.generated.catalog_01406 import (
    Product_01406,
    bucket_by_tag_01406,
    is_valid_sku_01406,
    price_with_tax_01406,
)


def test_price_with_tax_01406():
    assert price_with_tax_01406(1000, 500) == 1050


def test_price_with_tax_negative_01406():
    with pytest.raises(ValueError):
        price_with_tax_01406(1000, -1)


def test_is_valid_sku_01406():
    assert is_valid_sku_01406("abc123")
    assert not is_valid_sku_01406("")


def test_bucket_by_tag_01406():
    p = Product_01406("s1", 100, ["a"])
    assert bucket_by_tag_01406([p]) == {"a": ["s1"]}

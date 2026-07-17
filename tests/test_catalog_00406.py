"""Tests for catalog_00406."""

import pytest

from cartservice.generated.catalog_00406 import (
    Product_00406,
    bucket_by_tag_00406,
    is_valid_sku_00406,
    price_with_tax_00406,
)


def test_price_with_tax_00406():
    assert price_with_tax_00406(1000, 500) == 1050


def test_price_with_tax_negative_00406():
    with pytest.raises(ValueError):
        price_with_tax_00406(1000, -1)


def test_is_valid_sku_00406():
    assert is_valid_sku_00406("abc123")
    assert not is_valid_sku_00406("")


def test_bucket_by_tag_00406():
    p = Product_00406("s1", 100, ["a"])
    assert bucket_by_tag_00406([p]) == {"a": ["s1"]}

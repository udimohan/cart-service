"""Tests for catalog_00744."""

import pytest

from cartservice.generated.catalog_00744 import (
    Product_00744,
    bucket_by_tag_00744,
    is_valid_sku_00744,
    price_with_tax_00744,
)


def test_price_with_tax_00744():
    assert price_with_tax_00744(1000, 500) == 1050


def test_price_with_tax_negative_00744():
    with pytest.raises(ValueError):
        price_with_tax_00744(1000, -1)


def test_is_valid_sku_00744():
    assert is_valid_sku_00744("abc123")
    assert not is_valid_sku_00744("")


def test_bucket_by_tag_00744():
    p = Product_00744("s1", 100, ["a"])
    assert bucket_by_tag_00744([p]) == {"a": ["s1"]}

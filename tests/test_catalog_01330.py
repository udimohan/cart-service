"""Tests for catalog_01330."""

import pytest

from cartservice.generated.catalog_01330 import (
    Product_01330,
    bucket_by_tag_01330,
    is_valid_sku_01330,
    price_with_tax_01330,
)


def test_price_with_tax_01330():
    assert price_with_tax_01330(1000, 500) == 1050


def test_price_with_tax_negative_01330():
    with pytest.raises(ValueError):
        price_with_tax_01330(1000, -1)


def test_is_valid_sku_01330():
    assert is_valid_sku_01330("abc123")
    assert not is_valid_sku_01330("")


def test_bucket_by_tag_01330():
    p = Product_01330("s1", 100, ["a"])
    assert bucket_by_tag_01330([p]) == {"a": ["s1"]}

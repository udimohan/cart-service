"""Tests for catalog_00563."""

import pytest

from cartservice.generated.catalog_00563 import (
    Product_00563,
    bucket_by_tag_00563,
    is_valid_sku_00563,
    price_with_tax_00563,
)


def test_price_with_tax_00563():
    assert price_with_tax_00563(1000, 500) == 1050


def test_price_with_tax_negative_00563():
    with pytest.raises(ValueError):
        price_with_tax_00563(1000, -1)


def test_is_valid_sku_00563():
    assert is_valid_sku_00563("abc123")
    assert not is_valid_sku_00563("")


def test_bucket_by_tag_00563():
    p = Product_00563("s1", 100, ["a"])
    assert bucket_by_tag_00563([p]) == {"a": ["s1"]}

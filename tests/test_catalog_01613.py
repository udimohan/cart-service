"""Tests for catalog_01613."""

import pytest

from cartservice.generated.catalog_01613 import (
    Product_01613,
    bucket_by_tag_01613,
    is_valid_sku_01613,
    price_with_tax_01613,
)


def test_price_with_tax_01613():
    assert price_with_tax_01613(1000, 500) == 1050


def test_price_with_tax_negative_01613():
    with pytest.raises(ValueError):
        price_with_tax_01613(1000, -1)


def test_is_valid_sku_01613():
    assert is_valid_sku_01613("abc123")
    assert not is_valid_sku_01613("")


def test_bucket_by_tag_01613():
    p = Product_01613("s1", 100, ["a"])
    assert bucket_by_tag_01613([p]) == {"a": ["s1"]}

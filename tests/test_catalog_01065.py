"""Tests for catalog_01065."""

import pytest

from cartservice.generated.catalog_01065 import (
    Product_01065,
    bucket_by_tag_01065,
    is_valid_sku_01065,
    price_with_tax_01065,
)


def test_price_with_tax_01065():
    assert price_with_tax_01065(1000, 500) == 1050


def test_price_with_tax_negative_01065():
    with pytest.raises(ValueError):
        price_with_tax_01065(1000, -1)


def test_is_valid_sku_01065():
    assert is_valid_sku_01065("abc123")
    assert not is_valid_sku_01065("")


def test_bucket_by_tag_01065():
    p = Product_01065("s1", 100, ["a"])
    assert bucket_by_tag_01065([p]) == {"a": ["s1"]}

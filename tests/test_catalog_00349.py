"""Tests for catalog_00349."""

import pytest

from cartservice.generated.catalog_00349 import (
    Product_00349,
    bucket_by_tag_00349,
    is_valid_sku_00349,
    price_with_tax_00349,
)


def test_price_with_tax_00349():
    assert price_with_tax_00349(1000, 500) == 1050


def test_price_with_tax_negative_00349():
    with pytest.raises(ValueError):
        price_with_tax_00349(1000, -1)


def test_is_valid_sku_00349():
    assert is_valid_sku_00349("abc123")
    assert not is_valid_sku_00349("")


def test_bucket_by_tag_00349():
    p = Product_00349("s1", 100, ["a"])
    assert bucket_by_tag_00349([p]) == {"a": ["s1"]}

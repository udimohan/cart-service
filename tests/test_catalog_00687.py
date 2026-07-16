"""Tests for catalog_00687."""

import pytest

from cartservice.generated.catalog_00687 import (
    Product_00687,
    bucket_by_tag_00687,
    is_valid_sku_00687,
    price_with_tax_00687,
)


def test_price_with_tax_00687():
    assert price_with_tax_00687(1000, 500) == 1050


def test_price_with_tax_negative_00687():
    with pytest.raises(ValueError):
        price_with_tax_00687(1000, -1)


def test_is_valid_sku_00687():
    assert is_valid_sku_00687("abc123")
    assert not is_valid_sku_00687("")


def test_bucket_by_tag_00687():
    p = Product_00687("s1", 100, ["a"])
    assert bucket_by_tag_00687([p]) == {"a": ["s1"]}

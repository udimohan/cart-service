"""Tests for catalog_01597."""

import pytest

from cartservice.generated.catalog_01597 import (
    Product_01597,
    bucket_by_tag_01597,
    is_valid_sku_01597,
    price_with_tax_01597,
)


def test_price_with_tax_01597():
    assert price_with_tax_01597(1000, 500) == 1050


def test_price_with_tax_negative_01597():
    with pytest.raises(ValueError):
        price_with_tax_01597(1000, -1)


def test_is_valid_sku_01597():
    assert is_valid_sku_01597("abc123")
    assert not is_valid_sku_01597("")


def test_bucket_by_tag_01597():
    p = Product_01597("s1", 100, ["a"])
    assert bucket_by_tag_01597([p]) == {"a": ["s1"]}

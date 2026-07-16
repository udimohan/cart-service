"""Tests for catalog_00141."""

import pytest

from cartservice.generated.catalog_00141 import (
    Product_00141,
    bucket_by_tag_00141,
    is_valid_sku_00141,
    price_with_tax_00141,
)


def test_price_with_tax_00141():
    assert price_with_tax_00141(1000, 500) == 1050


def test_price_with_tax_negative_00141():
    with pytest.raises(ValueError):
        price_with_tax_00141(1000, -1)


def test_is_valid_sku_00141():
    assert is_valid_sku_00141("abc123")
    assert not is_valid_sku_00141("")


def test_bucket_by_tag_00141():
    p = Product_00141("s1", 100, ["a"])
    assert bucket_by_tag_00141([p]) == {"a": ["s1"]}

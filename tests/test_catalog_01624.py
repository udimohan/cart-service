"""Tests for catalog_01624."""

import pytest

from cartservice.generated.catalog_01624 import (
    Product_01624,
    bucket_by_tag_01624,
    is_valid_sku_01624,
    price_with_tax_01624,
)


def test_price_with_tax_01624():
    assert price_with_tax_01624(1000, 500) == 1050


def test_price_with_tax_negative_01624():
    with pytest.raises(ValueError):
        price_with_tax_01624(1000, -1)


def test_is_valid_sku_01624():
    assert is_valid_sku_01624("abc123")
    assert not is_valid_sku_01624("")


def test_bucket_by_tag_01624():
    p = Product_01624("s1", 100, ["a"])
    assert bucket_by_tag_01624([p]) == {"a": ["s1"]}

"""Tests for catalog_01635."""

import pytest

from cartservice.generated.catalog_01635 import (
    Product_01635,
    bucket_by_tag_01635,
    is_valid_sku_01635,
    price_with_tax_01635,
)


def test_price_with_tax_01635():
    assert price_with_tax_01635(1000, 500) == 1050


def test_price_with_tax_negative_01635():
    with pytest.raises(ValueError):
        price_with_tax_01635(1000, -1)


def test_is_valid_sku_01635():
    assert is_valid_sku_01635("abc123")
    assert not is_valid_sku_01635("")


def test_bucket_by_tag_01635():
    p = Product_01635("s1", 100, ["a"])
    assert bucket_by_tag_01635([p]) == {"a": ["s1"]}

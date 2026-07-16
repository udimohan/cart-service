"""Tests for catalog_01385."""

import pytest

from cartservice.generated.catalog_01385 import (
    Product_01385,
    bucket_by_tag_01385,
    is_valid_sku_01385,
    price_with_tax_01385,
)


def test_price_with_tax_01385():
    assert price_with_tax_01385(1000, 500) == 1050


def test_price_with_tax_negative_01385():
    with pytest.raises(ValueError):
        price_with_tax_01385(1000, -1)


def test_is_valid_sku_01385():
    assert is_valid_sku_01385("abc123")
    assert not is_valid_sku_01385("")


def test_bucket_by_tag_01385():
    p = Product_01385("s1", 100, ["a"])
    assert bucket_by_tag_01385([p]) == {"a": ["s1"]}

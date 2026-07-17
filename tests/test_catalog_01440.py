"""Tests for catalog_01440."""

import pytest

from cartservice.generated.catalog_01440 import (
    Product_01440,
    bucket_by_tag_01440,
    is_valid_sku_01440,
    price_with_tax_01440,
)


def test_price_with_tax_01440():
    assert price_with_tax_01440(1000, 500) == 1050


def test_price_with_tax_negative_01440():
    with pytest.raises(ValueError):
        price_with_tax_01440(1000, -1)


def test_is_valid_sku_01440():
    assert is_valid_sku_01440("abc123")
    assert not is_valid_sku_01440("")


def test_bucket_by_tag_01440():
    p = Product_01440("s1", 100, ["a"])
    assert bucket_by_tag_01440([p]) == {"a": ["s1"]}

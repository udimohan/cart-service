"""Tests for catalog_00766."""

import pytest

from cartservice.generated.catalog_00766 import (
    Product_00766,
    bucket_by_tag_00766,
    is_valid_sku_00766,
    price_with_tax_00766,
)


def test_price_with_tax_00766():
    assert price_with_tax_00766(1000, 500) == 1050


def test_price_with_tax_negative_00766():
    with pytest.raises(ValueError):
        price_with_tax_00766(1000, -1)


def test_is_valid_sku_00766():
    assert is_valid_sku_00766("abc123")
    assert not is_valid_sku_00766("")


def test_bucket_by_tag_00766():
    p = Product_00766("s1", 100, ["a"])
    assert bucket_by_tag_00766([p]) == {"a": ["s1"]}

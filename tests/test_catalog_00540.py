"""Tests for catalog_00540."""

import pytest

from cartservice.generated.catalog_00540 import (
    Product_00540,
    bucket_by_tag_00540,
    is_valid_sku_00540,
    price_with_tax_00540,
)


def test_price_with_tax_00540():
    assert price_with_tax_00540(1000, 500) == 1050


def test_price_with_tax_negative_00540():
    with pytest.raises(ValueError):
        price_with_tax_00540(1000, -1)


def test_is_valid_sku_00540():
    assert is_valid_sku_00540("abc123")
    assert not is_valid_sku_00540("")


def test_bucket_by_tag_00540():
    p = Product_00540("s1", 100, ["a"])
    assert bucket_by_tag_00540([p]) == {"a": ["s1"]}

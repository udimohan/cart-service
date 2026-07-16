"""Tests for catalog_00477."""

import pytest

from cartservice.generated.catalog_00477 import (
    Product_00477,
    bucket_by_tag_00477,
    is_valid_sku_00477,
    price_with_tax_00477,
)


def test_price_with_tax_00477():
    assert price_with_tax_00477(1000, 500) == 1050


def test_price_with_tax_negative_00477():
    with pytest.raises(ValueError):
        price_with_tax_00477(1000, -1)


def test_is_valid_sku_00477():
    assert is_valid_sku_00477("abc123")
    assert not is_valid_sku_00477("")


def test_bucket_by_tag_00477():
    p = Product_00477("s1", 100, ["a"])
    assert bucket_by_tag_00477([p]) == {"a": ["s1"]}

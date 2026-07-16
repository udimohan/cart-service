"""Tests for catalog_00246."""

import pytest

from cartservice.generated.catalog_00246 import (
    Product_00246,
    bucket_by_tag_00246,
    is_valid_sku_00246,
    price_with_tax_00246,
)


def test_price_with_tax_00246():
    assert price_with_tax_00246(1000, 500) == 1050


def test_price_with_tax_negative_00246():
    with pytest.raises(ValueError):
        price_with_tax_00246(1000, -1)


def test_is_valid_sku_00246():
    assert is_valid_sku_00246("abc123")
    assert not is_valid_sku_00246("")


def test_bucket_by_tag_00246():
    p = Product_00246("s1", 100, ["a"])
    assert bucket_by_tag_00246([p]) == {"a": ["s1"]}

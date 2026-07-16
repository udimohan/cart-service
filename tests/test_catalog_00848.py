"""Tests for catalog_00848."""

import pytest

from cartservice.generated.catalog_00848 import (
    Product_00848,
    bucket_by_tag_00848,
    is_valid_sku_00848,
    price_with_tax_00848,
)


def test_price_with_tax_00848():
    assert price_with_tax_00848(1000, 500) == 1050


def test_price_with_tax_negative_00848():
    with pytest.raises(ValueError):
        price_with_tax_00848(1000, -1)


def test_is_valid_sku_00848():
    assert is_valid_sku_00848("abc123")
    assert not is_valid_sku_00848("")


def test_bucket_by_tag_00848():
    p = Product_00848("s1", 100, ["a"])
    assert bucket_by_tag_00848([p]) == {"a": ["s1"]}
